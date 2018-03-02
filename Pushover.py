

#!/usr/bin/env python

import httplib, urllib
import sys


def sendmessage():
    conn = httplib.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
      urllib.urlencode({
        "token": "Your App Api goes here",
        "user": "Your User Key goes here",
        "message": str(sys.argv[1]),
        "title": str(sys.argv[2]),
        "url": str(sys.argv[3])
      }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()
    print "Message has been Sent"



def main():
    if len(sys.argv) != 4:
        print("Usage: PushOver.py 'message' 'title' 'url' \n")
    else:
		sendmessage()

if __name__ == '__main__':
    main()