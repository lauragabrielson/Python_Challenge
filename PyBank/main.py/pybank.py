import os
import csv
import numpy as np  

#path to collect data from csv file in Resources folder
pybank_csv = os.path.join('..', 'Resources', '02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')

monthly_change = []
#define function
#def financial_analysis(pybank_data):
    # month = pybank_data[0]
    # profit = int(pybank_data[1])


    # total_months = len(month)
    # total_profit = sum(profit)

    # print(f'Total Months: {total_months}')
    # print(f'Total: {total_profit}')

# with open(pybank_csv, newline='') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=',')
#     for row in csvreader:

#         monthly_change.append

with open(pybank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    lines = csvfile.readlines()
    change = np.array(lines[1])
    np.diff(change)
    print(change)
    # total = 0
    # total_months = 0
    # average_change = 0
    # difference = 0


    # for column in csvreader:
    #     total += int(column[1])
    #     csvreader.line_num
    #     total_months += 1
        

    # print("Financial Analysis")
    # print("------------------------------------------------")
    # print("Total Months: " + str(total_months))
    # print("Total Profit: $" + str(total))
        








