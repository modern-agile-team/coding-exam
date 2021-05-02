data = list(input("데이터를 입력하세요 : ").split())

new_data = []                                               #중복을 제거한 데이터를 담을 새로운 리스트
for d in range(len(data)):                                  # 새로 만든 리스트에 기존 데이터가 없다면 추가 하는 코드
    if data[d] not in new_data:   
        new_data.append(data[d])

new_data = "".join(new_data)
print(new_data)

last_data = []                                              #대소문자를 변경해서 담을 새로운 리스트
for i in range(len(new_data)):
    if (ord(new_data[i]) < 91 and ord(new_data[i])>65):
        n = ord(new_data[i])
        n+=32
        last_data.append(chr(n))
    elif (ord(new_data[i]) > 96 and ord(new_data[i])<123):
        n = ord(new_data[i])
        n-=32
        last_data.append(chr(n))
    else:
        last_data.append(new_data[i])

last_data = "".join(last_data)
print(last_data,type(last_data))