"""
신삼호 62평과 35평 비교
"""
import realty as r
import pylab as plt
import matplotlib
import matplotlib.font_manager as fm # 한글 label 설정을 위해

# 그래프의 한글 폰트 설정
font_location="C:\\Windows\\Fonts\\ngulim.ttf" # font 파일 위치
font_name = fm.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name) #font 설정

#2005년부터 2017년까지 그래프 그리기
data1 = [[], []]
data1_1 = [[], []]
data2 = [[], []]
for i in range(2006, 2018):
    for j in range(1, 13):
        ym=str(i)
        if (j < 10):
            ym=ym+"0"+str(j)
        else:
            ym=ym+str(j)
        seocho=r.getaptdata(11650, ym)
        data1=r.x_y_data(seocho, "방배신삼호", 185.46, data1)
        data1_1=r.x_y_data(seocho, "방배신삼호", 105.04, data1_1)
        data2=r.x_y_data(seocho, "방배신삼호", 164.97, data2)

plt.plot(data1[0], data1[1], label="방배신삼호62평")
plt.plot(data2[0], data2[1], label="방배신삼호55평")
plt.plot(data1_1[0], data1_1[1], label="방배신삼호35평")
plt.legend(loc='upper left')
plt.title('방배신삼호62평 vs 55평 vs 35평')
plt.xlabel('거래년월') #x축 레이블 설정
plt.ylabel('거래금액') #y축 레이블 설정

plt.show()