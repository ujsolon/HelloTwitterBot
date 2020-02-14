## Import our Twitter credentials from init.py
import os
import tweepy
import credentials
from bilang import *

## change the current directory to the directory where the running script file (.py) exists.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

## Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
auth.set_access_token(credentials.access_token, credentials.access_token_secret)
api = tweepy.API(auth)

## Open text file test1.txt (or your chosen file) for reading
my_file = open('1000filipino.txt', 'r')

## Read lines one by one from my_file and assign to file_lines variable
file_lines = my_file.readlines()
file_lines = file_lines[curr_line]

##do the tweet here; Hello text is hardcoded
print(file_lines)
api.update_status("Hello " +file_lines)

## Close file
my_file.close()

with open("bilang.py", "w") as file:
    s = "curr_line = " + str(curr_line+1)
    file.write(s)

file.close()