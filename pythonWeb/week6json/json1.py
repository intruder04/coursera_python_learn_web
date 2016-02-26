import json
import urllib
sum = 0
jsonurl = 'http://python-data.dr-chuck.net/comments_244584.json'
uh = urllib.urlopen(jsonurl)
data = json.load(uh)

# print json.dumps(data, indent=4)

for item in data["comments"]:
    global sum
    sum = sum + int(item["count"])
print sum
