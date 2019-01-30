#This script works with the yelp.com API
#You need to have an existing Yelp developer account access to run this 
#Your account key should be placed in configs/settings.config. 

import configparser
import requests
import os
import twitter

##Fun with Yelp's API

#Config parser is used to read data from a config/init file
config = configparser.ConfigParser()
cwd = os.getcwd()
config.read(cwd + '/configs/settings.config')
ykey = config['YELP']['DevKey']
tkey = config['TWITTER']['DevKey']
tskey = config['TWITTER']['SecretKey']
taccess = config['TWITTER']['AccessToken']
tsaccess = config['TWITTER']['SecretToken']

url = "https://api.yelp.com/v3/businesses/search"

#Yelp's API expects your to authorize your requests in a specific manner post March 2018
headers = {'Authorization': 'bearer %s' % ykey}

params = {'location': 'Austin, TX', 'term': 'sushi'}
r = requests.get(url, headers=headers, params=params)

results = r.json()

for i in results['businesses']:
	if ( i['rating'] > 4.0 ):
			print(i['name'])
			print(i['rating'])
			print(i['location']['address1'])

##Fun with Twitter's API

tapi = twitter.Api(consumer_key = tkey, consumer_secret = tskey, 
					access_token_key = taccess, access_token_secret = tsaccess)
try:
	tapi.VerifyCredentials
except: 
	print('Sorry, could not authenticate you with Twitter')
else:
	print(tapi.GetFollowers())
	print(tapi.GetFriends())

#tapi.PostUpdates(status="This is a test. Today's lucky number is 188")

screen_name = 'Reindeere Flotilla'

try:
	tapi.UsersLookup(screen_name=screen_name)
except:
	print('User not found')
else:
	print('User, ' + screen_name + ' appears to be registered with Twitter')
