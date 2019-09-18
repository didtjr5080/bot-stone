import requests
from bs4 import BeautifulSoup
import re
import random
import urllib.request
import urllib.parse
import json

lastlist=[]

word=[]





if not lastlist:
    print("시작할 단어를 입력해주세요")
    c = input("끝말잇기:")
    url = requests.get("https://stdict.korean.go.kr/search/searchResult.do?pageSize=10&searchKeyword=" + c,
                       params={'pageIndex': 1})
    html = url.text
    soup = BeautifulSoup(url.content, 'html.parser')
    links = soup.select(
        "#searchDataVO > div > ul > li > dl > dt > a")  # searchDataVO > div > ul > li:nth-child(2) > dl > dt > a
    url = requests.get("https://stdict.korean.go.kr/search/searchResult.do?pageSize=10&searchKeyword=" + c,
                       params={'pageIndex': 1})
    html = url.text
    soup = BeautifulSoup(url.content, 'html.parser')
    links = soup.select(
        "#searchDataVO > div > ul > li > dl > dt > a")  # searchDataVO > div > ul > li:nth-child(2) > dl > dt > a

    # word = []
    # for url in links:
    #     # print(url.text)
    #     if url.has_attr('href'):
    #         if url.get('href').find('#none') != -1:
    #             # # print(url.text)
    #             # print(url.text.replace(" ", "").replace("-", "").replace("\r", "").replace("\t", "").replace("\n", ""))
    #             # word.append(url.text.replace(" ", "").replace("-", "").replace("\r", "").replace("\t", "").replace("\n", ""))
    #             hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')  # 한글이만 남김
    #             result = hangul.sub('', url.text)
    #             print(result)
    #             word.append(result)
    # print(word)

    lastnumfor = soup.select("#searchDataVO > div > div.paging > span.last > a")
    if len(lastnumfor) > 0:
        print(lastnumfor[0].get('onclick')[
              str(lastnumfor[0].get('onclick')).rfind('(') + 1:str(lastnumfor[0].get('onclick')).rfind(')')])

        for i in range(2, int(lastnumfor[0].get('onclick')[
                              str(lastnumfor[0].get('onclick')).rfind('(') + 1:str(lastnumfor[0].get('onclick')).rfind(
                                      ')')]) + 1):
            url = requests.get(
                "https://stdict.korean.go.kr/search/searchResult.do?pageSize=10&searchKeyword=" + c,
                params={'pageIndex': i})
            html = url.text
            soup = BeautifulSoup(url.content, 'html.parser')
            links = soup.select(
                "#searchDataVO > div > ul > li > dl > dt > a")  # searchDataVO > div > ul > li:nth-child(2) > dl > dt > a

            # word = []
            for url in links:
                # print(url.text)
                if url.has_attr('href'):
                    if url.get('href').find('#none') != -1:
                        # # print(url.text)
                        # print(url.text.replace(" ", "").replace("-", "").replace("\r", "").replace("\t", "").replace("\n", ""))
                        # word.append(url.text.replace(" ", "").replace("-", "").replace("\r", "").replace("\t", "").replace("\n", ""))
                        hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')  # 한글이만 남김
                        result = hangul.sub('', url.text)
                        # print(result)
                        if result in word:
                            continue
                        elif result not in word:
                            word.append(result)
            if len(word) > 200:
                break
        if c in word:
            url = requests.get(
                "https://stdict.korean.go.kr/search/searchResult.do?pageSize=10&searchKeyword=" + c + "*",
                params={'pageIndex': 1})
            html = url.text
            soup = BeautifulSoup(url.content, 'html.parser')
            links = soup.select(
                "#searchDataVO > div > ul > li > dl > dt > a")  # searchDataVO > div > ul > li:nth-child(2) > dl > dt > a
            url = requests.get(
                "https://stdict.korean.go.kr/search/searchResult.do?pageSize=10&searchKeyword=" + c + "*",
                params={'pageIndex': 1})
            html = url.text
            soup = BeautifulSoup(url.content, 'html.parser')
            links = soup.select(
                "#searchDataVO > div > ul > li > dl > dt > a")  # searchDataVO > div > ul > li:nth-child(2) > dl > dt > a

            # word = []
            # for url in links:
            #     # print(url.text)
            #     if url.has_attr('href'):
            #         if url.get('href').find('#none') != -1:
            #             # # print(url.text)
            #             # print(url.text.replace(" ", "").replace("-", "").replace("\r", "").replace("\t", "").replace("\n", ""))
            #             # word.append(url.text.replace(" ", "").replace("-", "").replace("\r", "").replace("\t", "").replace("\n", ""))
            #             hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')  # 한글이만 남김
            #             result = hangul.sub('', url.text)
            #             print(result)
            #             word.append(result)
            # print(word)

            lastnumfor = soup.select("#searchDataVO > div > div.paging > span.last > a")
            if len(lastnumfor) > 0:
                print(lastnumfor[0].get('onclick')[
                      str(lastnumfor[0].get('onclick')).rfind('(') + 1:str(lastnumfor[0].get('onclick')).rfind(')')])

                for i in range(2, int(lastnumfor[0].get('onclick')[
                                      str(lastnumfor[0].get('onclick')).rfind('(') + 1:str(
                                          lastnumfor[0].get('onclick')).rfind(
                                          ')')]) + 1):
                    url = requests.get(
                        "https://stdict.korean.go.kr/search/searchResult.do?pageSize=10&searchKeyword=" + c[len(c)] + "*",
                        params={'pageIndex': i})
                    html = url.text
                    soup = BeautifulSoup(url.content, 'html.parser')
                    links = soup.select(
                        "#searchDataVO > div > ul > li > dl > dt > a")  # searchDataVO > div > ul > li:nth-child(2) > dl > dt > a

                    # word = []
                    for url in links:
                        # print(url.text)
                        if url.has_attr('href'):
                            if url.get('href').find('#none') != -1:
                                # # print(url.text)
                                # print(url.text.replace(" ", "").replace("-", "").replace("\r", "").replace("\t", "").replace("\n", ""))
                                # word.append(url.text.replace(" ", "").replace("-", "").replace("\r", "").replace("\t", "").replace("\n", ""))
                                hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')  # 한글이만 남김
                                result = hangul.sub('', url.text)
                                # print(result)
                                if result in word:
                                    continue
                                elif result not in word:
                                    word.append(result)
                    if len(word) > 200:
                        break
            aa=random.choice(word)
            print(aa)
        elif c not in word:
            print("존재하지않는 단어입니다")
        print(word)
    else:
        lastnumfor = soup.select("#searchDataVO > div > div.paging > span > a")
        if len(lastnumfor) > 0:
            print(lastnumfor[len(lastnumfor) - 1].get('onclick')[
                  str(lastnumfor[len(lastnumfor) - 1].get('onclick')).rfind('(') + 1:str(
                      lastnumfor[len(lastnumfor) - 1].get('onclick')).rfind(')')])

            for i in range(2, int(lastnumfor[len(lastnumfor) - 1].get('onclick')[
                                  str(lastnumfor[len(lastnumfor) - 1].get('onclick')).rfind('(') + 1:str(
                                      lastnumfor[len(lastnumfor) - 1].get('onclick')).rfind(
                                      ')')]) + 1):
                url = requests.get(
                    "https://stdict.korean.go.kr/search/searchResult.do?pageSize=10&searchKeyword=" + c[len(c)] + "*",
                    params={'pageIndex': i})
                html = url.text
                soup = BeautifulSoup(url.content, 'html.parser')
                links = soup.select(
                    "#searchDataVO > div > ul > li > dl > dt > a")  # searchDataVO > div > ul > li:nth-child(2) > dl > dt > a

                # word = []
                for url in links:
                    # print(url.text)
                    if url.has_attr('href'):
                        if url.get('href').find('#none') != -1:
                            # # print(url.text)
                            # print(url.text.replace(" ", "").replace("-", "").replace("\r", "").replace("\t", "").replace("\n", ""))
                            # word.append(url.text.replace(" ", "").replace("-", "").replace("\r", "").replace("\t", "").replace("\n", ""))
                            hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')  # 한글이만 남김
                            result = hangul.sub('', url.text)
                            # print(result)
                            if result in word:
                                continue
                            elif result not in word:
                                word.append(result)
                if len(word) > 200:
                    break
            aa = random.choice(word)
            print(aa)
        if c not in word:
            print("존재하지않는 단어입니다")
        print(word)
else:
    while True:
        word=[]
        c = input("끝말잇기:")
        url = requests.get("https://stdict.korean.go.kr/search/searchResult.do?pageSize=10&searchKeyword=" + c,
                           params={'pageIndex': 1})
        html = url.text
        soup = BeautifulSoup(url.content, 'html.parser')
        links = soup.select(
            "#searchDataVO > div > ul > li > dl > dt > a")  # searchDataVO > div > ul > li:nth-child(2) > dl > dt > a
        url = requests.get("https://stdict.korean.go.kr/search/searchResult.do?pageSize=10&searchKeyword=" + c,
                           params={'pageIndex': 1})
        html = url.text
        soup = BeautifulSoup(url.content, 'html.parser')
        links = soup.select(
            "#searchDataVO > div > ul > li > dl > dt > a")  # searchDataVO > div > ul > li:nth-child(2) > dl > dt > a

        # word = []
        # for url in links:
        #     # print(url.text)
        #     if url.has_attr('href'):
        #         if url.get('href').find('#none') != -1:
        #             # # print(url.text)
        #             # print(url.text.replace(" ", "").replace("-", "").replace("\r", "").replace("\t", "").replace("\n", ""))
        #             # word.append(url.text.replace(" ", "").replace("-", "").replace("\r", "").replace("\t", "").replace("\n", ""))
        #             hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')  # 한글이만 남김
        #             result = hangul.sub('', url.text)
        #             print(result)
        #             word.append(result)
        # print(word)
        if lastlist in c:
            print("이미사용된 단어입니다")
        elif aa[len(aa)-1] != c[0]:
            print("첫글자와 마지막글자가 일치 하여야 합니다")
        else:
            lastnumfor = soup.select("#searchDataVO > div > div.paging > span.last > a")
            if len(lastnumfor) > 0:
                print(lastnumfor[0].get('onclick')[
                      str(lastnumfor[0].get('onclick')).rfind('(') + 1:str(lastnumfor[0].get('onclick')).rfind(')')])

                for i in range(2, int(lastnumfor[0].get('onclick')[
                                      str(lastnumfor[0].get('onclick')).rfind('(') + 1:str(lastnumfor[0].get('onclick')).rfind(
                                          ')')]) + 1):
                    url = requests.get(
                        "https://stdict.korean.go.kr/search/searchResult.do?pageSize=10&searchKeyword=" + c,
                        params={'pageIndex': i})
                    html = url.text
                    soup = BeautifulSoup(url.content, 'html.parser')
                    links = soup.select(
                        "#searchDataVO > div > ul > li > dl > dt > a")  # searchDataVO > div > ul > li:nth-child(2) > dl > dt > a

                    # word = []
                    for url in links:
                        # print(url.text)
                        if url.has_attr('href'):
                            if url.get('href').find('#none') != -1:
                                # # print(url.text)
                                # print(url.text.replace(" ", "").replace("-", "").replace("\r", "").replace("\t", "").replace("\n", ""))
                                # word.append(url.text.replace(" ", "").replace("-", "").replace("\r", "").replace("\t", "").replace("\n", ""))
                                hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')  # 한글이만 남김
                                result = hangul.sub('', url.text)
                                # print(result)
                                if result in word:
                                    continue
                                elif result not in word:
                                    word.append(result)
                    if len(word) > 200:
                        break
                aa = random.choice(word)
                print(aa)

                if c in word:
                    url = requests.get(
                        "https://stdict.korean.go.kr/search/searchResult.do?pageSize=10&searchKeyword=" + c + "*",
                        params={'pageIndex': 1})
                    html = url.text
                    soup = BeautifulSoup(url.content, 'html.parser')
                    links = soup.select(
                        "#searchDataVO > div > ul > li > dl > dt > a")  # searchDataVO > div > ul > li:nth-child(2) > dl > dt > a
                    url = requests.get(
                        "https://stdict.korean.go.kr/search/searchResult.do?pageSize=10&searchKeyword=" + c + "*",
                        params={'pageIndex': 1})
                    html = url.text
                    soup = BeautifulSoup(url.content, 'html.parser')
                    links = soup.select(
                        "#searchDataVO > div > ul > li > dl > dt > a")  # searchDataVO > div > ul > li:nth-child(2) > dl > dt > a

                    # word = []
                    # for url in links:
                    #     # print(url.text)
                    #     if url.has_attr('href'):
                    #         if url.get('href').find('#none') != -1:
                    #             # # print(url.text)
                    #             # print(url.text.replace(" ", "").replace("-", "").replace("\r", "").replace("\t", "").replace("\n", ""))
                    #             # word.append(url.text.replace(" ", "").replace("-", "").replace("\r", "").replace("\t", "").replace("\n", ""))
                    #             hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')  # 한글이만 남김
                    #             result = hangul.sub('', url.text)
                    #             print(result)
                    #             word.append(result)
                    # print(word)

                    lastnumfor = soup.select("#searchDataVO > div > div.paging > span.last > a")
                    if len(lastnumfor) > 0:
                        print(lastnumfor[0].get('onclick')[
                              str(lastnumfor[0].get('onclick')).rfind('(') + 1:str(lastnumfor[0].get('onclick')).rfind(')')])

                        for i in range(2, int(lastnumfor[0].get('onclick')[
                                              str(lastnumfor[0].get('onclick')).rfind('(') + 1:str(
                                                  lastnumfor[0].get('onclick')).rfind(
                                                  ')')]) + 1):
                            url = requests.get(
                                "https://stdict.korean.go.kr/search/searchResult.do?pageSize=10&searchKeyword=" + c[
                                    len(c)] + "*",
                                params={'pageIndex': i})
                            html = url.text
                            soup = BeautifulSoup(url.content, 'html.parser')
                            links = soup.select(
                                "#searchDataVO > div > ul > li > dl > dt > a")  # searchDataVO > div > ul > li:nth-child(2) > dl > dt > a

                            # word = []
                            for url in links:
                                # print(url.text)
                                if url.has_attr('href'):
                                    if url.get('href').find('#none') != -1:
                                        # # print(url.text)
                                        # print(url.text.replace(" ", "").replace("-", "").replace("\r", "").replace("\t", "").replace("\n", ""))
                                        # word.append(url.text.replace(" ", "").replace("-", "").replace("\r", "").replace("\t", "").replace("\n", ""))
                                        hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')  # 한글이만 남김
                                        result = hangul.sub('', url.text)
                                        # print(result)
                                        if result in word:
                                            continue
                                        elif result not in word:
                                            word.append(result)
                            if len(word) > 200:
                                break
                    aa = random.choice(word)
                    print(aa)
                else:
                    print("존재하지않는 단어입니다")

    # c=input(":")

