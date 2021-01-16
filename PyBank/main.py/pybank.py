import os
import csv
import numpy as np  

#path to collect data from csv file in Resources folder
pybank_csv = os.path.join('..', 'Resources', '02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')

revenue = []
month = []
with open(pybank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
  
    for rows in csvreader:
        revenue.append(int(rows[1]))
        month.append(rows[0])
        months = len(month)
    

    revenue_change = []
    for x in range(1, len(revenue)):
        revenue_change.append((int(revenue[x]) - int(revenue[x-1])))
       
average_change = (sum(revenue_change) / len(revenue_change))
rounded_average = round(average_change, 2)

total_revenue = sum(revenue)

    
max_change = max(revenue_change)
min_change = min(revenue_change)


max_month = (month[revenue_change.index(max(revenue_change))+1])
min_month = (month[revenue_change.index(min(revenue_change))+1])

print(f'Total Months: {months}')
print(f'Toatl: ${total_revenue}')
print(f'Average Change: ${rounded_average}')
print(f'Greatest Increase in Profits: {max_month} (${max_change})')
print(f'Greatest Decrease in Profits: {min_month} (${min_change})')


    



    