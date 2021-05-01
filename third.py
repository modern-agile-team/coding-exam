while(1):
    n = int(input("데이터 개수는? : "))
    if(n>=1)&(n<=100):
        break
    else :
        print("데이터 개수를 다시 입력해주세요")
ns = []
name = []
sex = []
name_sex={}
for i in range(n):
    ns.append((input("이름과 성별을 입력해주세요 : ")).split(" "))
for h in range(n):
    name.append(ns[h][0])
    sex.append(ns[h][1])
for k in range(n):
    name_sex[name[k]]=sex[k]
print(name_sex)
    



