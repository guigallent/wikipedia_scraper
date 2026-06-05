import requests

class CountryLeadersAPI:

    def __init__(self):
        """
        A wrapper for interacting with the Country Leaders API.

        Attributes:
            base_url (str): The base URL of the API.
            country_endpoint (str): Endpoint to retrieve supported countries.
            leaders_endpoint (str): Endpoint to retrieve leaders by country.
            cookies_endpoint (str): Endpoint to refresh the access cookie.
            session (requests.Session): A persistent session for optimized requests.
            cookies (requests.cookies.RequestsCookieJar): The current authentication cookies.
        """

        self.base_url = "https://country-leaders.onrender.com/"
        self.country_endpoint = self.base_url + "countries"
        self.leaders_endpoint = self.base_url + "leaders"
        self.cookies_endpoint = self.base_url + "cookie"
        self.session = requests.Session()
        self.cookies = self.refresh_cookie()
        
    def refresh_cookie(self):
        """Fetches and returns a fresh cookie from the API """

        return self.session.get(self.cookies_endpoint).cookies
        
    def get_countries(self):
        """
        Retrieves the list of supported countries from the API.

        Returns:
            list: A list of country codes.
        """

        req = self.session.get(self.country_endpoint, cookies=self.cookies)
        if req.status_code == 403:
            self.cookies = self.refresh_cookie()
            req = self.session.get(self.country_endpoint, cookies=self.cookies)

        return self.session.get(self.country_endpoint, cookies = self.cookies).json()

    def get_leaders(self, country):
        """
        Retrieves the leaders for a specific country.

        Args:
            country (str): The country code (e.g., 'us', 'fr').

        Returns:
            list: A list of dictionaries containing leader information.
        """

        req = self.session.get(self.leaders_endpoint, cookies = self.cookies, params = {"country": country})

        if req.status_code == 403:
            self.cookies = self.refresh_cookie()
            req = self.session.get(self.leaders_endpoint, cookies = self.cookies, params = {"country": country})

        return req.json()
    
    def __del__(self):
        self.session.close()