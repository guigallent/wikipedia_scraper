import requests
import json
import re
from bs4 import BeautifulSoup

def get_first_paragraph(wikipedia_url, session): #modifier le nombre d'argument
    
    headers = {"User-Agent": "Mozilla/5.0"}
    wiki_text = session.get(wikipedia_url, headers = headers) #modification requests change into session
    soup = BeautifulSoup(wiki_text.text, 'html.parser')

    for p in soup.find_all("p"):
        if p.find("b"):
            first_paragraph = p.get_text()
            first_paragraph = re.sub(r'\[[^\]]*\]', "", first_paragraph) # removes [references]
            first_paragraph = re.sub(r'\([^)]*(Écouter|listen)[^)]*\)', "", first_paragraph)  # removes phonetic pronunciations
            first_paragraph = re.sub(r'ⓘ', '', first_paragraph)  # removes audio icons
            first_paragraph = re.sub(r'\s{2,}', " ", first_paragraph)  # removes double spaces
            first_paragraph = re.sub(r'\s,', ",", first_paragraph)  # fixes " ,"
            return first_paragraph   

def get_leaders():

    root_url = "https://country-leaders.onrender.com"
    cookie_url = root_url + "/cookie"
    countries_url = root_url + "/countries"
    leaders_url = root_url + "/leaders"

    cookies = requests.get(cookie_url).cookies
    countries = requests.get(countries_url, cookies=cookies).json()
    
    session = requests.Session() #session unique pour wikipédia

    data = {}

    for country in countries:

        req = requests.get(leaders_url, cookies=cookies, params={"country": country})

        if req.status_code == 403:
            cookies = requests.get(cookie_url).cookies
            req = requests.get(leaders_url, cookies=cookies, params={"country": country})

        leaders = req.json()
        country_data = {}

        for leader in leaders:
            url = leader["wikipedia_url"]
            paragraph = get_first_paragraph(url,session) #session utilisée

            name = f"{leader['first_name']} {leader['last_name']}"
            dates = f"({leader.get('start_mandate', 'unknown')} - {leader.get('end_mandate', 'present')})"

            country_data[f"{name} {dates}"] = paragraph

        data[country] = country_data
    
    return data
    

def save(leaders_per_country): 
    with open("leaders.json", "w") as f: 
        json.dump(leaders_per_country, f, indent=4)

if __name__ == "__main__":
    leaders_per_country = get_leaders()
    save(leaders_per_country)
    print('Script complete!')