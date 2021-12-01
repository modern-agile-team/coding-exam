N = 'aaba'
M = 'gfdgfa'
# >>>'aaba', 'gfdgfa' >>> 입력값
arr_string = []
for i in M:
    for j in N:
        if j == i:
            arr_string.append(j)

arr2 = set(arr_string)
arr_string = list(arr2)

count = 0
for i in range(len(M)):
    for j in arr_string:
        if M[i] == j:
            count += i

print(count)