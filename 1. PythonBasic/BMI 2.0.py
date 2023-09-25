# BMI Calculator

# user weight in kg
user_weight = eval(input("Enter the user weight: "))

# user height in meter
user_height = eval(input("Enter the user height: "))

BMI = round(user_weight / user_height**2 , 2)
print("BMI :", BMI)

if BMI < 18.5:
    print("user is underweight.")
elif 18.5 < BMI < 25 :
    print("User has a normal weight.")
elif 25 < BMI < 30 :
    print("User is overweight.")
elif 30 < BMI < 35 :
    print("User is Obese.")
elif BMI > 35 :
    print("user is Clinically Obese.")



