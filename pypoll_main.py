# main.py for the PyPoll assignment
import os
import csv

election_data = 'election_data.csv'


# Store the values we need to print
total_votes = 0
total_votes_khan = 0
total_votes_correy = 0
total_votes_li = 0
total_votes_otooley = 0
percent_khan = 0
percent_correy = 0
percent_li = 0
percent_otooley = 0
name = ()
winner = ()

# Read in the CSV file and print the header
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    
    title = next(csvfile)
    csv_header = next(csvfile)

# Determione the total number of votes each candidate won

    for row in csvreader:

        total_votes = int(total_votes) + 1
        name = row[2]
#       print(name)
        if name == "Khan":
            total_votes_khan = int(total_votes_khan) + 1
        if name == "Correy":
            total_votes_correy = int(total_votes_correy) + 1
        if name == "Li":
            total_votes_li = int(total_votes_li) + 1
        if name == "O'Tooley":
            total_votes_otooley = int(total_votes_otooley) + 1

# Determine the percentage of votes that each candidate won
percent_khan = (total_votes_khan / total_votes) * 100
percent_khan = round(percent_khan,4)
percent_correy = (total_votes_correy / total_votes) * 100
percent_correy = round(percent_correy,4)
percent_li = (total_votes_li / total_votes) * 100
percent_li = round(percent_li,4)
percent_otooley = (total_votes_otooley / total_votes) * 100
percent_otooley = round(percent_otooley,4)
        
#  Determine the winner of the election based on the popular vote
winner = "Khan"

# Print out the required budget data 




print(f"Election Results") 
line1 ="Election Results"
print(f"____________________________________")
line2 = "____________________________________"
print("Total Votes: " , total_votes)
line3 = "Total Votes: " + str(total_votes)
print("______________________________________")
line4 = "_____________________________________"
print(("Khan: "), str(percent_khan) + "% ", "(" + str(total_votes_khan) + ")")
line5 = "Khan: " + str(percent_khan) + "% " + "(" + str(total_votes_khan) + ")"
print(("Correy: "), str(percent_correy) + "%", "(" + str(total_votes_correy) +")")
line6 = "Correy: " + str(percent_correy) + "% "  + "(" + str(total_votes_correy) + ")"
print(("Li: "), str(percent_li) + "% "  + "(" + str(total_votes_li) + ")")
line7 = "Li: " + str(percent_li) + "% " +  "(" + str(total_votes_li) + ")"
print(("O'Tooley: "), str(percent_otooley) +"%", "(" + str(total_votes_otooley) + ")")
line8 = "O'Tooley: " + str(percent_otooley) + "% " + "(" + str(total_votes_otooley) + ")"
print(f"_______________________________________")
line9 = "_______________________________________"
print("Winner: " + "Khan")
line10 = "Winner: " + "Khan"
print("______________________________________")
line11 = "_____________________________________"




# print to output file
output_file = "/Users/suevalverde/GWUB/python-challenge/PyPoll/PyPoll_output.txt"
with open(output_file, "wt") as datafile:
    n = datafile.write(line1)
    n = datafile.write("\n")
    n = datafile.write(line2)
    n = datafile.write("\n")
    n = datafile.write(line3)
    n = datafile.write("\n")
    n = datafile.write(line4)
    n = datafile.write("\n")
    n = datafile.write(line5)
    n = datafile.write("\n")
    n = datafile.write(line6)
    n = datafile.write("\n")
    n = datafile.write(line7)
    n = datafile.write("\n")
    n = datafile.write(line8)
    n = datafile.write("\n")
    n = datafile.write(line9)
    n = datafile.write("\n")
    n = datafile.write(line10)
    n = datafile.write("\n")
    n = datafile.write(line9)

    datafile.close()





