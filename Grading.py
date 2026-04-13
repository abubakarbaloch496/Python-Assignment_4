# Takes marks of 5 students, assigns grades, and finds highest marks
passed = 0
failed = 0
highest = 0

for i in range(1,6):
    marks = int(input("Enter marks: "))

    if marks > highest:
        highest = marks

    if marks >= 80:
        print("Student" + str(i) + ": A")
        passed +=1
    elif marks >= 60:
        print("Student" + str(i) + ": B")
        passed +=1
    elif marks >= 50:
        print("Student" + str(i) + ": C")
        passed +=1
    else:
        print("Student" + str(i) + ": Fail")
        failed +=1

print("Total Passed:", passed)
print("Total Failed:", failed)
print("Highest Marks:", highest)