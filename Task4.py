user_input = input('Enter some words divided by "space": ').split(' ')
for str_num, word in enumerate(user_input):
    print(str_num + 1, word[0:10])
