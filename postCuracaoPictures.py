'''
Robert Holahan
11 February 2018
TwitterBot
Written in Python 2.7.11 

This python script will post images from a designated folder on the local system
to a Twitter account in an automated fashion.

For security reasons, your will have to provide the following information
for your Twitter account.

Consumer Key, Consumer Secret, Access Token, and Access Token Secret.
and assign them to the proper variable.

This script requires that you have the tweepy library installed on your system.
'''  

#an open source wrapper for the Twitter API.
import tweepy as tp

#native python libraries
import time
import os

#strings required to login to your Twitter app account.
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''


#Twitter login.
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_secret)
api = tp.API(auth)

#point to the directory where the desired pictures meet,
#this arg can be changed to point to alternate folder.
os.chdir('images')

#Loop through images contained in the designated folder and post to Twitter account at 3 second intervals.
x = 0
for image in os.listdir('.'):
	api.update_with_media(image)
	time.sleep(3)
	x += 1
	
print(str(x) + ' Images were posted to Twitter!')