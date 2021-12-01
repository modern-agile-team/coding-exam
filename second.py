input_arr = input().split(", ")
input_arr[0] = input_arr[0][1:]
input_arr[-1] = input_arr[-1][:-1]

arr = []
for i in input_arr:
    i = int(i)
    arr.append(i)

result = [min(arr), sum(arr), max(arr)]

print(result)
