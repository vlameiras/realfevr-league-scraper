"""Main module of RealFevr League Scraper"""

from flask import Flask
from prettytable import PrettyTable
import requests
from app.defaults import TABLE_FIELDS
from app.scraper import RealFevrScraper


app = Flask(__name__)

table_output = PrettyTable()
table_output.field_names = TABLE_FIELDS

scraper = RealFevrScraper()



@app.route("/", defaults={"output_type": "plain"})
@app.route("/<string:output_type>")
def results(output_type='html'):
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
    if output_type == 'html':
        response = table_output.get_html_string(attributes={"border": 1})
    else:
        response = table_output.get_string()
    table_output.clear_rows()
    return response
