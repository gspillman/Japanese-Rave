#This script works with the yelp.com API
#You need to have an existing Yelp developer account access to run this 
#Your account key should be placed in configs/settings.config. 

import configparser
import requests
import os

#Config parser is used to read data from a config/init file
config = configparser.ConfigParser()
cwd = os.getcwd()
print(cwd)
config.read(cwd + '/configs/settings.config')
key = config['YELP']['DevKey']

url = "https://api.yelp.com/v3/businesses/search"

#Yelp's API expects your to authorize your requests in a specific manner post March 2018
headers = {'Authorization': 'bearer %s' % key}

params = {'location': 'Austin, TX', 'term': 'sushi'}
r = requests.get(url, headers=headers, params=params)

results = r.json()

for i in results['businesses']:
	if ( i['rating'] > 4.0 ):
			print(i['name'])
			print(i['rating'])
			print(i['location']['address1'])

