# Life in weeks, days and months

TotalAge = 90

currentAge = int(input("enter your age:"))

RemainingAge = TotalAge - currentAge

# Moth is a year = 12, weeks in a month =4
# weeks in a year = 52, Days in a year =365

Days = RemainingAge*365

Months = RemainingAge*12

Weeks = RemainingAge*52

print(f'You have remain {RemainingAge} years,{Months} month,{Weeks} weeks, {Days} days in your life')
