#JavaScript Image Scraper

import requests
import os
from bs4 import BeautifulSoup
from selenium import webdriver
import shutil
import time

#This URL is to a JavaScript based gallery of historical rave fliers from Tokyo, Japan
url = "http://www.ravepreservationproject.com/gallery/index.php#Japan/Tokyo"
base_img_url = "http://www.ravepreservationproject.com/gallery/"
js_script = "return document.documentElement.outerHTML"
image_directory = "images"

#Making a web request, taking the response and placing it into a bs4 object
web_req = requests.get(url)
web_soup = BeautifulSoup(web_req.text, 'html.parser')

#Note - this will only print out a handful of images within the header/footer of the page
#It can't grock anything from the image gallery because of the JS nature of the gallery. 
print(web_soup.find_all("img"))

#Oooh boy - we need Webdriver!
#Make sure you pip install selenium
#Next, make sure you get the latest version of Chromedirver (try here: https://sites.google.com/a/chromium.org/chromedriver/downloads)
#You'll need to put the driver into your /usr/local/bin directory or PATH

driver = webdriver.Chrome()
driver.get(url)

#Not going to implement a wait for... method for this script so we'll just sleep for 10 seconds.
#This is to accomodate for the time it might take for the image gallery to load. 

time.sleep(5)

html = driver.execute_script(js_script)

wd_soup = BeautifulSoup(html, 'html.parser')

print("Looks like we found " + str(len(wd_soup.findAll("img"))) + " images on the page.")

images = []

for i in wd_soup.findAll("img"):
	src = i["src"]
	if ".jpg" not in src:
		continue
	else:
		images.append(src)

current_path = os.getcwd()
for each in images:
	file_name = os.path.basename(each)
	img_r = requests.get(base_img_url + each)
	new_path = os.path.join(current_path, image_directory, file_name)
	
	#wb option is for write in binary - creates new file or overwrites existing file. 
	with open(new_path, "wb") as output_file:
		shutil.copyfileobj(img_r.raw, output_file)
	del img_r

driver.close()
