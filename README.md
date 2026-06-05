# Wikipedia_Scraper
[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


## 📖 Description

The **Wikipedia Scraper** is a collaborative Python project built in pair programming mode. The goal was to **create a simple but realistic data pipeline that collects political leaders from an external REST API and enriches this data by scraping their Wikipedia pages to extract the first biography paragraph**. The final output is a JSON file containing leaders with key information to identify them, along with their first Wikipedia paragraph (in the language of the corresponding country). The project focuses on a fixed set of countries: France (FR), United States (US), Belgium (BE), Morocco (MA), and Russia (RU). 

During this project, the team: 

- worked in a virtual environment using `.venv` 
- practiced Git Flow with feature branches, pull requests, and code reviews 
- learned how to interact with a REST API using `requests` 
- built a web scraper using `BeautifulSoup` 
- extracted and cleaned unstructured HTML data 
- connected different modules into one working program 
- learned how to structure a project in a more modular and organised way 

Through this project, we also improved our understanding of: 

- teamwork and code collaboration using GitHub 
- debugging real API and scraping issues 
- handling errors and unexpected data responses 
- writing cleaner and more reusable Python code


## 📦 Repo structure

wikipedia-scraper/
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
├── dev/
│   ├── guillermo_sandbox.ipynb
│   └── iness_sandbox.ipynb
└── src/
    ├── __init__.py
    ├── api_client.py
    ├── file_utils.py
    └── html_scraper.py

📝 N.B. : The `dev/` folder was used as our training space during the project. It contains notebooks where we tested the API and explored how it works before building the main code. It is not required to run the project and can be ignored.

### 🧩 Project modules

The project is organized into three main modules located in the `src/` folder:

- `api_client.py` handles requests to the Country Leaders API, retrieves countries and leaders, and refreshes cookies when needed.

- `file_utils.py` contains helper function used to extract Wikipedia URLs and organize leader information before scraping.

- `html_scraper.py` fetches Wikipedia pages, extracts and cleans the first biography paragraph, and saves the results to a JSON file.

This modular structure makes the code easier to maintain and update.


## 📌 Usage

1. Clone the repository to your local machine

2. Create and activate your virtual environment

3. Install the libraries listed in the `requirements.txt` file

4. Run the main script


### ⚙️ What happens when you run it

When the script starts, it:

- connects to the Country Leaders API
- retrieves the list of available country codes
- prompts the user to select a country
- fetches the leaders for the selected country
- extracts the Wikipedia URL of each leader
- scrapes the first biography paragraph from each Wikipedia page
- cleans the extracted text to remove unwanted elements
- displays the results in the terminal
- saves the collected data into a JSON file

### 📦 Output

The script generates a `leaders.json` file containing:

- the names of the leaders
- their mandate dates
- the first paragraph of their Wikipedia biography
- information written in the language of the selected country

Each leader is stored as a separate entry in the JSON file.


## 🔧 Possible improvements 

Even if this project already works as a small data pipeline, there are a few ways it could be improved in the future.

### 1. Custom output file name 

Right now, the script saves the result as a fixed JSON file. 

A possible improvement would be to let the user choose the output file name directly when running the script. This would make the tool more flexible and reusable. 

### 2. Improve user interaction for multiple runs

Instead of stopping the program after one run, an improvement would be to let the user choose another country directly in the terminal.

After finishing, the program could ask:

> “Do you want to run the program again for another country?”

This would allow the user to use the script several times without restarting it manually.

It could also be combined with the first improvement by letting the user choose a different output file name each time, so each run saves a new JSON file.

### 3. Improve text cleaning 

The current cleaning process removes most unwanted characters, but some elements still remain, such as: 
- pronunciation guides (e.g. `/ʒak ʃiʁak/`) 
- unwanted words like “Écouter” 
- some leftover formatting from Wikipedia 

A better cleaning function could improve the final output by making the text more readable and consistent.

## ⏱️ Timeline

This project took three days for completion.

## 📌 Personal Situation
This project was done as part of the AI & Data Science Bootcamp at BeCode. 

👥 Connect with us:
- [LinkedIn - Guillermo Gallent Lloria](https://www.linkedin.com/in/guillermo-gallent/)
- [LinkedIn - Iness Khatiri](https://www.linkedin.com/in/iness-khatiri-14392a258)