score = list(map(int, input("컴마와 띄어쓰기를 구분으로 점수를 입력하세요 : ").split(", ")))
avg = int(sum(score)/len(score))
print("학점의 평균은 :",round(avg,0))