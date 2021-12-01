number1, text1 = input().split()
number1 = int(number1)
text1 = str(text1)
if number1 >= 0 and number1 <= 100:
    for i in range(number1):
        print(text1, end="")
    print()