
# Problem:
# Write a Python program that reads a CSV file containing data on student scores. Perform the following tasks:

#     Load the data into a Pandas DataFrame.
#     Display summary statistics for each column.
#     Plot a bar chart of average scores for each subject using Matplotlib or Plotly.
#     Save the cleaned DataFrame to a new CSV file.

student_scores = [['Name', 'Math', 'Science', 'English'],
                ['Girish', 88, 92, 85],
                ['Pallavi', 76, 89, 78],
                ['Hridu', 92, 85, 91],
                ['Vedu', 71, 78, 80],
                ['Ankit', 64, 56, 60],
                ['Rahul', 90, 94, 88],
                ['Priya', 73, 68, 74],
                ['Ganesh', 82, 82, 79],
                ['Suhas', 81, 79, 77],
                ['Shweta', 70, 75, 78]]

# Calculate the average scores of each student
average_scores = []
for i, student in enumerate(student_scores[1:]):
    average_score = sum(student[1:]) / 3
    # limit the average score to two decimal places
    average_score = round(average_score, 2)
    average_scores.append([student[0], average_score])

# Add the average scores to the student_scores list
student_scores[0].append('Average')

for i, student in enumerate(student_scores[1:]):
    student.append(average_scores[i][1])

# Print the updated student_scores list
for student in student_scores:
    print(student)

# Save the updated student_scores list to a new file
with open('data/student_scores_updated.csv', 'w') as file:
    for student in student_scores:
        file.write(','.join(map(str, student)) + '\n')

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/student_scores_updated.csv')

# Display summary statistics for each column
summary_stats = df.describe()
print(summary_stats)

# Plot a bar chart of average scores for each subject
subjects = ['Math', 'Science', 'English']
average_scores = df[subjects].mean()
average_scores.plot(kind='bar', color='skyblue')
plt.ylabel('Average Score')
plt.title('Average Scores for Each Subject')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Save the cleaned DataFrame to a new CSV file
df.to_csv('data/cleaned_student_scores.csv', index=False)
print('Data saved to cleaned_student_scores.csv')

# Output:
# ['Name', 'Math', 'Science', 'English', 'Average']
# ['Girish', 88, 92, 85, 88.33]
# ['Pallavi', 76, 89, 78, 81.0]
# ['Hridu', 92, 85, 91, 89.33]

