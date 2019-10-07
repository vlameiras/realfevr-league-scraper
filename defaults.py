REALFEVR_USERNAME = None
REALFEVR_PASSWORD = None
BASE_URL = 'https://fantasy.realfevr.com'
TEAMS_URL = '/teams/{}'
LOGIN_URL = '/users/sign_in?utf8=%E2%9C%93&authenticity_token=jRYO5H2JZlO12BzuGokujb5JpPHRhjuhzEDiuu6YuJ8%3D&user%5Bemail%5D={}&user%5Bremember_me%5D=0&user%5Bpassword%5D={}&button='.format(REALFEVR_USERNAME, REALFEVR_PASSWORD)
LEAGUE_IDS = []
LEAGUE_EXCLUDED_TEAMS = []
TABLE_FIELDS = ["Team", "Points", "Players Left"]
FAKE_USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0'
ADDITIONAL_HEADERS = {'User-Agent': FAKE_USER_AGENT}