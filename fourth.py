N, M = input().split(" M")
N = N[5:-1]
M = M[4:-1]

result = 0

for i in range(len(M)):
    if M[i] in N:
        result += i

print(result)
