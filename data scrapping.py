'''import requests
from bs4 import BeautifulSoup
# # Making a GET request
r = requests.get('https://intake.steerhealth.io/doctor-search/aa1f8845b2eb62a957004eb491bb8ba70a')

# # Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find('div', class_='entry-content')
content = s.find_all('p')

print(content)'''

# import requests
# from bs4 import BeautifulSoup


# # Making a GET request
# r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# # check status code for response received
# # success code - 200
# print(r)

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())

import requests
from bs4 import BeautifulSoup as bs
import csv

URL = 'https://intake.steerhealth.io/doctor-search/aa1f8845b2eb62a957004eb491bb8ba70a'

soup = bs(req.text, 'html.parser')

titles = soup.find_all('div', attrs={'class', 'head'})
titles_list = []

count = 1
for title in titles:
	d = {}
	d['Title Number'] = f'Title {count}'
	d['Title Name'] = title.text
	count += 1
	titles_list.append(d)

filename = 'titles.csv'
with open(filename, 'w', newline='') as f:
	w = csv.DictWriter(f,['Title Number','Title Name'])
	w.writeheader()
	
	w.writerows(titles_list)
