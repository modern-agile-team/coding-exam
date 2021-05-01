h, m, s = list(input("시간, 분, 초를 입력하세요 : ").split(":"))

if h<=0 and h>=24:
    if m<=0 and m>60:
        if s<=0 and s>60:
            print(h,"시", end='')
            print(m,"분", end='')
            print(s,"초", end='')
        else:
            print("오류")
    else:
        print("오류")
else:
    print("오류")