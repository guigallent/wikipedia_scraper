import requests

class CountryLeadersAPI:

    def __init__(self):
        self.base_url = "https://country-leaders.onrender.com/"
        self.country_endpoint = self.base_url + "countries"
        self.leaders_endpoint = self.base_url + "leaders"
        self.cookies_endpoint = self.base_url + "cookie"
        self.session = requests.Session()
        self.cookies = self.refresh_cookie()
        
    def refresh_cookie(self):
        return requests.get(self.cookies_endpoint).cookies
        
    def get_countries(self):
        return requests.get(self.country_endpoint, cookies = self.cookies).json()

    def get_leaders(self, country):
        req = self.session.get(self.leaders_endpoint, cookies = self.cookies, params = {"country": country})

        if req.status_code == 403:
            self.cookies = self.refresh_cookie()
            req = self.session.get(self.leaders_endpoint, cookies = self.cookies, params = {"country": country})

        print(req.json())
    
    def __del__(self):
        self.session.close()