# ContactCongressBE
Backend for contact information of Government Officials

## Features
- Scrapes congressional information for contact purposes from https://contactrepresentatives.org/ and puts them into a sqlite db file.

## Data
For those who do not want to deal with code, congress.db is provided. Can be converted to excel or csv if needed.

## How to Use
1. Make sure to have python and edge installed on your machine. If using a different web browser/driver, make sure to modify the code accordingly.

[Python Installation](https://www.python.org/downloads/)

[Edge Installation](https://www.microsoft.com/en-us/edge/download?form=MM1475)

2. cd into the project directory (wherever you saved it on your machine + "cd ContactCongressBE")

3. Create a virtual environment with "python -m venv venv"
   
5. Activate environment (should be "venv\Scripts\activate" on windows OR "source venv/bin/activate" on Mac assuming the environment is named venv)
   
7. Install the requirements with "pip install -r requirements.txt".

8. Run the program with "python contactAPI.py". This will run a flask server.
   
10. Get the completed db by querying the api like "curl http://127.0.0.1:5000/refresh" (mac) or "(Invoke-WebRequest "http://127.0.0.1:5000/refresh")" (windows)

11. Either convert the db file to a spreadsheet/csv, or curl the api like "curl http://127.0.0.1:5000/lookup?name=joe&party=dem" (mac) or "(Invoke-WebRequest "http://127.0.0.1:5000/candidates").Content" (windows)


## Disclaimer
Please note that web scraping may be subject to legal restrictions depending on the website's terms of service. It is recommended to review and comply with the website's policies before using this scraper. 

## License
This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/). Feel free to use, modify, and distribute this tool according to the terms of the license.

For any questions or feedback, please contact [flatwhitecoffey@gmail.com](mailto:flatwhitecoffey@gmail.com). Thank you for using ContactCongress!
