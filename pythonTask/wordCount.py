# counts occurence of each word 

def cswordCount(f): 
    wordcount = {}
    for line in f:
        line = line.rstrip()
        line = line.split(' ')
        for l in line:
            if l in wordcount:
                wordcount[l] = wordcount[l] + 1
            else:
                wordcount[l] = 1
    print('CASE SENSITIVE MATCHING')
    print(wordcount)
    f.seek(0)
    wordcountci = {}
    for li in f:
        li = li.rstrip()
        li = li.lower()
        li = li.split(' ')
        for l in li:
            if l in wordcountci:
                wordcountci[l] = wordcountci[l] + 1
            else:
                wordcountci[l] = 1
    print('CASE INSENSITIVE MATCHING')
    print(wordcountci)



f = open('file.txt','r')
cswordCount(f)
f.close()
