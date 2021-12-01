pattern = "abba"
input_string ="foo foo foo foo"
list_pattern = list(pattern)
print(list_pattern)
list_string = list(input_string.split(" "))
print(list_string)
result = dict(zip(list_pattern,list_string))
print(result)
judge =(len(list_string))/len(result)
print(judge)
seen = []
true_result = dict()
if judge == len(result):
        for key,val in result.items():
                if val not in seen:
                        seen.append(val)
                        true_result[key] = val
                        if true_result == result :
                                print("true")
                        else:
                                print("false")
else:
        print("false")

