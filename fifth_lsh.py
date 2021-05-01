import pprint
labtop_num = []
labtop_num += map(int, input().split(" "))
labtop_num.sort()
labtop_brand = {"삼성" : [], "애플": [], "한성": [], "레노버": [], "LG": [], "아수스": [], "기타": []}

for i in labtop_num:
    if i // 1000 == 1:
        labtop_brand["삼성"].append(i)
    elif i // 1000 == 2:
        labtop_brand["애플"].append(i)
    elif i // 1000 == 3:
        labtop_brand["한성"].append(i)
    elif i // 1000 == 4:
        labtop_brand["레노버"].append(i)
    elif i // 1000 == 5:
        labtop_brand["LG"].append(i)
    elif i // 1000 == 6:
        labtop_brand["아수스"].append(i)
    else:  
        labtop_brand["기타"].append(i)

pprint.pprint(labtop_brand)