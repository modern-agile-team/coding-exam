score = input().split(',')
n = len(score)
score = map(int, score)
print(round(sum(score)/n))
