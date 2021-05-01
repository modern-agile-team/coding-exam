notebook = {}
num = input().split(' ')
n = len(num)
num = map(int, num) #문자열배열을 정수형 배열로 전환

for i in range(0, n+1, 1) :
  if  1000<= num[i] >= 1999 :
    notebook["삼성"] = num[i] 
  elif 2000<= num[i] >= 2999 :
    notebook["애플"] = num[i]
  elif 3000<= num[i] >= 3999 :
    notebook["한성"] = num[i]
  elif 4000<= num[i] >= 4999 :
    notebook["레노버"] = num[i]
  elif 5000<= num[i] >= 5999 :
    notebook["애플"] = num[i]
  elif 6000<= num[i] >= 6999 :
    notebook["애플"] = num[i]
  else :
    notebook["기타"] = num[i]