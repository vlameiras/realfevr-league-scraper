from flask import Flask
from prettytable import PrettyTable
import requests
from .defaults import TABLE_FIELDS
from .scraper import RealFevrScraper


app = Flask(__name__)

TABLE_OUTPUT = PrettyTable()
TABLE_OUTPUT.field_names = TABLE_FIELDS

SCRAPER = RealFevrScraper()

@app.route("/")
def results():
    try:
        league_results = SCRAPER.fetch_leagues()
    except requests.exceptions.RequestException:
        return "An error occurred while accessing RealFevr"
    for result in league_results:
        TABLE_OUTPUT.add_row(result)
    response = TABLE_OUTPUT.get_html_string(attributes={"border": 1})
    TABLE_OUTPUT.clear_rows()
    return response
