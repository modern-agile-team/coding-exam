input_num = [-5,2,13,23,100,4]
#정수들을 원소로 가지는 배열을 입력해 주세요
array_num = []
array_min = min(input_num)
array_max = max(input_num)
array_total = 0 
for i in input_num:
        array_total+=i
array_num.append(array_min)
array_num.append(array_total)
array_num.append(array_max)
print(array_num)

