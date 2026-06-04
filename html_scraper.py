import requests
import re
from bs4 import BeautifulSoup
import json

class WikipediaScraper:
    #création du squelette
    def __init__(self,session):
        self.session = session
        self.headers = {"User-Agent": "Mozilla/5.0"}
    
    #téléchargement des documents HTML
    def fetch_html(self, url:str):
        
        #safely requests raw HTML text
        try:
            req = self.session.get(url, headers = self.headers)

            print(f"Status code : {req.status_code}")
        
            #robust handling to deal with 404s, 500s or connection drops
            if req.status_code == 404 or req.status_code == 500:
                return "Error is found"
        
            return req.text

        #connection drops
        except Exception:
            return "Connection drops"
    
    def get_first_paragraph(self, html:str):
        #Parses raw HTML with BeautifulSoup, finds the first true biographical narrative paragraph (), and returns it.
        soup = BeautifulSoup(html, 'html.parser')
        
        for p in soup.find_all("p"):
            if p.find("b"):
                first_paragraph = p.get_text()                
                return first_paragraph
        return ""
    
    def clean_text(self, text:str):
    #A cleaning utility method to strip out unwanted characters, whitespace, or Wikipedia citation brackets (e.g., [1], [citation needed]).

        text = re.sub(r'\[[^\]]*\]', "", text) # removes [references]
        text = re.sub(r'\([^)]*(Écouter|listen)[^)]*\)', "", text)  # removes phonetic pronunciations
        text = re.sub(r'ⓘ', '', text)  # removes audio icons
        text = re.sub(r'\s{2,}', " ", text)  # removes double spaces
        text = re.sub(r'\s,', ",", text)  # fixes " ,"

        return text.strip()

    def to_json_file(self, filepath: str, data) -> None:
    # stores the data structure into a JSON file
        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)

#testing the code
if __name__ == "__main__":
    session = requests.Session()
    scraper = WikipediaScraper(session)

    url = "https://fr.wikipedia.org/wiki/Nicolas_Sarkozy"

    html = scraper.fetch_html(url)

    paragraph = scraper.get_first_paragraph(html)

    clean = scraper.clean_text(paragraph)

    data = {
        "url": url,
        "paragraph": clean
    }

    scraper.to_json_file("output.json", data)

    print("JSON file created!")