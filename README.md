# RealFevr League Scraper

This small project was a request from a group of friends which love to play RealFevr. They are a group of 10+ people, so this is a problem since RealFevr leagues are limited to 10 teams. They have two leagues where they compete, but don't have a straightforward way to actually check who is performing best among all leagues.

Hence the creation of this small python application which scrapes RealFevr in a responsible way :)

Given a list of league ids and valid website credentials, it will scrape RealFevr using `requests` and `beautifulsoup4`. Results are printed in HTML or plain text via `PrettyTable`.

## Requirements
- Valid RealFevr credentials
- Provide a list of leagues which you have access to
  
## Installation
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
export FLASK_APP=app.app
export REALFEVR_USERNAME=<your_username>
export REALFEVR_PASSWORD=<your_password>
flask run
```

## Usage
**Plain text output**
```bash
curl -XGET http://127.0.0.1:5000/


+-----------------------+--------+--------------+
|          Team         | Points | Players Left |
+-----------------------+--------+--------------+
|    Buddies FC POR     |   2    |      11      |
|     Meister Canela    |   5    |      11      |
|         Alt+F1        |   1    |      11      |
|   The Cool Pirates1   |   0    |      11      |
|      S.L.Carnide      |   9    |      11      |
|     Nerdrage F.C.     |   11   |      10      |
|     Santarem 10 FC    |   0    |      11      |
|       Min Sports      |   4    |      11      |
|       SLB Lumiar      |   1    |      11      |
|       MarvelousFC     |   8    |      11      |
|   The Amazing 1s FC   |   14   |      10      |
|       Nigel S FC      |   3    |      11      |
|        FC KooL        |   9    |      11      |
|  No Way Jose Mate FC  |   10   |       9      |
|     Born2Win PORTG    |   1    |      11      |
|       Luke Pwnage     |   7    |      11      |
|    Soulmaster Team    |   5    |      11      |
|       NOP SCP FC      |   9    |      10      |
| Alfragide Alliance FC |   0    |      11      |
|      Carnaxide UTD    |   12   |      10      |
+-----------------------+--------+--------------+
```

**HTML Table output**

```bash
curl -XGET http://127.0.0.1:5000/html
...
```

## Linting
```
pylint app/
```

## Notes
Currently, the scraper will extract each team's round performance. In the near future it should also extract player informations.
