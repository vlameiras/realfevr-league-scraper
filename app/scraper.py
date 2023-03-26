"""Scraper module"""
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from app.defaults import ADDITIONAL_HEADERS, BASE_URL, LEAGUE_IDS, LOGIN_URL, TEAMS_URL
from app.client import HttpClient


class RealFevrScraper: # pylint: disable=too-few-public-methods
    """Scraper class which fetches and processes website raw content"""

    def __init__(self):
        self._http_client = HttpClient(headers=ADDITIONAL_HEADERS)
        self._http_client.post(urljoin(BASE_URL, LOGIN_URL))
        self.league_results = []
        self.teams = None
        self.round = None
        self.round_games = None

    def fetch_leagues(self):
        """Fetches leagues specified by the user"""
        self.league_results = []
        for league_id in LEAGUE_IDS:
            self._fetch_league_results(league_id)

    def _fetch_league_results(self, league_id):
        self._fetch_teams(league_id)
        self._fetch_round()
        self._fetch_round_games()
        self._fetch_round_games_detail()

    def _fetch_teams(self, league_id):
        response = self._http_client.get(
            urljoin(BASE_URL, TEAMS_URL.format(league_id)))
        self.teams = _process_response(response.text)

    def _fetch_round(self):
        current_round_url = self.teams.find(
            "li", attrs={"data-main-submenu": "current_round"}).find(
                "a", {"class": "sub-opt"}).get('href')
        response_round = self._http_client.get(
            urljoin(BASE_URL, current_round_url))
        self.round = _process_response(response_round.text)

    def _fetch_round_games(self):
        self.round_games = self.round.find_all(
            "div", {"class": "current-round-game"})

    def _fetch_round_games_detail(self):
        for round_game in self.round_games:
            team_modules = round_game.find_all("div", {"class": "team-module"})
            for team_module in team_modules:
                team_name = team_module.find(
                    "div", {"class": "team-info--name"}).find("a").get('title')
                team_score = team_module.find(
                    "div", {"class": "team-score"}).find("span").text.strip()
                try:
                    team_players_left = team_module.find(
                        "div", {"class": "team-info--playersLeft"}).find("span").text.strip()
                except Exception: #TODO: Add specific exception
                    team_players_left = team_module.find(
                        "div", {"class": "team-info--playersLeft"}).text.strip()
                self.league_results.append(
                    [team_name, team_score, team_players_left])


def _process_response(response):
    return BeautifulSoup(response, features="html.parser")
