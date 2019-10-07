from defaults import ADDITIONAL_HEADERS, BASE_URL
from client import HttpClient
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

HTTP_SESSION = requests.Session()


class RealFevrScraper:
    def __init__(self):
        self._http_client = HttpClient(base_url=BASE_URL, headers=ADDITIONAL_HEADERS)

    def fetch_leagues(self):
        response = self._http_client.post(LOGIN_URL)

        league_results = []
        for league_id in defaults.LEAGUE_IDS:
            league_results.append(_fetch_league_results(response, session, league_id))
       
        return league_results

    def _fetch_league_results(self, league_id):
        response = self._http_client.get(TEAMS_URL.format(league_id))
        response_soup = _process_response(response.text)
        current_round_url = _get_round_url(response_soup)
        response_round = self._http_client.get(current_round_url)
        response_round_soup = _process_response(response_round.text)
        round_games = _fetch_round_games(response_round_soup)
        round_games_detail = _fetch_round_games_detail(round_games)
        return round_games_detail
    
    def _get_round_url(self, response):
        current_round_url = response.find("li", attrs={"data-main-submenu": "current_round"}).find("a", { "class": "sub-opt"}).get('href')
        return current_round_url

    def _fetch_round_games(self, response):
        round_games = response_round_soup.find_all("div", {"class": "current-round-game"})
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

    def _process_response(self, response):
        return BeautifulSoup(response.text, features="html.parser")
