import json
sum = 0
profit_counter = 0
firm_dict = {}
with open('task7.txt', 'r') as my_file:
    for line in my_file:
        firm_name, firm_type, firm_profit, firm_losses = line.split()
        firm_profit = int(firm_profit)
        firm_losses = int(firm_losses)
        firm_dict[firm_dict] = abs(firm_profit-firm_losses)
        if firm_losses < firm_profit:
            sum += firm_profit-firm_losses
            profit_counter += 1
profit_dict = {'Average profit': sum/profit_counter}
my_list = [firm_dict, profit_dict]
print(my_list)
with oper('task7.json', 'w') as my_file:
    json.dump(my_list, my_file)
