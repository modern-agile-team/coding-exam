wrong_data = input("잘못된 데이터 : ")

data = ""
wrong_data = wrong_data.split(" ")

for i in wrong_data:
    if i[:len(i) // 2] == i[len(i) // 2 :]:
        data += i[:len(i) // 2] + " "
    else:
        data += i + " "

result = ""
for i in data:
    if i.isupper() == 1:
        i = i.lower()
    else:
        i = i.upper()
    result += i

result = result.rstrip(" ")
print(result)
