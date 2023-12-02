def compute_total(L1,L2,L3,L4,E1,E2):
    min_labs = minT(L1,L2,L3,L4)
    total_labs = L1 + L2 + L3 + L4 - min_labs
    total_exams = (E1 + E2)/3
    return(total_labs + total_exams)

def minT(T1,T2,T3,T4):
    minT = T1
    if T2 < minT:
        minT = T2
    if T3 < minT:
        minT = T3
    if T4 < minT:
        minT = T4
    return(minT)

def compute_grade(marks):
    if marks >= 80:
        return('A')
    if marks >= 65:
        return('B')
    if marks >= 50:
        return('C')
    if marks >= 35:
        return('D')
    if marks < 35:
        return('F')

roll_no = [0,0,0,0,0]
grade = [0,0,0,0,0]

for i in range(0, 5):
    roll_no[i] = int(input("roll number: "))
    Lab1, Lab2, Lab3, Lab4 = input("Enter marks for labs: ").split()
    Exam1, Exam2 = input("Enter marks for exams: ").split()
    total = compute_total(int(Lab1),int(Lab2),int(Lab3),int(Lab4),int(Exam1),int(Exam2))
    grade[i] = compute_grade(total)

for i in range(0,5):
    print(roll_no[i], grade[i])