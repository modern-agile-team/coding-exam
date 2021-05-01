n = int(input("n : "))

dict_user_data = {}
for i in range(n):
    user_data = input("user_data : ")
    user_data = user_data.split(" ")
    dict_user_data[user_data[0]] = user_data[1]
print(dict_user_data)