import requests
from bs4 import BeautifulSoup

j = 'python developer'.strip().title()
items = j.split(' ')

job = 'python developer'.replace('+',' ').strip()

location ='Bengaluru'.replace('+',' ').strip()


url = 'https://www.indeed.co.in/jobs?q=python+developer&sort=date'

url = 'https://www.indeed.co.in/jobs?q='+job+'&l='+location+'&sort=date'


res = requests.get(url).content

soup = BeautifulSoup(res,'html.parser')

data = soup.find_all('div',class_='jobsearch-SerpJobCard')

for i in data:
    title = i.find('h2',class_='title')
    if items[0] in title.text.strip():
        link = title.find('a')

        sal = i.find('span',class_='salaryText')
        day = i.find('span',class_='date')
        company = i.find('span',class_='company')
        summary = i.find('div',class_='summary')

        print('\n',title.text)
        print(sal)
        print(day.text)
        print(company.text)
        print(summary.text)
        print('https://www.indeed.co.in'+link['href'])












