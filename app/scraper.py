from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
from .defaults import ADDITIONAL_HEADERS, BASE_URL, LEAGUE_IDS, LOGIN_URL, TEAMS_URL
from .client import HttpClient


class RealFevrScraper:
    def __init__(self):
        self._http_client = HttpClient(headers=ADDITIONAL_HEADERS)
        self._http_client.post(urljoin(BASE_URL, LOGIN_URL))
    
    def _process_response(self, response):
        return BeautifulSoup(response.text, features="html.parser")
    
    def _get_round_url(self, response):
        current_round_url = response.find("li", attrs={"data-main-submenu": "current_round"}).find("a", { "class": "sub-opt"}).get('href')
        return current_round_url
    
    def _fetch_league_results(self, league_id):
        response = self._http_client.get(urljoin(BASE_URL, TEAMS_URL.format(league_id)))
        response_soup = self._process_response(response.text)
        current_round_url = self._get_round_url(response_soup)
        response_round = self._http_client.get(urljoin(BASE_URL, current_round_url))
        response_round_soup = self._process_response(response_round.text)
        round_games = self._fetch_round_games(response_round_soup)
        round_games_detail = self._fetch_round_games_detail(round_games)
        return round_games_detail
    
    def fetch_leagues(self):     
        league_results = []
        for league_id in LEAGUE_IDS:
            league_results.append(self._fetch_league_results(league_id))
       
        return league_results

    def _fetch_round_games(self, response):
        round_games = response.find_all("div", {"class": "current-round-game"})
        return round_games

    def _fetch_round_games_detail(self, round_games):
        round_games_detail = []
        for round_game in round_games:
            team_modules = round_game.find_all("div", {"class": "team-module"})
            for team_module in team_modules:
                team_name = team_module.find("div", {"class": "team-info--name"}).find("a").get('title')
                team_score = team_module.find("div", {"class": "team-score"}).find("span").text.strip()
                
                try:
                    team_players_left = team_module.find("div", {"class": "team-info--playersLeft"}).find("span").text.strip()
                except Exception:
                    team_players_left = team_module.find("div", {"class": "team-info--playersLeft"}).text.strip()

                round_games_detail.append([team_name, team_score, team_players_left])
        return round_games_detail


