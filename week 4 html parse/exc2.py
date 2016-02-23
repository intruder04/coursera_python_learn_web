import urllib
from BeautifulSoup import *
url = raw_input('Enter - ')
pos = raw_input('Enter pos: ')
repeat = raw_input('Enter repeat: ')
repCount = 0

def geturl(Url, Pos):
        counter = 0
        html = urllib.urlopen(Url).read()
        soup = BeautifulSoup(html)
        tags = soup('a')
        for tag in tags:
            counter = counter + 1
            if counter == int(Pos):
                # repeat = repeat + 1
                print tag.get('href', None)
                global url
                url = tag.get('href', None)

while repCount < int(repeat):
    geturl(url, pos)
    repCount = repCount + 1
