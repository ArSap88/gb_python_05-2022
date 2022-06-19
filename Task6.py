task6_file = open('task6_file', 'w', encoding='utf=8')
data_dict = {}
for string in task6_file:
    string = string.split(':')
    data_dict[string[0]] = string[1]
task6_file.close()
for key in data_dict:
    sum = 0
    data_dict[key] = data_dict[key].split()
    for i in range(len(data_dict[key])):
        for char in data_dict[key][i]:
            if char not in '0123456789':
                data_dict[key][i] = data_dict[key][i].replace(char, '')
            try:
                sum += int(data_dict[key][i])
            except:
                continue
    data_dict[key] = sum
print(data_dict)
