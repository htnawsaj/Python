#!/usr/bin/env python

# Import the modules

import bitly_api
import sys
import re
import string
import android

# Define your API information

API_USER = "User Name"
API_KEY = "Api Key"

b = bitly_api.Connection(API_USER, API_KEY)

# Define how to use the program

##usage = """Usage: python shortener.py [url]
##e.g python shortener.py http://www.google.com"""

##if len(sys.argv) != 2:
##    print usage
##    sys.exit(0)

##longurl = sys.argv[1]

droid = android.Android()
clip = droid.getClipboard()



# Provided by Peter Hansen on StackOverflow:
# http://stackoverflow.com/questions/1986059/grubers-url-regular-expression-in-python/1986151#1986151
pat = r'\b(([\w-]+://?|www[.])[^\s()<>]+(?:\([\w\d]+\)|([^%s\s]|/)))'
pat = pat % re.escape(string.punctuation)


match = re.findall(pat, clip.result)

if match:
    for x in match:
        # Get the first match without redirects
        longurl = x[0]
        response = b.shorten(longurl)
        droid.setClipboard(response['url'])
elif not match:
      print('No match found')


