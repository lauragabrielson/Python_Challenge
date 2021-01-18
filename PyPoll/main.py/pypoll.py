#import files
import os
import csv
from collections import Counter

#path to collect data from csv file in Resources folder
pypoll_csv = os.path.join('..', 'Resources', '02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')

#read lines and count votes for each candidate
with open(pypoll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    lines = [line for line in csvreader]
    votes = Counter([l[2] for l in lines])

    #candidate = votes.keys()
 #extract candidate votes from dictionary
    cand1 = (votes["Khan"])
    cand2 = (votes["Correy"])
    cand3 = (votes["Li"])
    cand4 = (votes["O'Tooley"])

#calculate the winner and total votes
    winner = votes.most_common(1)[0][0]
    total_votes = cand1 + cand2 + cand3 + cand4

#calculate candidate percentages
    cand1_percent = round(cand1 / total_votes * 100)
    cand2_percent = round(cand2 / total_votes * 100)
    cand3_percent = round(cand3 / total_votes * 100)
    cand4_percent = round(cand4 / total_votes * 100)
   
 #print results
    print("Election Results")
    print("-------------------------")
    print(f'Total Votes: {total_votes}')
    print("-------------------------")
    print(f'Khan:  {cand1_percent}.000%   ({cand1})')
    print(f'Correy:  {cand2_percent}.000%   ({cand2})')
    print(f'Li:  {cand3_percent}.000%   ({cand3})')
    print(f"O'Tooley:  {cand4_percent}.000%   ({cand4})")
    print("-------------------------")
    print(f'Winner: {winner}')
    print("-------------------------")


#write files

    f = open("pypoll_analysis.txt", "w")
    
    f.write("Election Results")
    f.write("-------------------------")
    f.write(f'Total Votes: {total_votes}')
    f.write("-------------------------")
    f.write(f'Khan:  {cand1_percent}.000%   ({cand1})')
    f.write(f'Correy:  {cand2_percent}.000%   ({cand2})')
    f.write(f'Li:  {cand2_percent}.000%   ({cand2})')
    f.write(f"O'Tooley:  {cand3_percent}.000%   ({cand3})")
    f.write("-------------------------")
    f.write(f'Winner: {winner}')
    f.write("-------------------------")       

    