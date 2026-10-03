def getLetterGrade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

studentName = input("Enter student name: ")

grades = []

grade1 = float(input("Enter grade 1: "))
grade2 = float(input("Enter grade 2: "))
grade3 = float(input("Enter grade 3: "))
grade4 = float(input("Enter grade 4: "))
grade5 = float(input("Enter grade 5: "))

grades.append(grade1)
grades.append(grade2)
grades.append(grade3)
grades.append(grade4)
grades.append(grade5)

average = sum(grades) / len(grades)

letterGrade = getLetterGrade(average)

print()
print(studentName)
print("Average:", average)
print("Letter Grade:", letterGrade)