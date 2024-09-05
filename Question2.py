#Advanced List Methods and Identity Operators

#Problem Statement: You have two lists of student names. One list contains the names of students who have submitted their assignments, and the other list contains the names of students who attended the last class.

#Task 1: Given the two lists:

# submitted = ["Alice", "Bob", "Charlie", "David"]
# attended = ["Charlie", "Eve", "Alice", "Frank"]
# Find out if Alice submitted their assignment and attended class. HINT: How might the in keyword be of use here? 
# And how can you check to see if Alice is in both submitted and attended in one if statement?

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

student = "Alice"

if student in submitted and student in attended:
    print(f"{student} submitted the assignment and attended class.")
elif student in submitted or student in attended:
    print(f"{student} either didn't attend class or submit the assignment.")
else:
    print(f"{student} didn't attend class or submit the assignment.")