from api_client import CountryLeadersAPI
from html_scraper import WikipediaScraper
from file_utils import get_urls

def main():
    """
    This function will interact with the user to obtain a list of leaders from the country indicated by them.
    This program uses the API https://country-leaders.onrender.com/ to fetch the information.
    The countries included are retrieved from the API based on availability.
    The leaders' names and dates, as well as an extract of the first paragraph of their Wikipedia page, will then be stored in a JSON file.
    """

    country_leaders = CountryLeadersAPI()
    scraper = WikipediaScraper(country_leaders.session)

    active_countries = country_leaders.get_countries()

    print(f"Available countries: {active_countries}")
    country = input("Enter a country code or write \"exit\" to finish the execution: ")

    while country not in active_countries:
        print(f"Country '{country}' not available. Please choose from: {active_countries} or write \"exit\" to finish the execution:")
        country = input("Enter a country code: ")
        if country.lower() == "exit":
            print("Exiting program.")
            exit()

    leaders = country_leaders.get_leaders(country)
    urls = get_urls(leaders)

    results = {}
    for name_dates, url in urls.items():
        html = scraper.fetch_html(url)
        paragraph = scraper.get_first_paragraph(html)
        clean = scraper.clean_text(paragraph)
        results[name_dates] = clean
        print(f"\n{name_dates}")
        print(clean)

    scraper.to_json_file("leaders.json", results)
    print("\nJSON file created!")

if __name__ == "__main__":
    main()