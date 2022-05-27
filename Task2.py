# Можно сделать так:
#
# some_list = input('Enter some data divided by ",": ')
# some_list = some_list.split(',')
#
# или не заморачиваться:
#
some_list = list(input('Enter some data: '))
for count in range(0, len(some_list)-1, 2):
    some_list[count], some_list[count+1] = some_list[count+1], some_list[count]
print(some_list)
