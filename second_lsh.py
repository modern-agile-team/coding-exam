time = input("시각 : ")

result = time.split(":")

result[0] += "시"
result[1] += "분"
result[2] += "초"

print(result)