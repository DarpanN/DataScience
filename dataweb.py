# import pandas as pd
# df1 = pd.read_csv('file.csv')
# df = pd.read_csv('source1.csv')
# print(df1)
# print(df)


# import json

# # Load the JSON file
# with open('file.json') as json_file:
#     data = json.load(json_file)



# import xml.etree.ElementTree as ET

# # Load the XML file
# tree = ET.parse('file.xml')
# root = tree.getroot()
# print(root)


# import requests
# from bs4 import BeautifulSoup

# url = "https://www.facebook.com"
# page = requests.get(url)
# soup = BeautifulSoup(page.content, "html.parser")
# print(soup.prettify())




# import requests

# url = "https://facebook.com"
# response = requests.get(url)
# webContent = response.text
# print(webContent)



import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = 'https://facebook.com'
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the links on the page
links = soup.find_all('a')

# Extract the text of each link
for link in links:
    print(link.text)






