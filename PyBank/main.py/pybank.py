import os
import csv 

#path to collect data from csv file in Resources folder
pybank_csv = os.path.join('..', 'Resources', '02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')

#create lists for revenue and month
revenue = []
month = []

#open csv
with open(pybank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    

 #add to lists and determine months 
    for rows in csvreader:
        revenue.append(int(rows[1]))
        month.append(rows[0])
        months = len(month)
    
#calculate monthly revenue change
    revenue_change = []
    for row in range(1, len(revenue)):
        revenue_change.append((int(revenue[row]) - int(revenue[row-1])))

#cancluate average change and round at 2 decimals      
average_change = (sum(revenue_change) / len(revenue_change))
rounded_average = round(average_change, 2)

#calculate total revenue
total_revenue = sum(revenue)

#find the greatest increase and greatest decrease values   
max_change = max(revenue_change)
min_change = min(revenue_change)

#establish the months correstponding to greatest increase and decrease
max_month = (month[revenue_change.index(max(revenue_change))+1])
min_month = (month[revenue_change.index(min(revenue_change))+1])

#print summary
print("Financial Analysis")
print("---------------------------------")
print(f'Total Months: {months}')
print(f'Toatl: ${total_revenue}')
print(f'Average Change: ${rounded_average}')
print(f'Greatest Increase in Profits: {max_month} (${max_change})')
print(f'Greatest Decrease in Profits: {min_month} (${min_change})')


    



    