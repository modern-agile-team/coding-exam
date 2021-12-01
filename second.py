def solution(ls):
    min_element = min(ls)
    sum_total = sum(ls)
    max_element = max(ls)
    return [min_element, sum_total, max_element]


if __name__ == "__main__":
    input_ls = list(map(int, input().split()))
    print(solution(input_ls))
