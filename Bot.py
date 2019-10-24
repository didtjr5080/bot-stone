from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import re

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
        print(int(b[0]) * int(b[1]))
    except ValueError:
        계산실패()

def 나누기 (user):
    b = user.split("/")
    try:
        print(int(b[0]) / int(b[1]))
    except ValueError:
        계산실패()

def 더하기 (user):
    b = user.split("+")
    try:
        print(int(b[0]) + int(b[1]))
    except ValueError:
        계산실패()

def 빼기 (user):
    b = user.split("-")
    try:
        print(int(b[0]) - int(b[1]))
    except ValueError:
        계산실패()

dbi=[]
dbo=[]
about=[]
patch=[]
command=[]
with open("dateru","rt",encoding='UTF8') as f:
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

with open("daterb","rt",encoding='utf-8') as f:
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

with open("about", "rt", encoding='utf-8') as f:
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

with open("patch", "rt", encoding='utf-8') as f:
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
with open("command", "rt", encoding='utf-8') as f:
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

def 사전 (find):
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
      # 한글과 띄어쓰기를 제외한 모든 부분을 제거



    if (rescode == 200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)


while True:
    user = input("user:")
    test=user.split(" ")
    user=test[0]
    X = user.find('*')
    N = user.find('/')
    P = user.find('+')
    M = user.find('-')
    # print (test)
    # print(user)
    # print (dbo)
    # print (about)
    if user[0]== "/":
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
        else:
            print("잘못된 명령어 입니다")



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
            print("ston:" + dbo[a])

        elif user[X] != "*" and user[N] != "/" and user[P] != "+" and user[M] != "-" and user not in dbi:
            print("stone:이럴땐 어떻게 대답을 해야하죠?")
            user1 = input("teach:")
            with open("dateru", "at", encoding='utf-8')as f:
                f.write('\n')
                f.write(user)
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


        # print("dbi",dbi)
        # print("dbo", dbo)
