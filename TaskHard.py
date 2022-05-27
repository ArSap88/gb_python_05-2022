goods_db = []
db_dict = {}
goods_analysis_dict = {'Name': [], 'Price': [], 'Quantity': [], 'M.u.': []}
user_start_choice = input('Add some data to database? y/n: ')
if user_start_choice == 'y':
    count = 1
    how_many = int(input('How many positions? '))
    while count <= how_many:
        db_dict = ({'Name': input('Enter name: '), 'Price': int(input('Enter price: ')),
                    'Quantity': int(input('Enter quantity: ')), 'M.u.': input('Enter m.u.: ')})
        goods_db.append((count, db_dict))
        for key in db_dict.keys():
            goods_analysis_dict[key].append(db_dict[key])
        count += 1
    analyze_maybe = input('See some analysis? y/n ')
    if analyze_maybe == 'y':
        for key in goods_analysis_dict.keys():
            print(key, ':', goods_analysis_dict[key])
    elif user_start_choice == 'n':
        print('Goodbye.')
    else:
        print('Wrong input.')
elif user_start_choice == 'n':
    print('Goodbye.')
else:
    print('Wrong input.')
