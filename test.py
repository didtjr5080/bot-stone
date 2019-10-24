import requests
from bs4 import BeautifulSoup
import re
import urllib.request
import urllib.parse
import json

c= input(":")

url = requests.get("https://terms.naver.com/search.nhn?query=티모&searchType=text&nluQuery=" + c )
html=url.text
soup=BeautifulSoup(url.content,'html.parser')
links = soup.select("#searchDataVO > div >  ul > il > div > strong > a")#searchDataVO > div > ul > li:nth-child(2) > dl > dt > a

word = []
for url in links:
    # print(url.text)
    if url.has_attr('href'):
        if url.get('href').find('#none') != -1:
            # # print(url.text)
            # print(url.text.replace(" ", "").replace("-", "").replace("\r", "").replace("\t", "").replace("\n", ""))
            # word.append(url.text.replace(" ", "").replace("-", "").replace("\r", "").replace("\t", "").replace("\n", ""))
            hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')  # 한글이만 남김
            result = hangul.sub('', url.text)
            print(result)
            word.append(result)
print(word)
