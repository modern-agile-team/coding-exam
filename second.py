import numpy as np
TIME_DATA = input("시간 데이터를 입력하세요 : ")
time = (TIME_DATA.split(":"))
for i in range(3):
    a = int (time[i])
    if i==0 :   
        if (a<0)|(a>23):
            print("시에 오류가 있습니다.")
    else: 
        if (a<0)|(a>59):
            print("분이나 초에 오류가 있습니다.") 
table = np.array([time[0]+"시",time[1]+"분",time[2]+"초"])
print(table)