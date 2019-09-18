import requests
from bs4 import BeautifulSoup

c=input(":")

link = requests.get("https://stdict.korean.go.kr/search/searchResult.do?pageSize=10&searchKeyword" + c + "*")
# print(url)
html=link.text
# print(html)
# print(url)
soup=BeautifulSoup(html,'html.parser')

links = soup.select("dt > a")

for link in links:
    print("가")
    if link.has_attr('href'):
        print("나")
        if link.get('href').find('#none') != -1:
            print(link.text)
            print("다")