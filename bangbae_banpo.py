"""
신삼호 62평과 반래퍼 35평 비교
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
data2_1 = [[], []]
data2_2 = [[], []]
data2_3 = [[], []]
for i in range(2006, 2018):
    for j in range(1, 13):
        ym=str(i)
        if (j < 10):
            ym=ym+"0"+str(j)
        else:
            ym=ym+str(j)
        seocho=r.getaptdata(11650, ym)
        data1=r.x_y_data(seocho, "방배신삼호", 185.46, data1)
        data1_1=r.x_y_data(seocho, "래미안퍼스티지", 135.92, data1_1)
        data2=r.x_y_data(seocho, "래미안퍼스티지", 84.93, data2)
        data2_1=r.x_y_data(seocho, "래미안퍼스티지", 117.12, data2_1)
        data2_2=r.x_y_data(seocho, "래미안퍼스티지", 169.31, data2_2)
        data2_3=r.x_y_data(seocho, "래미안퍼스티지", 198.22, data2_3)

plt.plot(data1[0], data1[1], label="방배신삼호62평")
plt.plot(data1_1[0], data1_1[1], label="반래퍼52평")
plt.plot(data2[0], data2[1], label="반래퍼35평")
plt.plot(data2_1[0], data2_1[1], label="반래퍼45평")
plt.plot(data2_2[0], data2_2[1], label="반래퍼62평")
plt.plot(data2_3[0], data2_3[1], label="반래퍼72평")

plt.legend(loc='upper left')
plt.title('방배신삼호62평 vs 반래퍼')
plt.xlabel('거래년월') #x축 레이블 설정
plt.ylabel('거래금액') #y축 레이블 설정

plt.show()