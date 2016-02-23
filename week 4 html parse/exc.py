import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

sum = 0

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    print 'Contents:',tag.contents[0]
    sum = sum + int(tag.contents[0])
print(sum)
