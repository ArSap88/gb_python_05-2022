def exponentiation_func(positive_num, negative_num):
    return 1 / positive_num ** abs(negative_num)
print(exponentiation_func(int(input('Enter positive number: ')), int(input('Enter negative number: '))))

'''
с помощью цикла:

def exponentiation_func(positive_num, negative_num):
    output = 1
    for i in range(abs(negative_num)):
        output *= positive_num
    output = 1 / output
    return output
print(exponentiation_func(int(input('Enter positive number: ')), int(input('Enter negative number: '))))

'''