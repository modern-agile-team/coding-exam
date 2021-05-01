data = list(input("데이터를 입력하세요 : ").split())

new_data = []                       #중복을 제거한 데이터를 담을 새로운 리스트

for d in data:                      # 새로 만든 리스트에 기존 데이터가 없다면 추가 하는 코드
    if d not in new_data:   
        new_data.append(d)

n = len(new_data)
last_data = []                      #대소문자를 변경해서 담을 새로운 리스트

for j in range(n):                   #아스키코드를 활용해서 90보다 작으면(대문자라면) +32를 통해 소문자로 변경
    if ord(data[j]) < 90:           
        n = ord(data[j])
        n += 32
        data[j] = chr(n)
    else:                           #아스키코드를 활용해서 90보다 크면(소문자라면) -32를 통해 소문자로 변경
        n = ord(data[j])
        n -= 32
        data[j] = chr(n)
    last_data.append(data[j])       #변경한 데이터를 빈 리스트에 추가


print(last_data)                    # 이렇게 하고싶었는데 잘 안되네요...ㅠㅠ


