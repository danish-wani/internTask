from lxml import html
import requests
from lxml import etree
import urllib

f = open('links.txt','r')
links = []
for link in f:
	links.append(link)
for url in links:
	print (url)

f = open('wordMeaning','w')
#global s
#global word
for url in links:
	#url = 'http://kashmirpedia.kauls.net/Angreez'
	#print("abc---  ",url)
	page = requests.get(url)
	tree = html.fromstring(page.content)
	num = tree.xpath('/html/body/div[2]/div[4]/div[1]/blockquote//text()')
	s =""
	if len(num) == 0:
		s = 'Meaning Not available'
	else:
		for i in range (len(num)-1):
			s = s[0:]+" "+num[i] 
			#print (s)
	word = url[url.rfind('/')+1:]
	#print(word)
	s = s.strip("\r\n' '")
	s = s.replace("\r\n"," ")
	word = word.strip("\r\n' '")
	word = word.replace('%20','')
	#global wordMeaning
	wordMeaning = dict()
	wordMeaning[word] = s
	#f.write(str(wordMeaning))
	print(wordMeaning)

#break
f.read()
f.close()
	