def user_data(n):                                                   #유저의 데이터를 성별과 이름으로 나누어서 저장하는 함수 생성
    
    data_list = []
    for i in range(n):                                              #입력한 숫자만큼 입력을 받도록 하는 반복문.
        data = input("공백을 구분으로 이름과 성별을 입력하세요 : ")     
        data_list.append(data)                                      #입력받은 데이터를 리스트에 추가한다.

    data_dic = {}
    for i in range(len(data_list)):                                 #리스트를 딕셔너리 형식으로 변환.
        name = data_list[i][:-3]                                    #(이름) 공백과 성별을 포함한 마지막 3자리를 제외하고 name이라는 변수에 추가.
        sex = data_list[i][-2:]                                     #(성별) 마지막 2자리만 sex 변수에 추가한다.
        data_dic[name] = sex                                        #잘라낸 이름을 key값으로 성별을 value 값으로 한다.
    
    return data_dic

n = int(input("입력값을 입력하세요 : "))
print(user_data(n))