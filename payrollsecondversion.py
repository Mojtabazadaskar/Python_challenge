import os
import csv

csvpath=os.path.join('Resources','budget_data.csv')
output=os.path.join('Resources','Report.txt')

tmonths=0
trevenue=0
revenue=[]
per_revenue=0
month_change=[]
revenue_change=0
greatest_dec=["",0]
greatest_inc=["",0]
revenue_changelist=[]
revenue_ave=[]

with open (csvpath,'r') as csvfile:
    csvreader=csv.DictReader(csvfile)
    
    
    for row in csvreader:
        
        # calculate the total months
        tmonths +=1 

        #calculate the total revenue
        trevenue += int(row["Profit/Losses"])


        revenue_change = float(row["Profit/Losses"]) - per_revenue
        per_revenue= float(row["Profit/Losses"])
        revenue_changelist=revenue_changelist +[revenue_change]
        month_change=[month_change]+[row['Date']]

        if revenue_change > greatest_inc[1]:
            greatest_inc[1]= revenue_change
            greatest_inc[0]=row['Date']

        if revenue_change < greatest_dec[1]:
            greatest_dec[1]=revenue_change
            greatest_dec[0]=row['Date']

revenue_ave=round(sum(revenue_changelist)/len(revenue_changelist),2)          


with open(output ,'w') as readme:
    readme.write("Financial Analysis \n")
    readme.write("--------------------\n")
    readme.write(" Total Months :" + str(tmonths)+ "\n" )
    readme.write(" Total Revenue: $" +str(trevenue) + "\n")
    readme.write(" Average Revenue Change : $" +str(revenue_ave)+ "\n")
    readme.write("Greatest Increase in Revenue :"+ str(greatest_inc[0])+  "($"  + str(greatest_inc[1])+")" "\n")
    readme.write("Greatest Decrease in Revenue :"+ str(greatest_dec[0]) + "($" +str(greatest_dec[1])+")" "\n")
