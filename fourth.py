def solution(strList):
    N, M = strList[0], strList[1]
    result = 0
    for idx, char in enumerate(M):
        if char in N:
            result += idx
    return result

#if __name__ == "__main__":
    #list1 = ['good', 'daood']
    #print(solution(list1))

if __name__ == "__main__":
    #list1 = ['good', 'daood']
    list2 = list(input().split())
    print(list2)
    print(solution(list2))
