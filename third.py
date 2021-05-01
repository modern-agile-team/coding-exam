n = int(input())
my_dict = {}
for i in range(n) :
    key,val = map(str,input().split())
    my_dict[key] = val
print(my_dict)
