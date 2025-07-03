
import requests
from bs4 import BeautifulSoup

url = input("Enter the URL: ")
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

title = soup.title.string
print(f"Title of the webpage: {title}")
    