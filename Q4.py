# -*- coding: utf-8 -*-
N = input('N = ')                   #입력 나눠서 받기
M = input('M = ')

if(len(N)<len(M) and len(N)<=50 and len(M)<=50):         # 제한조건
    result = len(N)+len(M)
    print(result)
else:
    print("error")