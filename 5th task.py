revenue = int(input('Enter revenue: '))
costs = int(input('Enter costs: '))
if revenue > costs:
    profit = (revenue - costs)
    profitability = profit / revenue
    print(f'Profit is {profit}. Profitability = {profitability}')
    employees = int(input('Enter number of employees: '))
    print(f'Profit per employee: {profit / employees}')
elif revenue == costs:
    print('Zero work.')
else:
    print('Loss...')
