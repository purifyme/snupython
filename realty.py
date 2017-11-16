import urllib.request

from bs4 import BeautifulSoup
import re #regular expression

def to_int(price):
    price=re.sub(',','', price)
    return int(price)

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

    return aptdata
"""
    print("=============aptdata==========")
    for a in aptdata:
        print(str(a))
"""


def x_y_data(aptdata, apt, area, x_y):
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

#    k=0
    isSame=False #바로 앞 년
    sum=0
    count=0
    for i in range(0, len(blist6)):
        if re.search(apt, blist6[i]):
            if to_int(blist2[i]) <=30000: # noise 제거
                continue
            if float(blist9[i]) >= area-2 and float(blist9[i]) <= area+2:
                sum+=to_int(blist2[i])
                count +=1
                print("year=", blist4[i], "sum=", sum, "count=", count, "price=",blist2[i] )
    if (sum != 0):
        x_y[0].append(to_int(blist4[i])+to_int(blist7[i])/12)
#                print("0", x_y[0][k])
        x_y[1].append(sum/count)#같은 해에 여러건 매매된 경우, 평균가격을 저장
#                k +=1
    return x_y

    #data frame 형태 만들기, columns를 정의하면, 그 순서로 출력됨. 아니면, 임의의 순서로.
"""
    apt = pd.DataFrame(
        {'년': blist4, '월': blist7, '일': blist8,  '법정동': blist5, '아파트': blist6, '전용면적': blist9, '층':blist12, '거래금액': blist2, '건축년도': blist3,
          '번지': blist10, '지역코드': blist11}, columns = [ '년', '월',  '일', '법정동', '아파트', '전용면적', '층','거래금액', '건축년도',
         '번지', '지역코드'])
"""
