import requests; import re; from bs4 import BeautifulSoup; import json; import time

class WikipediaScraper:

    def __init__(self,session):

        """
        Initializes the scraper with an HTTP session

        Attributes :
            session : session object used to send HTTP requests
            headers (dict) : default request headers for Wikipedia requests
        """

        self.session = session
        self.headers = {"User-Agent": "Mozilla/5.0"}

        print("Scarper initialized")
    



    def fetch_html(self, url:str):
        """
        Retrieves the raw HTML content from the given URL and returns it,
        while handling common HTTP errors (404, 500) and connection-related exceptions

        Args:
            url (str): URL of the Wikipedia page to fetch
        
        Returns:
            str: The page HTML content if the request succeds, otherwise an error message
        
        """

        print("Fetching page")
        
        try:
            #Send an HTTP GET request to the specified url
            req = self.session.get(url, headers = self.headers)

            print(f"Status code : {req.status_code}")

            #403 = blocked by website 
            #can happen if we send to many requests in a short time (anti-bot protection)
            #so we wait a bit and try again
            if req.status_code == 403:
                print("403 detected, waiting 5 seconds...")
                time.sleep(5)
                req = self.session.get(url, headers=self.headers) 
            

            #Handle common server and page-not-found errors
            if req.status_code == 404 or req.status_code == 500:
                print("Error : page not found or server error")
                return "Error is found"


            #Return the HTML content of the response
            print("HTML received")
            return req.text


        #Handle connection failures and unexpected request errors
        except Exception:
            print("Connection error")
            return "Connection drops"
         



    def get_first_paragraph(self, html:str):
        
        """
        Parses the raw HTML using BeautifulSoup, 
        extracts the first biographical paragraph 
        (usually the first <p> containing bold text),
        and returns it as normal text without HTML tags.
        
        Args:

            html (str): Raw HTML content of a Wikipedia page.

        Returns:

            str: The first biographical paragraph as text, or an empty string if not found.
        """
        print("Parsing HTML")

        #parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')

        #loop through all paragraph elements <p>
        for p in soup.find_all("p"):

            #check if the paragraph contains bold text
            if p.find("b"):

                #extract only the text (remove HTML tags)
                first_paragraph = p.get_text()

                #return the first valid paragraph found                
                return first_paragraph
            
        #return empty str if no <p> found
        #this avoids returning None and make the result always a str    
        print("No paragraph found")
        return ""
    



    def clean_text(self, text:str):
        """
        Cleans a text str by removing unwanted characters, whitespace or Wikipedia citation brackets
        
        Args:
            text (str): raw text extracted from Wikipedia.

        Returns:
            str: cleaned text with unnecessary elements removed.
        
        """
        print("Cleaning text")

        #remove citation brackets like [1], [citation], etc.
        text = re.sub(r'\[[^\]]*\]', "", text) 
        
        #remove pronunciation or audio-related content like "Ecouter" or "Listen"
        #text = re.sub(r'\([^)]*(Écouter|listen)[^)]*\)', "", text)
        text = re.sub(r"(/[^)]/\s[^)])", "", text)  
        
        #remove audio icon symbols
        text = re.sub(r'ⓘ', '', text)  
        
        #replace double spaces with a single space
        text = re.sub(r'\s{2,}', " ", text) 
        
        #fix spacing before commas
        text = re.sub(r'\s,', ",", text)  # fixes " ,"

        #remove extra spaces at the start and end
        print("Cleaning done")
        return text.strip()
        



    def to_json_file(self, filepath: str, data) -> None:
        """
        Stores the scraped data into a JSON file with proper UTF-8 encoding.

        Args:
            filepath (str): Path of the JSON file to create or overwrite.
            data (dict): Data structure to save into the file.

        Returns:
            None
        """
        
        print("Saving file")

        #open the file in write mode with UTF-8 encoding so accents (é, è,ç, etc.) are saved correctly
        with open(filepath, "w", encoding="utf-8") as f:

            #save data in JSON format
            #ensure_ascii = False keeps real accents instead of \u codes
            json.dump(data, f, indent=4, ensure_ascii=False) 

        print("File saved!")