# main.py for PyBank assignment

# importing csv module 
import csv 
import os


budget_data = "budget_data.csv"


# budget_data = os.path.join("..", "PyBank", "budget_data.csv")


# Store the values we need to print
max_loss = 0
max_profit = 0
current_value = 0
total_value = 0
ave_value = 0
month_max_decrease = ()
month_max_increase = ()
month_count = 0
change = 0
prior_row_amount = 0
prior_max_increase = 0
prior_max_decrease = 0


# Read in the CSV file and print the header
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
   

    csv_header = next(csvfile)

    for row in csvreader:
    
 #      print(row[0], row[1])
        total_value = float(row[1]) + float(total_value)
        row_amount = float(row[1])
        row_month = row[0]
        month_count = month_count + 1
        change = int(row_amount) - int(prior_row_amount)
        # append change to list of increases and decrease so we can sum and avergage them
        
        
        if int(change) < int(prior_max_decrease):
            max_decrease = change
            month_max_decrease = row_month
        if int(change) > int(prior_max_increase):
            max_increase = change
            month_max_increase = row_month
        prior_row_amount = row_amount

    

    total_value = int(total_value)
    
    # Print out the required budget data 
    
    print(f"Functional Analysis") 
    line1 ="Functional Analayis"
    print(f"____________________________________")
    line2 = "____________________________________"
    print(("Total_Months: "), str(month_count))
    line3 = "Total_Months: " + str(month_count)
    print(("Total: $" ), str(total_value)) 
    line4 = "Total: $"  + str(total_value) 
    print(("Average: $" ), str(total_value/month_count))
    line5 = "Average: $"  + str(total_value/month_count)
    max_increase = int(max_increase)
    max_increase = "$(" + str(max_increase) + ")"
    print(("Greatest Increase in Profits: "), month_max_increase, max_increase)
    line6 = "Greatest Increase in Profits: " + str(month_max_increase) + str(max_increase)
    max_decrease = int(max_decrease)
    max_decrease = "$(" + str(max_decrease) + ")"
    print(("Greatest Decrease in Profits: "), month_max_decrease, max_decrease)
    line7 = "Greatest Decrease in Profits: " + str(month_max_decrease) + str(max_decrease)



# print to output file
output_file = "/Users/suevalverde/GWUB/python-challenge/PyBank/PyBank_output.txt"
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
datafile.close()
    


  
