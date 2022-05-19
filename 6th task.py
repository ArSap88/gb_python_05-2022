km_1_day = float(input('Enter number of km on first day: '))
km_future = float(input('How much km in the end: '))
day = 1
while km_future >= km_1_day:
    km_1_day = km_1_day * 1.1
    day = day + 1
print(day)
