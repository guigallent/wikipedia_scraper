from api_client import CountryLeadersAPI
from html_scraper import WikipediaScraper



country_leaders = CountryLeadersAPI()
active_countries = country_leaders.get_countries()
leaders = country_leaders.get_leaders("fr")

scraper = WikipediaScraper()

print(leaders)

for leader in leaders:
    print(leader['wikipedia_url'])




