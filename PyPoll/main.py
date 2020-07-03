import os
import csv

PyPollcsv = os.path.join("Resources","election_data.csv")

count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []
with open(PyPollcsv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:

        count = count + 1

        candidatelist.append(row[2])
    for c in set(candidatelist):
        unique_candidate.append(c)
        # V is the total number of votes per candidate
        V = candidatelist.count(c)
        vote_count.append(V)
        # P is the percent of total votes per candidate
        P = (V/count)*100
        vote_percent.append(P)

    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]
 
print("***********************************************************************************************")
print("Election Results")   
print("**********************************************************************************************")
print("Total Votes :" + str(count))    
print("**********************************************************************************************")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
print("**********************************************************************************************")
print("The winner is: " + winner)
print("***********************************************************************************************")



with open('election_results.txt', 'w') as text:
    text.write("*********************************************************************************\n")
    text.write("Election Results\n")
    text.write("**********************************************************************************\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("**********************************************************************************\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("*************************************************************************************\n")
    text.write("The winner is: " + winner + "\n")
    text.write("***************************************************************************************\n")
