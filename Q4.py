# -*- coding: utf-8 -*-
N = input('N = ')                   #�Է� ������ �ޱ�
M = input('M = ')

if(len(N)<len(M) and len(N)<=50 and len(M)<=50):         # ��������
    result = len(N)+len(M)
    print(result)
else:
    print("error")