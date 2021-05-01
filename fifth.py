def leptop_brand(number):
    number = sorted(number)         #정렬

    samsung = []                    #각 브랜드별로 리스트 생성
    apple = []
    hansung = []
    lenover = []
    LG = []
    asus = []
    others = []

    for i in number:                #알맞은 브랜드 리스트에 번호가 추가되는 반복문
        if i<2000:
            samsung.append(i)
        elif i<3000:
            apple.append(i)
        elif i<4000:
            hansung.append(i)
        elif i<5000:
            lenover.append(i)
        elif i<6000:
            LG.append(i)
        elif i<7000:
            asus.append(i)
        else:
            others.append(i)

    brand = {"삼성" : samsung, "애플" :apple, 
            "한성":hansung, "레노버":lenover,
            "엘지":LG, "아수스":asus, "기타":others}
    return brand
    
number = map(int,input("공백을 구분으로 노트북 번호 입력 : ").split())
print(leptop_brand(number))
