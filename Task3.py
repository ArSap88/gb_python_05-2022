employers_file = open('Task3_file.txt', 'r', encoding='utf-8')
database = employers_file.readlines()
salary_sum = 0
employers_names = []
for string in database:
    line_split = string.split()
    salary_sum += float(line_split[1])
    if float(line_split[1]) < 20000.00:
        employers_names.append(line_split[0])
print('Employers with low salary: ', ', '.join(employers_names), '\nAverage salary: ', salary_sum/len(database))
employers_file.close()
