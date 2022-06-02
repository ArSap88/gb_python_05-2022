'''
Не соображу как сделать вывод красивее, но работает:

def capitalization_func(some_string):
    words = some_string.split(' ')
    output = []
    for i in words:
        letters = str(i)
        first_letter = letters[:1].upper()
        word = first_letter + letters[1:]
        output.append(word)
    return output
print(capitalization_func(input('Enter words: ')))

Однако используя .title получается намного лучше ->
'''

def capitalization_func(some_string):
    return some_string.title()
print(capitalization_func(input('Enter words: ')))
