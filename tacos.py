import requests
from bs4 import BeautifulSoup

url = "https://www.yelp.com/search?find_desc=tacos&find_loc=Austin%2C+TX&ns=1"

taco_request = requests.get(url)

if not taco_request.status_code == 200:
  print("Uh oh - we didn't get a 200 OK from the URL")

taco_soup = BeautifulSoup(taco_request.text, 'html.parser')

print taco_soup.find_all("a")

print taco_soup.find_all("id")