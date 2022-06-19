test_file = open('test_file.txt', 'w+')
user_input = True
while user_input:
    user_input = input("Enter text: ")
    text = [user_input, '\n']
    test_file.writelines(text)
    if not user_input:
        break
test_file.close()
