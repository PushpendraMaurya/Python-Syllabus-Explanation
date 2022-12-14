import requests
from bs4 import BeautifulSoup


# Making a GET request
r = requests.get('https://intake.steerhealth.io/doctor-search/aa1f8845b2eb62a957004eb491bb8ba70a')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# Getting the title tag
print(soup.title)

# Getting the name of the tag
print(soup.title.name)

# Getting the name of parent tag
# print(soup.title.parent.name)

# use the child attribute to get
# the name of the child tag
