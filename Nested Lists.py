n = int(input())

for i in range(0,n):
    name = input()
    score = float(input())
    if i == 0:
        students = [[name,score]]
    else:
        students.append([name,score])

students = sorted(students, key=lambda x: x[1])

