student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# for this code you can add the score using the for loop in the following manner

total_score = 0
for score in student_scores:
    total_score += score

print(total_score)

# This line of code checks for the maximum score of the items in list student_scores
# This code loops through every number in the list until it gets the largest number
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)
