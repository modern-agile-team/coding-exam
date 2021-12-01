# abba
# foo bar bar foo
text1 = list(input())
text2 = input().split()

# text1 = set(text1)
print(text1)
print(text2)

for i in range(len(text1)):
    if text1[i] == "a":
        text1[i] = 1
    else:
        text1[i] = 0

for i in range(len(text2)):
    if text2[i] == "foo":
        text2[i] = 1
    else:
        text2[i] = 0
print(text1)

print(text2)
if (text1 == text2):
    print(True)
else:
    print(False)
