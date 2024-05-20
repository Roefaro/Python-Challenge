# import the csv file
import os
import csv

# file path
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# open and read the csv file
with open(csvpath) as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
    
    # skip the header row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    # initialize variables
    total_months = 0
    total_profit = 0
    monthly_profit_change = []
    month_count = []
    greatest_increase = ["", 0]
    greatest_decrease = ["", 9999999999999999999]
    net_total = 0
    previous_net = 0
    net_change = 0
    net_change_list = []
    average_change = 0

    # loop through the data
    for row in csvreader:
        # calculate total months
        total_months += 1
        # calculate total profit
        net_total += int(row[1])
        # calculate net change
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list += [net_change]
        month_count += [row[0]]
        # calculate greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        # calculate greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

    # calculate average change
    average_change = sum(net_change_list) / len(net_change_list)

    # print results
    print("Financial Analysis")
    print("------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
    print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

    # output to text file
    output_path = os.path.join('..', 'analysis', 'financial_analysis.txt')
    with open(output_path, 'w') as file:
        file.write("Financial Analysis\n")
        file.write("------------------------\n")
        file.write(f"Total Months: {total_months}\n")
        file.write(f"Total: ${net_total}\n")
        file.write(f"Average Change: ${average_change}\n")
        file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
        file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Path: Starter_Code/PyBank/analysis/main.py
# Compare this snippet from Starter_Code/PyBank/analysis/main3.py:
# import the csv file
# import os
# import csv
