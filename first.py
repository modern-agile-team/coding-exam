a = input("점수들을 입력하세요. : ")
A = (a.split(", "))
b = len(A)
sum = 0
if (b>100)|(b<1):
    print("범위 오류입니다.")
else :    
    for i in range(b):
        c = int(A[i])
        if (c>100)|(c<0):
            print("범위 오류입니다.")
        else : 
            sum+=c
    sum = sum /b
    print(round(sum))