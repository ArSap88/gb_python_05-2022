def user_info_dict(**user_data):
    for key, value in user_data.items():
        print(f'{key} is {value};', end=' ')
user_info_dict(Firstname="Arman", Lastname="S", Email="example@example.com", Country="KZ", Age=33, Phone=123)
