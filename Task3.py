def lets_find_out(first, second, third):
    list_of_ints = [first, second, third]
    max_int_1 = max(list_of_ints)
    list_of_ints.remove(max_int_1)
    max_int_2 = max(list_of_ints)
    return max_int_1 + max_int_2
print(lets_find_out(int(input('First number: ')), int(input('Second number: ')), int(input('Third number: '))))

'''
Как вариант, можно так:

def lets_find_out(first, second, third):
    list_of_ints = [first, second, third]
    output = []
    max_int_1 = max(list_of_ints)
    output.append(max_int_1)
    list_of_ints.remove(max_int_1)
    max_int_2 = max(list_of_ints)
    output.append(max_int_2)
    return sum(output)
    print(lets_find_out(int(input('First number: ')), int(input('Second number: ')), int(input('Third number: '))))
    
но первый вариант мне больше нравится.
'''