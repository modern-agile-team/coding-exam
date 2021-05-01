n = int(input("유저 데이터의 개수 ->"))
dic = {}

if n < 1 or n > 100: 
  print("다시 실행후 1~100의 숫자를 입력하세요")

for i in range(1, n+1, 1) :    
  userdata1, userdata2 = input().split(' ')
  dic[userdata1] = userdata2

print(dic)