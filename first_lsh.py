score_data = input("점수 : ")

score_data = score_data.split(",")
score_sum = 0

for i in score_data:
    score_sum += int(i)

score_averege = score_sum / len(score_data)
print(round(score_averege))