#Tip Calculator. Follow the steps below

#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Time to calculate how much tip to pay. \nAnswer the questions below to figure out what you owe")
bill_value = float(input("What was the bill value: $"))
percent_tip = int(input("What percent of the bill is needed to pay? 10, 12 or 15 percent? "))
people_n = int(input("How many people are contributing to the bill? "))

total_tip = (percent_tip/100)*bill_value
total_bill = bill_value + total_tip
bill_pp = round(total_bill / people_n,2)

print("You owe $" + str(bill_pp) + " per person")