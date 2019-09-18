from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import re
import random

import win32com.client as wincl



speak = wincl.Dispatch("SAPI.SpVoice")



dbi=[]#유저가 입력한 데이터  리스트
dbo=[]#봇이 답 할 데이터 리스트
about=[]#프로그램 정보
patch=[]#패치노트
command=[]#명령어 목록
word=[]#크롤링데이터 저장 리스트
count=1#봇이 출력할값 검사할때 사용되는변수
hicount=0#봇이 출력할값 검사할때 사용되는변수
hilen=0#봇이 출력할값 검사할때 사용되는변수
p=""#봇의 대답수정할때 사용됨
change1=[]# 정보 수정 할 때 사용되는 리스트
change2=[]# 정보 수정 할 때 사용되는 리스트
sc3=0# 정보 수정할 때 쓰임

def get_html(url):
   _html = ""
   resp = requests.get(url)
   if resp.status_code == 200:
      _html = resp.text
   return _html

def 계산실패():
    print("입력한 값중 숫자가 아닌 값이 포합되어있습니다")

def 곱하기 (user):
    b = user.split("*")
    try:
        speak.Speak(int(b[0]) * int(b[1]),"입니다")
        print(int(b[0]) * int(b[1]),"입니다")
    except ValueError:
        계산실패()

def 나누기 (user):
    b = user.split("/")
    try:
        speak.Speak(int(b[0]) / int(b[1]), "입니다")
        print(int(b[0]) / int(b[1]),"입니다")
    except ValueError:
        계산실패()

def 더하기 (user):
    b = user.split("+")
    try:
        speak.Speak(int(b[0]) + int(b[1]), "입니다")
        print(int(b[0]) + int(b[1]),"입니다")
    except ValueError:
        계산실패()

def 빼기 (user):
    b = user.split("-")
    try:
        speak.Speak(int(b[0]) - int(b[1]), "입니다")
        print(int(b[0]) - int(b[1]),"입니다")
    except ValueError:
        계산실패()


with open("dateru","rt",encoding='UTF8') as f:#유저가 입력한 데이터 불러오기
    while True:
        line= f.readline()
        # print("line"+line)
        임시=line.split("\n")
        # print ("임시:",임시)
        # print(len(임시))
        dbi.append(임시[0])
        # print("dbi",dbi)
        if not line:
            break

with open("daterb","rt",encoding='utf-8') as f:#봇이 대답할수있는 데이터 불러오기
    while True:
        line = f.readline()
        # print("line" + line)
        임시 = line.split("\n")
        # print ("임시:", 임시)
        # print(len(임시))
        aaa=임시[0].split(" ")
        bbb=""
        for i in range(0,len(aaa)):
            if bbb== "":
                bbb=aaa[0]
            else:
                bbb=bbb+aaa[i]
        dbo.append(bbb)
        print(dbo)
        # print("dbo", dbo)
        if not line:
            break

with open("about", "rt", encoding='utf-8') as f:#프로그램정보 불러오기
    while True:
        line = f.readline()
        # print("line" + line)
        임시 = line.split("\n")
        # print ("임시:", 임시)
        # print(len(임시))
        about.append(임시[0])
        # print("dbo", dbo)
        if not line:
            break

with open("patch", "rt", encoding='utf-8') as f:#패치노트 불러오기
    while True:
        line = f.readline()
        # print("line" + line)
        임시 = line.split("\n")
        # print ("임시:", 임시)
        # print(len(임시))
        patch.append(임시[0])
        # print("dbo", dbo)
        if not line:
            break
with open("command", "rt", encoding='utf-8') as f:#명령어 목록 불러오기
    while True:
        line = f.readline()
        # print("line" + line)
        임시 = line.split("\n")
        # print ("임시:", 임시)
        # print(len(임시))
        command.append(임시[0])
        # print("dbo", dbo)
        if not line:
            break

def 사전 (find):#단어 데이터 크롤링
    import urllib.request
    from bs4 import BeautifulSoup as bs

    # aa = input("user:")
    client_id = "rbuhBPQ9m7B18FTs5uwl"
    client_secret = "VMusPkMfoc"
    encText = urllib.parse.quote(find)
    url = "https://openapi.naver.com/v1/search/encyc.xml?query=" + encText  # json 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    soup = bs(response, "html.parser")
    a = soup.find_all('description')
    # print(a)

    list = []
    for i in range(1, len(a)):
        # print(a[i])
        b = str(a[i])
        # print(b)
        c = b.split("<description>")
        # print("split",c)
        d = str(c[1])
        e = d.split("</description>")
        list.append(e[0])
    hangul = re.compile('[^ ㄱ-ㅣ가-힣0-9999]+')#한글이랑 숫자만 남김
    for i in range (0,len(list)):
        result = hangul.sub('', list[i])
        if i == 0:
            print(find, ":", i + 1, ".", result)
        else:
            print(" "," ","",i + 1, ".", result)
    speak.Speak("사전에서", find, "에대해 겁생한 결과입니다")
      # 한글과 띄어쓰기를 제외한 모든 부분을 제거



    if (rescode == 200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)


def list_change(sc3,list_num):# 2개로 나누었던 대답과 횟수 합치는 함수
    st=" "

    while sc3 >= len (change2):
        if " " == st:
            st=change2[sc3] + "." + change2[sc3]
        else:
            st=st + "." + change2[sc3] + "." + change2[sc3]
        sc3+=1
        if sc3 >= len(change2):
            dbo[list_num] = st
    print("d")





while True:
    user = input("user:")
    test=user.split(" ")#띄어 쓰기 기준 쪼개기
    user=test[0]
    X = user.find('*')
    N = user.find('/')
    P = user.find('+')
    M = user.find('-')
    # print (test)
    # print(user)
    # print (dbo)
    # print (about)
    print (test)
    if not user:
        continue
    else:
        if user[0] == "/":
            if user == "/정보":
                for i in range(0,len(about)):
                   print (about[i])

            elif test[0] == "/사전":
                find = test[1]
                사전(find)

            elif user == "/패치노트":
                for i in range(0,len(patch)):
                   print (patch[i])

            elif user == "/?" or user == "/help":
                for i in range(0,len(command)):
                   print (command[i])

            elif test[0] == "/수정요청":
                print(test[1])
                if test [1] in dbi:
                    list_num = dbi.index(test[1])#test[1] = 유저가 입력했을 때 데이터
                    # print("list_num:",list_num)
                    opw=dbo[list_num]
                    # print("opw:",opw)
                    save_dbi_wait=opw.split(".")
                    print("sdw:",save_dbi_wait)
                    print("scw1",save_dbi_wait[0])
                    sc=0
                    while sc <= len(save_dbi_wait):
                        if sc >= len(save_dbi_wait):
                            continue
                        print("sc:",sc)
                        print("sdw",save_dbi_wait[sc])
                        change1.append(save_dbi_wait[sc])
                        sc+=2
                        print("a")
                        if sc >= len(save_dbi_wait):
                            continue


                    sc1 = 1
                    print(save_dbi_wait)
                    while sc1 <= len(save_dbi_wait):
                        change2.append(save_dbi_wait[sc1])
                        sc1+=2

                        if sc1 >= len(save_dbi_wait):
                            continue
                        print("as")
                    print("c1",change1)
                    print("c2", change2)
                    if test [2] in dbo:#유저가 입력 한 값을 비교해 숫자 증가
                        save_num=change1.index(test[2])
                        change_num= int(change2[save_num])
                        change_num+=1
                        cn_save=str(save_num)
                        change2[save_num] = cn_save
                        list_change(sc3, list_num)
                        print('b')


                    elif test[2] not in dbo:
                        change1.append(test[2])
                        change2.append("1")
                        list_change(sc3, list_num)
                        print("c")
                print("dbo",dbo,"dbi",dbi)






            # elif user == "/끝말잇기":
            #     끝말잇기 = True
            #     print("끝말잇기가 시작되었습니다 시작할 단어를 입력해주세요")
            # elif user == "/항복":
            #     끝말잇기 == False
            #     print("user가 항복하여 Stone이 승리하였습니다")
            #     life = 3
            else:
                print("잘못된 명령어 입니다")
                speak.Speak("잘못된 명령어 입니다")




        else:
                if user[X] == "*":
                    곱하기(user)
                if user[N] == "/":
                    나누기(user)
                if user[P] == "+":
                    더하기(user)
                if user[M] == "-":
                    빼기(user)

                elif user in dbi:
                    a = dbi.index(user)
                    print(a)
                    b=dbo[a].split(",")
                    print(b)
                    c=[]
                    for i in range(0,len(b)):
                        c.append(b[i])
                    print(c)
                    d=[]
                    for i in range(0,len(c)):
                        x=c[i].split(".")
                        for j in range(0,len(x)):
                            d.append(x[j])
                    print(d)
                    while count<len(d):
                        # print("hilen:",hilen)
                        # print("hicount:",hicount)
                        # print(d[count])
                        if int(d[count]) < hicount:
                            hilen == count -1
                        if count <= len(d):
                            e=d[hilen]
                        count+=2
                    if hilen < 3:
                        print(e + "[공부 필요]")
                        speak.Speak(e+",방금한 대답은 더 공부할 필요가 있어요")
                    else:
                        speak.Speak(e)
                        print(e)
                    # print("ston:" + dbo[a])
                    # speak.Speak(dbo[a])
                elif user[X] != "*" and user[N] != "/" and user[P] != "+" and user[M] != "-" and user not in dbi:
                    print("stone:이럴땐 어떻게 대답을 해야하죠?")
                    speak.Speak("이럴땐 어떻게 대답을 해야하죠?")
                    user1 = input("teach:")
                    with open("dateru", "at", encoding='utf-8')as f:
                        f.write('\n')
                        f.write(user+"1")
                    with open("daterb", "at", encoding='utf-8')as f:
                        f.write('\n')
                        f.write(user1)

                    dbi = []
                    dbo = []

                    with open("dateru", "rt", encoding='UTF8') as f:
                        while True:
                            line = f.readline()
                            # print("line" + line)
                            임시 = line.split("\n")
                            # print ("임시:", 임시)
                            # print(len(임시))
                            dbi.append(임시[0])
                            # print("dbi", dbi)
                            if not line:
                                break

                    with open("daterb", "rt", encoding='utf-8') as f:
                        while True:
                            line = f.readline()
                            # print("line" + line)
                            임시 = line.split("\n")
                            # print ("임시:", 임시)
                            # print(len(임시))
                            dbo.append(임시[0])
                            # print("dbo", dbo)
                            if not line:
                                break
                                print("정보를 저장하였습니다")

