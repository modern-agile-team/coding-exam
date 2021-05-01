err=input("오류상태의 문자를 입력해주세요 : ")
err2 = (err.split(" "))
num = len(err2)
A = []
B = []
num3 = []
for i in range(num):
    num2= int(len(err2[i])/2)
    A.append(err2[i][0:num2])
    num3.append(num2)
    for j in range(num2):
        if (ord(A[i][j])>=65)&(ord(A[i][j])<=90):
            B.append(chr(ord(A[i][j])+32))
        else :
            B.append(chr(ord(A[i][j])-32))
for h in range(num-1):
    B.insert(num3[h]," ")
C = "".join(B)
print(C)

    
