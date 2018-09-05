from BeautifulSoup import BeautifulSoup
import requests
import re

hyperlinks = []
url = str(input("Enter the url: "))
if(len(url) > 0):
        req = requests.get(url)
        soup = BeautifulSoup(req)
        for link in soup.findAll('a'):
            hyperlinks.append(link)

        print(hyperlinks)
