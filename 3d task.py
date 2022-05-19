user_input_n = int(input('Enter number: '))
double_n = int(str(user_input_n) + str(user_input_n))
triple_n = int(str(user_input_n) + str(user_input_n) + str(user_input_n))
summary = user_input_n + double_n + triple_n
print(f'{user_input_n} + {double_n} + {triple_n} = {summary}')