import os
import csv

csvpath=os.path.join('Pybank','Resources','budget_data.csv')

Profit = []
Monthly_Changes= []
Date = []

Count = 0
Total_Profit = 0
Total_Change_Profit = 0
Initial_Profit = 0
with open (csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        Count = Count + 1
        Date.append(row[0])
        Profit.append(row[1])
        Total_Profit = Total_Profit + int(row[1])
        Final_Profit = int(row[1])
        Monthly_Changes_Profits = Final_Profit - Initial_Profit
        Monthly_Changes.append(Monthly_Changes_Profits)
        Total_Change_Profit = Total_Change_Profit + Monthly_Changes_Profits
        Initial_Profit = Final_Profit
        Average_Change_Profits = (Total_Change_Profit/Count)

        Greatest_Increase_Profits = max(Monthly_Changes)
        Greatest_Decrease_Profits = min(Monthly_Changes)

        Increase_Date = Date[Monthly_Changes.index(Greatest_Increase_Profits)]
        Decrease_Date = Date[Monthly_Changes.index(Greatest_Decrease_Profits)]

    print("*******************************************************************")
    print("Financial Analysis")
    print("*******************************************************************")
    print("Total Months: " + str(Count))
    print("Total Profits: " + "$" + str(Total_Profit))
    print("Average Change: " + "$" + str(int(Average_Change_Profits)))
    print("Greatest Increase in Profits: " + str(Increase_Date) + "( $ " + str(Greatest_Increase_Profits),")")
    print("Greatest Decrease in Profits: " + str(Decrease_Date) + "( $ " + str(Greatest_Decrease_Profits),")")
    print("*********************************************************************")
    
with open("bankresults.tex", "w") as text:
    text.write("**************************************************************** \n")
    text.write("  Financial Analysis" + "\n")
    text.write("****************************************************************\n\n")
    text.write(" Total Months: " + str(Count) + "\n")
    text.write(" Total Profits: " + "$" + str(Total_Profit) + "\n")
    text.write(" Average Change:  " + "$" + str(int(Average_Change_Profits)) + "\n" )
    text.write(" Greatest Increase in Profits: " + str(Increase_Date) + " ( $" + str(Greatest_Increase_Profits) + "\n" )
    text.write(" Greatest Decrease in Profits: " + str(Decrease_Date) + " ( $" + str(Greatest_Decrease_Profits) + "\n")
    text.write("***************************************************************\n")
