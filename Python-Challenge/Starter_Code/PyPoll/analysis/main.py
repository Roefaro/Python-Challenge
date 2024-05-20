# PyPoll helps a small, rural town modernize its vote-counting process using Python. Given poll data (election_data.csv) with three columns: "Voter ID", "County", and "Candidate", the script calculates:

# Total number of votes cast
# Complete list of candidates who received votes
# Percentage of votes each candidate won
# Total number of votes each candidate won
# Winner of the election based on popular vote

# Dependencies
import os
import csv

# file path
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

#Create lists to store data
total_votes = 0
candidates = []
votes = []
percentages = []

# open and read the csv file
with open(csvpath) as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
    
    # skip the header row
    csv_header = next(csvreader)
    
    # loop through the data
    for row in csvreader:
        # calculate total votes
        total_votes += 1
        # calculate candidates
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            votes.append(1)
        else:
            index = candidates.index(row[2])
            votes[index] += 1

    # calculate percentages
    for vote in votes:
        percentage = (vote/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percentages.append(percentage)
    
    # calculate the winner
    winner = max(votes)
    index = votes.index(winner)
    winning_candidate = candidates[index]

    # print results
    print("Election Results")
    print("------------------------")
    print(f"Total Votes: {total_votes}")
    print("------------------------")
    for i in range(len(candidates)):
        print(f"{candidates[i]}: {percentages[i]} ({votes[i]})")
    print("------------------------")
    print(f"Winner: {winning_candidate}")
    print("------------------------")

# output to a text file
output_file = os.path.join('..', 'analysis', 'election_results.txt')
with open(output_file, "w") as file:
    file.write("Election Results\n")
    file.write("------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("------------------------\n")
    for i in range(len(candidates)):
        file.write(f"{candidates[i]}: {percentages[i]} ({votes[i]})\n")
    file.write("------------------------\n")
    file.write(f"Winner: {winning_candidate}\n")
    file.write("------------------------\n")

# Path: Starter_Code/PyPoll/analysis/main.py
# Compare this snippet from Starter_Code/PyBank/analysis/main.py:
#     total_months = 0
#     total_profit = 0
#     monthly_profit_change = []
#     month_count = []
#     greatest_increase = ["", 0]
#     greatest_decrease = ["", 9999999999999999999]
#     net_total = 0
#     previous_net = 0
#     net_change = 0
#     net_change_list = []
#     average_change = 0

#     # loop through the data
#     for row in csvreader:
#         # calculate total months
#         total_months += 1
#         # calculate total profit
#         net_total += int(row[1])
#         # calculate net change
#         net_change = int(row[1]) - previous_net
#         previous_net = int(row[1])
#         net_change_list += [net_change]
#         month_count += [row[0]]
#         # calculate greatest increase
#         if net_change > greatest_increase[1]:
#             greatest_increase[0] = row[0]
#             greatest_increase[1] = net_change
#         # calculate greatest decrease
#         if net_change < greatest_decrease[1]:
#             greatest_decrease[0] = row[0]
#             greatest_decrease[1] = net_change
    

