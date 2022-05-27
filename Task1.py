some_list = [111, 'string', (222, 'more_string')]
for element in some_list:
    # +1 по index сделано для удобства восприятия
    print(f'Value {element} on position {some_list.index(element) + 1} has', type(element))
