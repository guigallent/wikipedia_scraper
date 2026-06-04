import requests
import re
from bs4 import BeautifulSoup

class WikipediaScraper:
    #création du squelette
    def __init__(self,session):
        self.session = session
    
    #téléchargement des documents HTML
    def fetch_html(self, url:str):
        #safely requests raw HTML text
        try:
            req = self.session.get(url)

            print(f"Status code : {req.status_code}")
        
            #robust handling to deal with 404s, 500s or connection drops
            if req.status_code == 404 or req.status_code == 500:
                return "Error is found"
        
            return req.text

        #connection drops
        except Exception:
            return "Connection drops"
    
