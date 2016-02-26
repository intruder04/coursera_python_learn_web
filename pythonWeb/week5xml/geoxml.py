import urllib
import xml.etree.ElementTree as ET
sum = 0

url = 'http://python-data.dr-chuck.net/comments_244580.xml'
uh = urllib.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)
counts = tree.findall('.//count')
for count in counts:
    global sum
    sum = sum + int(count.text)
print sum
