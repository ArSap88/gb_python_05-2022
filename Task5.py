def strange_func():
    output = 0
    continue_condition = True
    while continue_condition:
        input_list = input('Enter numbers split by space (any other symbol will exit the program): ').split(' ')
        for i in range(len(input_list)):
            try:
                int(input_list[i])
            except ValueError:
                print('Exiting program...')
                continue_condition = False
            else:
                output = output + int(input_list[i])
        print(f'Sum is {output}')
strange_func()

