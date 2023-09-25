# Find Average of student's height
student_height = input("input a list of student height:").split()

sum = 0
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
    sum = sum + student_height[n]

print("Students height:", student_height)
print("Sum: ", sum)

number_student = 0
for student in student_height:
    number_student += 1
print("Number of students :",number_student)

Average = sum / number_student

print("Average: ", round(Average))
