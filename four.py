word =  list(input().split())
new_word = []
Result = ""
for i in word :
    new_word.append(i[:len(i)//2]) #중복되는 단어를 중복을 제거합니다  다만 중복되지 않는 단어까지 잘려나가서 이부분은 해결하지 못했습니다

for j in new_word :
    j = j.capitalize()
    if Result == "" :
    
       Result = j 
        
    else :
    
        Result = Result+" "+j
print(Result)

        
        

