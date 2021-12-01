from first import solution
def solution(strList):
    pattern = strList[0]
    inStr = strList[1]

    for i,j in  zip(pattern, inStr.split()):
        print(i,j)
if __name__ == "__main__":
    list1 = ['abba', 'foo bar bar foo']
    print(solution(list1))
