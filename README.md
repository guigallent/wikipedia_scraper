# Wikipedia_Scraper
[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


## 📖 Description

The **Wikipedia Scraper** is a collaborative Python project built in pair programming mode. The goal was to **create a simple but realistic data pipeline that collects political leaders from an external REST API and enriches this data by scraping their Wikipedia pages to extract the first biography paragraph**. The final output is a JSON file containing political leaders with key information to identify them, along with their first Wikipedia paragraph (in the language of the corresponding country). The project focuses on a fixed set of countries: France (FR), United States (US), Belgium (BE), Morocco (MA), and Russia (RU). 

During this project, the team: 
- Worked in a shared isolated development environment using `venv` 
- Practiced Git Flow with feature branches, pull requests, and code reviews 
- Learned how to interact with a REST API using `requests` 
- Built a web scraper using `BeautifulSoup` 
- Extracted and cleaned unstructured HTML data 
- Connected different modules into one working program 
- Learned how to structure a project in a more modular and organised way 

Through this project, we also improved our understanding of: 

- teamwork and code collaboration using GitHub 
- debugging real API and scraping issues 
- handling errors and unexpected data responses 
- writing cleaner and more reusable Python code


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

1. Clone the repository to your local machine

2. Create and activate your virtual environment

3. Install the requirements

4. Explore the API (optional)

Before coding, use the dev/ notebooks to:

- test the API endpoints
- understand cookies/session behavior
- inspect the JSON structure of leaders

6. Run the main script

## 🧩 Project modules

The project is organized into three main modules (in src folder meme utils ?):

- `api_client.py` handles requests to the Country Leaders API, retrieves countries and leaders, and refreshes cookies when needed.

- `file_utils.py` contains helper functions used to extract Wikipedia URLs and organize leader information before scraping.

- `html_scraper.py` fetches Wikipedia pages, extracts and cleans the first biography paragraph, and saves the results to a JSON file.


This modular structure makes the code easier to maintain and update.

## ⚙️ What happens when you run it

When the script starts, it:

- Connects to the Country Leaders API
- Retrieves the list of available country codes
- Prompts the user to select a country
- Fetches the political leaders for the selected country
- Extracts the Wikipedia URL of each leader
- Scrapes the first biography paragraph from each Wikipedia page
- Cleans the extracted text to remove unwanted elements
- Displays the results in the terminal
- Saves the collected data into a JSON file

## 📦 Output

The script generates a `leaders.json` file containing:

- the names of the political leaders
- their mandate dates
- the first paragraph of their Wikipedia biography
- information written in the language of the selected country

Each leader is stored as a separate entry in the JSON file.

## 🔧 Possible improvements 

Even if this project already works as a small data pipeline, there are a few ways it could be improved in the future.

### 1. Custom output file name 

Right now, the script saves the result as a fixed JSON file. 

A possible improvement would be to let the user choose the output file name directly when running the script. This would make the tool more flexible and reusable. 

### 2. Better user interaction on errors 

Sometimes Wikipedia pages may fail to load or return incomplete data. An improvement would be to add a simple user prompt when this happens, for example: 

> “Something went wrong. Do you want to retry or stop the script?” 

This would allow the user to decide whether to: 
- rerun the script automatically 
- or stop and check the issue manually 

It would make the script more robust and user-friendly. 

### 3. Improve text cleaning 

The current cleaning process removes most unwanted characters, but some elements still remain, such as: 
- pronunciation guides (e.g. `/ʒak ʃiʁak/`) - unwanted words like “Écouter” 
- some leftover formatting from Wikipedia 

A better cleaning function could improve the final output by making the text more readable and consistent.

## ⏱️ Timeline

This project took three days for completion.

## 📌 Personal Situation
This project was done as part of the AI & Data Science Bootcamp at BeCode. 

👥 Connect with us:
- [LinkedIn - Guillermo Gallent Lloria](https://www.linkedin.com/in/guillermo-gallent/)
- [LinkedIn - Iness Khatiri](https://www.linkedin.com/in/iness-khatiri-14392a258)