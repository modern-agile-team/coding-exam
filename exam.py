def solution(phone_book):
    b_list = list(phone_book.values())
    answer = any(b_list)
    if answer == False:
        print("True")
    else:
        print("False")
    return answer