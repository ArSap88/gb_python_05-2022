given_list = [30, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_list = [el for el in given_list if el > given_list[given_list.index(el)-1]]
print(f'Task: {given_list}; \nResult: {result_list}')
