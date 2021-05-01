t = input("시간입력 : ")

timelst = t.split(":")
timelst = list(map(int, timelst))

if (0 <= t[0] <= 23):
    timelst.insert(1,"시")
else:
    print("다른 시간을 입력하세요.")

if (0 <= t[2] <= 59):
    timelst.insert(3,"분")
else:
    print("다른 시간을 입력하세요.")

if (0 <= t[4] <= 59):
    timelst.insert(5,"초")
else:
    print("다른 시간을 입력하세요.")


print(''.join(timelst))


