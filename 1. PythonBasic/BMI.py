# Body Mass Index Measurement(BMI) calculator
# BMI = weight/height**2

# take user weight as input in kg
weight = eval(input("Enter weight of the person:"))

# take user height as input in meter
Height = eval(input("Enter the height of the person:"))

BMI = int(weight / (Height ** 2))

print('BMI of the user is ',BMI)