import os
import sys
import urllib.request
from bs4 import BeautifulSoup as bs
import re

aa=input("user:")
client_id = "rbuhBPQ9m7B18FTs5uwl"
client_secret = "VMusPkMfoc"
encText = urllib.parse.quote(aa)



url = "https://openapi.naver.com/v1/search/encyc.xml?query=" + encText + "*" + "&isDisplayAll=false&page=3"# json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

print(url)

soup= bs(response,"html.parser")
print(soup)
a= soup.find_all('title')
print(a)
hangul = re.compile('[^ ㄱ-ㅣ가-힣0-9999]+')
list=[""]
for i in range(1,len(a)):
    # print(a[i])
    b=str(a[i])
    # print(b)
    c= b.split("<title>")
    # print("split",c)
    d = str(c[1])
    e= d.split("</title>")
    result = hangul.sub('', e[0])
    if list[0] == "":
        list[0]=result
    elif list[0] != "" and result not in list:
        list.append(result)
    elif list[0] != "" and result in list:
        continue
    # if list[0] == "":
    #     list[0]=result
    # elif list[0] != ""and list[list.index(result)] == result:
    #     continue
    # elif list[0] != "" and list[list.index(result)] != result:
    #     list.append(result)


print(list)

if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)