"""HTTP Client"""
import requests


class HttpClient:
    """Requests module wrapper"""
    def __init__(self, headers=None):
        self._session = requests.Session()
        self._headers = headers

        if self._headers is None:
            self._headers = {}

    def _request(self, method, url, json=None):
        try:
            response = self._session.request(method=method, url=url, json=json,
                                             headers=self._headers)
        except requests.exceptions.RequestException:
            raise
        return response

    def get(self, url):
        """Performs an HTTP GET request
        :param url: URL to be requested
        :return: Response object
        """
        response = self._request(method='GET', url=url)
        return response

    def post(self, url, json=None):
        """Performs an HTTP POST request
        :param url: URL to be requested
        :param json: JSON payload
        :return: Response object
        """
        response = self._request(method='POST', url=url, json=json)
        return response
