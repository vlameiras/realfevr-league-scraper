import requests


class HttpClient:
    def __init__(self, headers=None):
        self._session = requests.Session()
        self._headers = headers

        if self._headers is None:
            self._headers = {}

    def _request(self, method, url, json=None):
        try:
            response = self._session.request(method=method, url=url, json=json, headers=self._headers)
        except requests.exceptions.RequestException:
            raise
        return response

    def get(self, url):
        response = self._request(method='GET', url=url)
        return response

    def post(self, url, json=None):
        response = self._request(method='POST', url=url, json=json)
        return response
