import requests
import re
def listHyperlinks(f):
    hyperlinks = []
    #flag = False
    #for line in f:
        #line = line.rstrip()
        #line = line.split(' ')
        #print(line)
        
    txt = f.read().replace('\n',' ')
    print(txt)
    #print(txt.find('<a'))    
    #loc = txt.find("<a")
    
    match = re.match(r'href=[A-Za-z0-9.@]"',txt)
    print( match.groups())
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #if 'href' in f:
            #start = line.find('href')
            #print(f.seek())
    '''for l in line:
            if 'href' in l:
                low = l.find('"')
                #low = l.find("'")
                #high = l.find("'")
                l = l[low+1:high]
                if len(l) > 0:
                    hyperlinks.append('http://kashmirpedia.kauls.net/'+l)
    print(hyperlinks)'''

url = str(input("Enter the url of any webiste: "))
#print(url)
if len(url) > 0:
    req = requests.get(url)
    f = open('sourceCODE.txt','w')
    f.write(req.text)
    f.close()
    f = open('sourceCODE.txt','r')
    listHyperlinks(f)
    f.close()
