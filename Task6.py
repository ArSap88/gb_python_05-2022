from itertools import count, cycle


def count_func(start_num, stop_num):
    for el in count(start_num):
        if el > stop_num:
            break
        else:
            print(el)


def cycle_func(build_in_list, iterations):
    i = 0
    iter = cycle(build_in_list)
    while i < iterations:
        print(next(iter))
        i += 1


count_func(start_num=int(input("Enter start number: ")), stop_num=int(input("Enter stop number: ")))
cycle_func(build_in_list=[1, 2, 3, 4, 5], iterations=int(input("enter iteration: ")))

# Не люблю видеть в коде какие-либо подчеркивания, но и "лишние пустые строки" не люблю.
# Да, я понимаю - читаемость кода важнее, эх...
