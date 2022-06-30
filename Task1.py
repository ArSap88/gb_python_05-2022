class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        date = []

        for i in day_month_year.split():
            if i != '-':
                date.append(i)

        return int(date[0]), int(date[1]), int(date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 0:
                    return f'All right'
                else:
                    return f'Invalid year'
            else:
                return f'Invalid month'
        else:
            return f'Invalid day'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


current_date = Data('11 - 1 - 2001')
print(Data.valid(11, 11, 2050))
print(current_date.valid(11, 13, 2011))
print(Data.extract('11 - 11 - 2011'))
print(current_date.extract('11 - 11 - 2020'))
print(Data.valid(1, 11, 2000))
