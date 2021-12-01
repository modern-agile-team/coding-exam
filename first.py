def solution(n, inStr):
    return n * inStr

if __name__ == "__main__":
    ls = input().split()
    print(solution(int(ls[0]), ls[1]))