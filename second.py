def time(input_time):
    output_time = []
    hour = input_time[0]+"시"
    minuite = input_time[1]+"분"
    sec = input_time[2]+"초"

    output_time.extend([hour,minuite,sec])
    return output_time
input_time = input("  :를 구분으로 시 분 초를 입력하세요 : ").split(":")
print(time(input_time))
