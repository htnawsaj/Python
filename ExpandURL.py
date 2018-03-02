#-------------------------------------------------------------------------------
# This script is modified version of the one available at 
# http://www.macstories.net/tutorials/resolve-short-urls-with-pythonista-on-ios/
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import re
import string
import urllib
import sys
import webbrowser
import android

droid = android.Android()

redirect = droid.getClipboard()

# Provided by Peter Hansen on StackOverflow:
# http://stackoverflow.com/questions/1986059/grubers-url-regular-expression-in-python/1986151#1986151
pat = r'\b(([\w-]+://?|www[.])[^\s()<>]+(?:\([\w\d]+\)|([^%s\s]|/)))'
pat = pat % re.escape(string.punctuation)


match = re.findall(pat, redirect.result)

if match:
    for x in match:
        # Get the first match without redirects
        cleaned = urllib.urlopen(x[0]).geturl()
        droid.setClipboard(cleaned)

elif not match:
      print('No match found')