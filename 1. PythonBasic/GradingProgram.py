# Reward grade to the student according to their scores
student_score = {"Maria": 99, "Manisha": 87, "Nida": 79, "Anand": 98, "Kajal": 45, "Prince": 82, "Mohit": 89}
student_grade = {}
for key in student_score:
    score = student_score[key]
    if 90 < score:
        student_grade[key] = "Outstanding"
    elif 80 < score:
        student_grade[key] = "Exceed Exceptions"
    elif 70 < score:
        student_grade[key] = "Acceptable"
    else:
        student_grade[key] = "Fail"

print(student_grade)