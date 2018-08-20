import requests
import re
def listHyperlinks(f):
    hyperlinks = []
    for line in f:
        print('f')
        line = line.rstrip()
        line = line.split(' ')
        for l in line:
            if 'http' in l:
                low = l.find('"')
                high = l.rfind('"')
                l = l[low+1:high]
                low = l.find("'")
                high = l.find("'")
                l = l[low+1:high]
                if len(l) > 0:
                    hyperlinks.append(l)
        print(hyperlinks)

url = str(input("Enter the url of any webiste: "))
print(url)
if len(url) > 0:
    req = requests.get(url)
    f = open('sourceCODE.txt','w')
    f.write(req.text)
    f.close()
    f = open('sourceCODE.txt','r')
    listHyperlinks(f)
    f.close()
