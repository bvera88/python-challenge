import os

import csv

dir_path = os.path.dirname(os.path.realpath(__file__))

pypollpath = os.path.join(dir_path, "PyBank.csv")

with open(pypollpath) as csvfile:

    csvreader = csv.reader(csvfile)

    next(csvreader)
    total_months = 0
    total_sum = 0
    change = 0
    avg_list = []
    previous = 0
    max_change = ["",0]
    min_change = ["",9999]

    
    for x in csvreader:
        total_months = total_months + 1
        total_sum = total_sum + int(x[1])
        change = int(x[1]) - previous
        previous = int(x[1])
        avg_list = avg_list + [change]
        length = len(avg_list) - 1
        if change > max_change[1]:
            max_change[0] = x[0]
            max_change[1] = change
        if change < min_change[1]:
            min_change[0] = x[0]
            min_change[1] = change
    
    total_avg = sum(avg_list[1:])/length

    Header = "Financial Analysis"
    Ttl_months = "Total Months: " + str(total_months)
    Ttl = "Total: " + str(total_sum)
    Avg_Change = "Average Change: " + str(total_avg)
    Greatest_increase = "Greatest Increase in Profits: " + str(max_change[0]) + " " + str(max_change[1])
    Greatest_decrease = "Greatest Decrease in Profits: " + str(min_change[0]) + " " + str(min_change[1])

    PybankAssignment = open(os.path.join(dir_path, "PBAssignment.txt"), 'w')

    print(Header)
    print(Ttl_months)
    print(Ttl)
    print(Avg_Change)
    print(Greatest_increase)
    print(Greatest_decrease)

    PybankAssignment.write(Header + "\n")
    PybankAssignment.write(Ttl_months + "\n")
    PybankAssignment.write(Ttl + "\n")
    PybankAssignment.write(Avg_Change + "\n")
    PybankAssignment.write(Greatest_increase + "\n")
    PybankAssignment.write(Greatest_decrease + "\n")

    PybankAssignment.close()



