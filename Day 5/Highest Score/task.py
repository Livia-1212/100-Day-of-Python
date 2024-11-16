# student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# print(range(1, 10))

scores = [8, 65, 89, 86, 55, 91, 64, 89]
highest_score = 0
for current_score in scores:
    if current_score > highest_score:
        highest_score = current_score

print(highest_score)

