translation_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
initial_file = open('Task4_file.txt', 'r', encoding='utf-8')
translated_file = open('Task4_tr.txt', 'w', encoding='utf-8')
for string in initial_file:
    string = string.split(' - ')
    string[0] = translation_dict[string[0]]
    string = ' - '.join(string)
    translated_file.write(string)
initial_file.close()
translated_file.close()