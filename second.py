def time(input_time):                                               #주어진 시간을 시 분 초로 변환하는 함수 생성
    output_time = []  
      
    hour = input_time[0]+"시"
    minute = input_time[1]+"분"
    sec = input_time[2]+"초"

    output_time.extend([hour,minute,sec])
    return output_time

input_time = input("  :를 구분으로 시 분 초를 입력하세요 : ").split(":")
print(time(input_time))
