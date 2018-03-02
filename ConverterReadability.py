# firefoxize-starred-items.py
#
# Reads a Google "Reader JSON" file exported from Google Reader and
# outputs an HTML file suitable for importing into Firefox's
# bookmarks menu. This rescues you if you have been using Google
# Reader Starred Items as a bookmark file for feeds.
#
# See http://googlereader.blogspot.com/2011/10/new-in-reader-fresh-design-and-google.html
# and, when logged in, http://www.google.com/reader/settings?display=import

#original script from http://innocentpastimes.blogspot.in/2011/11/converting-google-reader-starred-items.html

import json, time, codecs

InputFile = 'C:\Personal\Python\Readability.json'  #download this
OutputFile = 'C:\Personal\Python\Readability_new.html'  #import this

with codecs.open(InputFile, 'r', encoding='utf-8') as f:
    ReadabilityItems = json.load(f)

FeedURLs = {}
FeedItems = {}

for item in ReadabilityItems:
    feedTitle = 'Readability'
    feedUrl = item['article__url']
    itemDate =  item['date_added']
    itemTitle = item['article__title'].split('\n')[0]
    itemURL = feedUrl
    FeedURLs[feedTitle] = feedUrl
    feedItems = FeedItems.setdefault(feedTitle, [])
    feedItems.append((itemTitle, itemURL, itemDate))

with codecs.open(OutputFile, 'w', encoding='utf-8') as b:
    b.write('''<!DOCTYPE html>
   <html>
        <head>
                <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
                <title>Instapaper: Export</title>
        </head>\n''')
    b.write('<body>\n\n')

    for feedTitle, feedURL in FeedURLs.items():
        b.write('<h1>%s</h1>\n' % feedTitle)
        b.write('<ol>\n')
        for (title, url, date) in FeedItems[feedTitle]:
            b.write('<li><a HREF="%s">%s</a></li>\n' % (url,title))
        b.write('</ol>\n\n')
    b.write('</body>\n\n\n')
    b.write('</html>\n')