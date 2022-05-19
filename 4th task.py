user_input = int(input('Enter random even positive number: '))
max_digit = 0
while user_input > 0:
    digit = user_input % 10
    if max_digit < digit:
        max_digit = digit
    user_input //= 10
print(f'Biggest digit is: {max_digit}')
