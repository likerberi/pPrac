import urllib.request
from bs4 import BeautifulSoup

url = "http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu"
soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")
#a_tags = soup.find_all('a')
a_tags = soup.find_all('title')
print(a_tags)
for idx in a_tags:
    if(idx.get('video-title') == None):
        continue
    else:
        print(idx.get('title'))


