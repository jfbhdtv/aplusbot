import os
import time
from markovbot import MarkovBot

#####
# INITIALIZE

# Initialize a MarkovBot instance
tweetbot = MarkovBot()

# Get the current directory's path
dirname = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the source
source = os.path.join(dirname, u'text.txt')
# Make your bot read the book
tweetbot.read(source)
print('I am here') 			

#####
# TWITTER

# The MarkovBot uses @sixohsix's Python Twitter Tools,
# which is a Python wrapper for the Twitter API. Find it on
# GitHub:https://github.com/sixohsix/twitter

#ALL YOUR SECRET STUFF


cons_key='xFDPDH69ZepYLRVkOqjQrtECN'
cons_secret='P1EP0zcYWZgibhQYJ9qa3dK6r7WWSHBJnT9SVejkwFMkeoFdak'
access_token='839635667852398597-2MRejOldAhYNdUqXDykKANnql9Tc65z'
access_token_secret='OOiKoYxvwzh8dNtkNszcfQtkLaSF29vyMFBTOVWjHpll6'

# Log in to Twitter
tweetbot.twitter_login(cons_key, cons_secret, access_token, access_token_secret)

# Start tweeting
tweetbot.twitter_tweeting_start(days=0, hours=1, minutes=0, keywords=None, prefix=None, suffix='#aplusbot #ITCert')

time.sleep(86400)
