user_input = int(input('Enter number: '))
my_list = [7, 5, 3, 2]
max_num = max(my_list)
min_num = min(my_list)
list_length = len(my_list)
if user_input > max_num:
    my_list.insert(0, user_input)
elif user_input < min_num:
    my_list.insert(list_length, user_input)
elif user_input in my_list:
    my_list.insert(my_list.index(user_input), user_input)
else:
    my_list.append(user_input)
print(my_list)
