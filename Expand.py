#!/usr/bin/env python

import re
import string
import urllib
import sys
import webbrowser
import android


#console.clear()

# Count arguments passed to script, if less than 2 run regex against clipboard
#numArgs = len(sys.argv)

droid = android.Android()
redirect = droid.getClipboard()

##if numArgs == 2:
##    redirect = sys.argv[1]
##elif numArgs < 2:
##    redirect = clipboard.get()
##redirect = 'http://bit.ly/15EkAY5'
# Provided by Peter Hansen on StackOverflow:
# http://stackoverflow.com/questions/1986059/grubers-url-regular-expression-in-python/1986151#1986151
pat = r'\b(([\w-]+://?|www[.])[^\s()<>]+(?:\([\w\d]+\)|([^%s\s]|/)))'
pat = pat % re.escape(string.punctuation)


match = re.findall(pat, redirect.result)

if match:
    for x in match:
##        console.show_activity()
        # Get the first match without redirects
        cleaned = urllib.urlopen(x[0]).geturl()
##        final = urllib.quote(cleaned, safe='')
##        URL = final.decode('utf8')
##        clipboard.set(cleaned)
##        console.hide_activity()
##        webbrowser.open('googlechrome-x-callback://x-callback-url/open/?url=https%3A%2F%2Fshare.flipboard.com%2Fflipit%2Fload%3Fv%3D1.0%26url%3D' + final + '&x-success=pocket://&x-source=Pocket')
        droid.setClipboard(cleaned)
#        webbrowser.open(final)
elif not match:
##    console.alert('No match found')
      print('No match found')
