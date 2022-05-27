month_num = int(input('Enter number of the month: '))
seasons_list = ['winter', 'spring', 'summer', 'autumn/fall']
if 1 <= month_num <= 2 or month_num == 12:
    season = 1
elif 3 <= month_num <= 5:
    season = 2
elif 6 <= month_num <= 8:
    season = 3
elif 9 <= month_num <= 11:
    season = 4
else:
    print('Number you entered does not correspond to month.')
print(f'Month number {month_num} is in', seasons_list[season - 1])

# Через dictionary:
#
# month_num = int(input('Enter number of the month: '))
# seasons_dict = {'first': 'winter', 'second': 'spring', 'third': 'summer', 'fourth': 'autumn/fall'}
# if 1 <= month_num <= 2 or month_num == 12:
#     season = "first"
# elif 3 <= month_num <= 5:
#     season = "second"
# elif 6 <= month_num <= 8:
#     season = "third"
# elif 9 <= month_num <= 11:
#     season = "fourth"
# else:
#     print('Number you entered does not correspond to month.')
# print(f'Month number {month_num} is in', seasons_dict[season])
