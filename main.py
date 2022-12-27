from bs4 import BeautifulSoup
import requests
import time

# take the required search input
print('Put some Skills That You Are Not Familiar With: ')
unfamiliar_skill = input('>')
print(f'Filtering Out {unfamiliar_skill} .....')

page_num = 0

# use requests to fetch url
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text

# create soup object to parse content
soup = BeautifulSoup(html_text, 'lxml')


# find elements containing the input key
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

page_limit = soup.find('header', class_='srp-header clearfix').div.h1.span.span.text
print(f'Found {page_limit}')

for job in jobs:
    published_date = job.find('span', class_='sim-posted').span.text
    if 'few' in published_date:
        company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
        skills = job.find('span', class_='srp-skills').text.replace(' ', '')
        more_info = job.header.h2.a['href']

        # retrieve the familiar skills only
        if unfamiliar_skill not in skills:
            print(f"company Name: {company_name.strip()}")
            print(f"Required Skills: {skills.strip()}")
            print(f"More info: {more_info}")
            print('')







