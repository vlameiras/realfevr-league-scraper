"""Main module of RealFevr League Scraper"""

from flask import Flask
from prettytable import PrettyTable
import requests
from .defaults import TABLE_FIELDS
from .scraper import RealFevrScraper


app = Flask(__name__)

table_output = PrettyTable()
table_output.field_names = TABLE_FIELDS

scraper = RealFevrScraper()


@app.route("/")
def results():
    """Scrapes user private RealFevr leagues
    :return: HTML table with results
    :rtype: HTML response
    """
    try:
        scraper.fetch_leagues()
    except requests.exceptions.RequestException:
        return "An error occurred while accessing RealFevr"
    for result in scraper.league_results:
        table_output.add_row(result)
    response = table_output.get_html_string(attributes={"border": 1})
    table_output.clear_rows()
    return response
