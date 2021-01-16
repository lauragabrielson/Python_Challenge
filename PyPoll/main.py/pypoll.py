import os
import csv
from collections import Counter

#path to collect data from csv file in Resources folder
pypoll_csv = os.path.join('..', 'Resources', '02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')

with open(pypoll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    lines = [line for line in csvreader]
    counts = Counter([l[2] for l in lines])
    Khan = (counts["Khan"])
    Correy = (counts["Correy"])
    Li = (counts["Li"])
    Tooley = (counts["O'Tooley"])
    winner = counts.most_common(1)[0][0]

    total_votes = Khan + Correy + Li + Tooley
    Khan_percent = round(Khan / total_votes * 100)
    Correy_percent = round(Correy / total_votes * 100)
    Li_percent = round(Li / total_votes * 100)
    Tooley_percent = round(Tooley / total_votes * 100)


    print("Election Results")
    print("-------------------------")
    print(f'Total Votes: {total_votes}')
    print("-------------------------")
    print(f'Khan:  {Khan_percent}.000%   ({Khan})')
    print(f'Correy:  {Correy_percent}.000%   ({Correy})')
    print(f'Li:  {Li_percent}.000%   ({Li})')
    print(f"O'Tooley:  {Tooley_percent}.000%   ({Tooley})")
    print("-------------------------")
    print(f'Winner: {winner}')
    print("-------------------------")


    f = open("pypoll_analysis.txt", "w")
    
    f.write("Election Results")
    f.write("-------------------------")
    f.write(f'Total Votes: {total_votes}')
    f.write("-------------------------")
    f.write(f'Khan:  {Khan_percent}.000%   ({Khan})')
    f.write(f'Correy:  {Correy_percent}.000%   ({Correy})')
    f.write(f'Li:  {Li_percent}.000%   ({Li})')
    f.write(f"O'Tooley:  {Tooley_percent}.000%   ({Tooley})")
    f.write("-------------------------")
    f.write(f'Winner: {winner}')
    f.write("-------------------------")       