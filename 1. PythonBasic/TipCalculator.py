# Tip Calculator
print("Welcome to the Tip Calculator!")

total_bill = eval(input("What is the total bill? $ "))

percentage_tip = eval(input('What percentage tip would you like to give? 10, 12 or 15?'))

people = int(input("how many people splitting the bill?"))

Each_personPay = round((((total_bill*percentage_tip)/100)+total_bill)/people, 2)

print(f"Each person should pay {Each_personPay}$ for {percentage_tip } percentage tip.")