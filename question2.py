'''
Here's a challenging programming problem that will test your 
knowledge of both list comprehension and dictionary comprehension:

Problem: Analyze Student Scores
You have a list of student records, where 
each record is a dictionary containing the student's name, 
a list of their scores, and their grade level. 
You need to perform the following tasks:

Calculate the average score for each student and store the 
result in a dictionary where the key is the student's name 
and the value is their average score.
Identify students with an average score above a certain threshold (e.g., 75) 
and store them in a dictionary where the key is the student's name 
and the value is their grade level.
Group students by grade level and calculate the average score for 
each grade level. Store the result in a dictionary where 
the key is the grade level and the value is the average score of 
all students in that grade level.
Here's the sample data structure:

python
Copy code
students = [
    {"name": "Alice", "scores": [85, 78, 92], "grade": 10},
    {"name": "Bob", "scores": [89, 76, 84], "grade": 11},
    {"name": "Charlie", "scores": [65, 70, 72], "grade": 10},
    {"name": "David", "scores": [95, 90, 93], "grade": 12},
    {"name": "Eva", "scores": [78, 85, 80], "grade": 11}
]
Steps to Solve:
Calculate Average Scores: Use dictionary comprehension to create a
dictionary of students and their average scores.
Filter by Threshold: Use dictionary comprehension to filter out students
with average scores above the threshold.
Group by Grade Level: Use dictionary comprehension combined with list 
comprehension to calculate the average score for each grade level.
Example Output:
For the above data:

Average scores dictionary:

python
Copy code
{'Alice': 85.0, 'Bob': 83.0, 'Charlie': 69.0, 'David': 92.67, 'Eva': 81.0}
Students with average score > 75:

python
Copy code
{'Alice': 10, 'Bob': 11, 'David': 12, 'Eva': 11}
Average scores by grade level:

python
Copy code
{10: 77.0, 11: 82.0, 12: 92.67}
Constraints:
You should solve this using list and dictionary comprehensions where 
applicable.
Try to make your solution efficient and concise.
Give this a try, and let me know if you need any hints o
have any questions!
'''

'''students = [{'name': '', 'scores': [20, 34], 'grade_level': [2]}]'''



# Initialize an empty list to store the student data
students = []

# Define how many students you want to input
num_students = int(input("Enter the number of students: "))

# Loop to input details for each student
for _ in range(num_students):
    name = input("Enter the student's name: ")
    scores = list(map(int, input("Enter the student's scores separated by space: ").split()))
    grade_level = [int(input("Enter the student's grade level: "))]

    # Create a dictionary for each student and append it to the list
    students.append({'name': name, 'scores': scores, 'grade_level': grade_level})

# Output the list of students
print(students)


avg_score = [
    {key: (sum(value) / len(value)) if key == 'scores'
     else value[0] if key == 'grade_level'
     else value
     for key, value in student.items()}
     for student in students
]

print(avg_score)
