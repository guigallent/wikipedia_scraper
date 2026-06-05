# Wikipedia_Scraper
[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


## 🏢 Description

The **Wikipedia Scraper** is a collaborative Python project built in pair programming mode. The goal is to design a modular and production-style data pipeline that retrieves political leaders by country from an external REST API, then enriches this data by scraping Wikipedia to extract the first biography paragraph of each leader.

During this project, the team :

- Work in a shared isolated development environment
- Apply Git Flow best practices (feature branches, pull requests, code reviews)
- Consume a REST API and modularize the client logic
- Build a web scraper using BeautifulSoup
- Clean and structure unstructured HTML data
- Integrate modules into a unified Python pipeline


## 📦 Repo structure

```
wikipedia_scraper/
├── .venv/
├── dev/
│   ├── guillermo_sandbox.ipynb
│   ├── iness_sandbox.ipynb
│   └── leaders_scraper.py
├── __init__.py
├── .gitignore
├── api_client.py
├── file_utils.py
├── html_scraper.py
├── main.py
├── output.json
├── README.md
└── requirements.txt
```

## 🛎️ Usage

1. Clone the repository to your local machine.

2. Create and activate your virtual environment:

3. Install the requirements.txt

4. Explore the API

Before coding, use the dev/ notebooks to:
- test the API endpoints
- understand cookies/session behavior
- inspect the JSON structure of leaders

5. Build the modules:

Work in separate feature branches:

- feature/api-client -> implement src/api_client.py
- feature/html-scraper -> implement src/html_scraper.py

Each module should be tested independently before integration

6. Run the main script

## ⚙️ What happens when you run it

The script automatically:

- Fetches available countries from a REST API
- Retrieves political leaders per country
- Extracts Wikipedia URLs from the API response
- Scrapes the first paragraph of each leader’s Wikipedia page
- Cleans and structures the text data
- Exports everything into a final JSON file

## 📦 Output

The final output is a structured JSON file containing:

- leaders per country (names + dates)
- cleaned first paragraph

## ⏱️ Timeline

This project took three days for completion.

## 📌 Personal Situation
This project was done as part of the AI & Data Science Bootcamp at BeCode. 

👥 Connect with us:
- [LinkedIn - Guillermo Gallent Lloria](https://www.linkedin.com/in/guillermo-gallent/)
- [LinkedIn - Iness Khatiri](https://www.linkedin.com/in/iness-khatiri-14392a258)