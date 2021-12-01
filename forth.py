n = list(input("n: "))
m = list(input("m: "))



if len(n)==len(m):
    print("n은 m보다 크거나 작아야 합니다.")
elif len(n)<len(m):
    for i in range(len(m)):
        c = n[i]
        lst = []
        for pos,char in enumerate(m):
            if(char == c):
                lst.append(pos)
    print(lst)
else :
    for i in range(len(n)):
        c = m[i]
        lst = []
        for pos,char in enumerate(n):
            if(char == c):
                lst.append(pos)
    print(lst)