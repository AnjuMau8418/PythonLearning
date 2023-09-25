# Love Calculator

print("Welcome! to the Love Calculator!")
name1 = input('What is your name?')
name2 = input("What is your curse name?")
combine_string = name1 + name2
lower_case_string = combine_string.lower()

T = lower_case_string.count('t')
R = lower_case_string.count('r')
U = lower_case_string.count('u')
E = lower_case_string.count('e')
TRUE = (T + R + U + E)

L = lower_case_string.count('l')
O = lower_case_string.count('o')
V = lower_case_string.count('v')
E = lower_case_string.count('e')
LOVE = (L + O + V + E)

Love_Score = int(str(TRUE) + str(LOVE))
if Love_Score < 10 or Love_Score > 90:
    print(f"your Love score is {Love_Score}, you go together like coke and mentos.")
elif 40 < Love_Score < 50:
    print(f"your Love score is {Love_Score}, you are alright together.")
else:
    print(f"Your Love score is {Love_Score}.")
