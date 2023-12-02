import itertools
import csv

grades = [4, 5, 6, 7, 8, 9, 10]
target_cgpa = 8
remaining_courses = 5

# Generate all permutations of grade points for the remaining courses
permutations = list(itertools.product(grades, repeat=remaining_courses))

# Filter permutations that result in a CGPA of 8 or above
valid_permutations = [p for p in permutations if sum(p) / remaining_courses >= target_cgpa]

# Print the valid permutations and the grade point for course 1
for p in valid_permutations:
    grade_point_course1 = p[0]
    print(f"Grade point for course 1: {grade_point_course1}, Permutation: {p}")

# Export valid permutations to CSV
with open('perm.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(valid_permutations)
