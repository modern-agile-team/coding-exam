listNum = str(input("점수를 입력하세요: "))

for i in range(0, len(listNum)):
    listNum.split(",")
    lst = [int(i) for i in listNum]
    lst.append(listNum)
    
average = sum(lst) / listNum

print(int(average))