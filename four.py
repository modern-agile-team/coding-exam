N = input("소문자로만 이루어진 문자열을 입력해 주세요:")
M = input("소문자로만 이루어진 문자열을 입력해 주세요:")
array_N = list(N)
array_M = list(M)

sum  = 0
array_overlap = []
for i in array_M:
        if i in array_N:
                array_overlap.append(i)
#print(array_overlap)
#print(array_M)

for j in array_overlap:
        if j in array_M:
                sum += array_M.index(j)
                print(array_M)
                array_M.insert(array_M.index(j),1)
                array_M.pop(array_M.index(j))
                print(array_M)
        else:
                break;
print(sum)

