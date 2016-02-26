import re
totalsum = 0
hand = open('text2.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[0-9]+',line)
    for number in x:
        totalsum = totalsum + int(number)
print totalsum
