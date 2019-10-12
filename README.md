# RealFevr League Scraper

This small project was a request from a group of friends which love to play RealFevr. They are a group of 10+ people, so this is a problem since RealFevr leagues are limited to 10 teams. They have two leagues where they compete, but don't have a straightforward way to actually check who is performing best among all leagues.

Hence the creation of this small python application which scrapes RealFevr in a responsible way :)

Given a list of league ids and valid website credentials, it will scrape RealFevr using `requests` and `beautifulsoup4`. Results are printed in a very simple table layout via `PrettyTable`

## Requirements
- Valid RealFevr credentials
- Provide a list of leagues which you have access to
  
## Usage
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
export FLASK_APP=app.app
flask run
```

## Notes
Currently it will extract each round team performance. In the near future it should also extract player informations
