from bs4  import *
from urllib.request import urlopen

d={}
x=0;
print(len(open('Users.txt').read().split(',')))
for UserName in open('Users.txt').read().split(',')[:10000]:
    try:
        page = urlopen("http://habrahabr.ru/users/%s/"%UserName)
        soup = BeautifulSoup(page.read(), from_encoding="utf-8")
        d[UserName]=(float(soup.find(True, 'num').text.replace(",",".").replace(u'\u2013','-')),
                     int(soup.find(True, 'votes').text.split()[0]))

        x+=1
        print(x)
    except : pass

open('Result.txt', 'w').write(str(d))
