user_input = int(input('Please enter a number (seconds) to convert in minutes and hours: '))
hours = user_input // 3600
minutes = (user_input % 3600) // 60
seconds = (user_input % 3600) % 60
print(f'{hours}:{minutes}:{seconds}')
