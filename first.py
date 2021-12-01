x,y = input('입력하세요:').split()
n=str(x)
setting=int(y)

for i in range(setting):
    if setting<100:
        print(n,end="")
    else:
        print("너무 많습니다.")