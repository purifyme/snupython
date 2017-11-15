# Python 샘플 코드 #
"""
from urllib2 import Request, urlopen
from urllib import urlencode, quote_plus
"""

import pandas as pd # data frame이라는 구조를 사용하기 위해. 표 형식을 제공한다.
import urllib.request
import pylab as plt
import matplotlib
import matplotlib.font_manager as fm # 한글 label 설정을 위해

url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev?'
queryParams = '?' + urllib.parse.urlencode({ urllib.parse.quote_plus('serviceKey') : 'Oj2fT3dvg1skRt3JPVJfhKBZV+cgnVWL9S2WTwUuLqbXiyY84lyN93SwMqocuiLn6KN41g4Cy1hKfb3XErMrzw==',
                                urllib.parse.quote_plus('pageNo') : '1',
                                urllib.parse.quote_plus('numOfRows') : '10', urllib.parse.quote_plus('LAWD_CD') : '11650',
                                urllib.parse.quote_plus('DEAL_YMD') : '201711' })

request = urllib.request.Request(url + queryParams)
request.get_method = lambda: 'GET'
"""
response_body = urllib.request.urlopen(request).read()
print(response_body)
"""

def getaptdata(address, yearmonth):
    url = "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade?LAWD_CD=" + str(
        address) + "&DEAL_YMD=" + str(
        yearmonth) + "&serviceKey=yUZ5XFWYdge8F%2FIWh28jqxiZaCl6yHbUkujV%2BJ7VY6x5V%2FTYMJTxVuYbf%2FhF56d4WdKpQpsJLFRZpSpWdQzKcQ%3D%3D"
    f = urllib.request.urlopen(url)
    aptdata2 = f.read().decode("utf8")
    f.close()
    soup = BeautifulSoup(aptdata2, 'html.parser')

    # item 엘레멘트들을 찾아서, item내에서 >으로 구분하여 list로 만들어 줌
    aptdata = list(aptdata.get_text().replace('\n', '').split(">") for aptdata in soup.find_all("item"))

    print("=============aptdata==========")
    for a in aptdata:
        print(str(a))
    blist1 = []
    blist2 = []
    blist3 = []
    blist4 = []
    blist5 = []
    blist6 = []
    blist7 = []
    blist8 = []
    blist9 = []
    blist10 = []
    blist11 = []
    blist12 = []

# 필요한 부분만 떼어내어, column 별로 저장
    for i in aptdata:
        blist1.append(i[0][:-4])
        blist2.append(i[1][:-5])
        blist3.append(i[2][:-2]) #1을 2로
        blist4.append(i[3][:-4])
        blist5.append(i[4][:-4])
        blist6.append(i[5][:-2])
        blist7.append(i[6][:-2])
        blist8.append(i[7][:-5])
        blist9.append(i[8][:-3])
        blist10.append(i[9][:-5])
        blist11.append(i[10][:-2]) #1을 4로
        blist12.append(i[11][:]) #1을 4로

    print("blist 출력")
    for i in range(1, 13):
        print("blist"+str(i)+":"+str(eval("blist"+str(i))))
    #data frame 형태 만들기, columns를 정의하면, 그 순서로 출력됨. 아니면, 임의의 순서로.
    apt = pd.DataFrame(
        {'년': blist4, '월': blist7, '일': blist8,  '법정동': blist5, '아파트': blist6, '전용면적': blist9, '층':blist12, '거래금액': blist2, '건축년도': blist3,
          '번지': blist10, '지역코드': blist11}, columns = [ '년', '월',  '일', '법정동', '아파트', '전용면적', '층','거래금액', '건축년도',
         '번지', '지역코드'])

    plt.plot(blist3, blist2)
    plt.xlabel('건축년도') #x축 레이블 설정
    plt.ylabel('거래금액') #y축 레이블 설정
    plt.show()

    print(apt)
    return (apt)


# 한번 해 보기
file = open("부동산","w",encoding='utf-8')

from bs4 import BeautifulSoup

f = urllib.request.urlopen(request)
resultXML = f.read( )
print("resultXML", resultXML)
xmlsoup = BeautifulSoup(resultXML,'html.parser')

items = xmlsoup.find_all('item')
print("items", items)
for item in items :
     file.write('\n-----------------------------------------\n')
     file.write(str(item))
#     file.write('아파트 : ' + item.title.get_text(strip=True) + '\n')
#     file.write('거래금액 : ' + item.description.get_text(strip=True) + '\n')
     file.write('\n')

file.close( )

font_location="C:\\Windows\\Fonts\\ngulim.ttf" # font 파일 위치
font_name = fm.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name) #font 설정
seocho=getaptdata(11650,201709)
seocho.to_csv('seocho_201711.csv', encoding='utf-8')

