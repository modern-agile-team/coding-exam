
a = input('점수를 입력하세요 : ').split(', ')


for i in range(101):
    if len(a)> 0 & len(a)<=100: 
        if  a[i]<=0 & a[i]>=100:         // 정수형 변환을 모르겠어요.. ㅠㅠ
            sum(a[i]) / len(a)
        else:
            print("오류") 
    else:
        print("오류0")


def average(a):
    return (sum(a) / len(a))
