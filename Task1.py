from sys import argv
payment_calc, work_hours, salary_per_hour, bonus = argv
try:
    total = (float(work_hours) * float(salary_per_hour)) + float(bonus)
    print(f"You'll get: {total}")
except ValueError:
    print('Wrong input.')
