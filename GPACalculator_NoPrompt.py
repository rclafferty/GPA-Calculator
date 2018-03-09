# Get the initial number of courses
# numCourses = (int)(input("Enter the number of courses: "))
numCourses = (int)(input())

# Declare variables to be used in the loop
totalHours = 0
totalCredits = 0
courseNames = []
courseHours = []
courseGrades = []

# Iterate through each course
for x in range(0,numCourses):
	# Get the course name
	courseName = input()
	courseNames.append(courseName)
	
	# Get the number of credit hours as an integer
	hours = (int)(input())
	courseHours.append(hours)
	totalHours += hours

	# Get the letter grade of the course
	grade = input()
	courseGrades.append(grade)
	totalCredits += (4 - (ord(grade) - ord('A'))) * hours
		# Ex: If the letter grade is B,
		# 	'B' - 'A' = 1
		#	4 - 1 = 3
		#	B = 3.0 credit

# Calculate GPA
gpa = totalCredits / totalHours

# Print all course
print("\nCourse Report:")
for x in range(0, numCourses):
	print("----------------------")
	print("Course: ", courseNames.pop(0))
	print("Hours:  ", courseHours.pop(0))
	print("Grade:  ", courseGrades.pop(0))

print("======================")
# Print GPA
print("Your gpa is: ", str(round(gpa,2)))