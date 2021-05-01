brandnum = {'삼성' :[],'애플' : [],'한성' : [],'레노버':[],'엘지':[],'아수스' : [],'기타': []}
num = list(map(int,input().split()))
for i in num :
    if i>=1000 and i<2000 :
        brandnum['삼성'] = [i]
    elif i>=2000 and i<3000 :
        brandnum['애플'] = [i]
    elif i>=3000 and i<4000 :
        brandnum['한성'] = [i]
    elif i>=4000 and i<5000 :
        brandnum['레노버'] = [i]
    elif i>= 5000 and i<6000 :
        brandnum['LG'] = [i]
    elif i>=6000 and i<7000 :
        brandnum['아수스'] = [i]
    else :
        brandnum['기타'] = [i]
    #딕셔너리에  value 값을 여러개를 넣어야 하는데  어떻게 해야하는지 모르겠습니다
        
        
print(brandnum)


