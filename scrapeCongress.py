from bs4 import BeautifulSoup as soup
import requests
from pprint import pprint
from util import cleanText
from congressprofile import Profile
import pandas as pd
from time import sleep
from tqdm import tqdm

class Scraper():
    def __init__(self):
        pass
    
    def refreshDB(self):
        HEADER = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}
        URL = "https://contactrepresentatives.org/"

        response = requests.get(URL, headers=HEADER)
        page_html = response.text
        page_soup = soup(page_html, "lxml")
        links = page_soup.find_all('a', attrs={'class': lambda e: e.startswith('text-') if e else False})
        profiles = []
        for i in tqdm(range(len(links))):
            link = links[i]
            response = requests.get(link['href'], headers=HEADER)
            page_html = response.text
            pageSoup = soup(page_html, "lxml")
            table = pageSoup.find(lambda tag: tag.name=='table')
            if table is None:
                continue
            rows = table.findAll(lambda tag: tag.name=='tr')
            name = None
            state = None
            party = None
            birthday = None
            entered = None
            address = None
            number = None
            email = None
            website = None
            twitter = None
            branch = link.parent.parent.parent.parent.get('id')
            if branch == None:
                branch = 'representative'
            for row in rows:
                pre, post = cleanText(row.text).split(':')
                href_tags = row.find('a')
                if 'name' in pre.lower():
                    name = post
                    if href_tags:
                        name = href_tags.get('href')
                elif 'state' in pre.lower():
                    state = post
                    if href_tags:
                        state = href_tags.get('href')
                elif 'party' in pre.lower():
                    party = post
                    if href_tags:
                        party = href_tags.get('href')
                elif 'birth date' in pre.lower():
                    birthday = post
                    if href_tags:
                        birthday = href_tags.get('href')
                elif 'entered' in pre.lower():
                    entered = post
                    if href_tags:
                        entered = href_tags.get('href')
                elif 'address' in pre.lower():
                    address = post
                    if href_tags:
                        address = href_tags.get('href')
                elif 'phone number' in pre.lower():
                    number = post
                    if href_tags:
                        number = href_tags.get('href')
                elif 'email' in pre.lower():
                    email = post
                    if href_tags:
                        email = href_tags.get('href')
                elif 'website' in pre.lower():
                    website = post
                    if href_tags:
                        website = href_tags.get('href')
                elif 'twitter' in pre.lower():
                    twitter = post
                    if href_tags:
                        twitter = href_tags.get('href')
            profiles.append(
                Profile(
                    name=name,
                    state=state,
                    party=party,
                    birthday=birthday,
                    entered=entered,
                    address=address,
                    number=number,
                    email=email,
                    website=website,
                    twitter=twitter,
                    branch=branch
                )
            )
            sleep(1)

        return pd.DataFrame([x.as_dict() for x in profiles])

