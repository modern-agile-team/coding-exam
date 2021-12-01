input_pattern = list(input())  # 패턴 입력 받기
input_string = list(input().split())  # 문자열 입력 받기

# 입력 받은 문자열을 입력 받은 패턴에 하나씩 대입하기
# 패턴문자 같은 것끼리 값 비교하기 => 같은 패턴문자에 있는 값이 같은지
# 패턴문자 다른 것끼리 값 비교하기 => 각 패턴문자에 있는 값이 다른지
# 위에서 비교한 값으로 결과내기

# {
#     "a":[],
#     "b":[]
#     }


result_pattern = dict()
for i in input_pattern:
    if i not in result_pattern:
        result_pattern[i] = []

for i in input_string:
    result_pattern[i].append(i)
print(result_pattern)
