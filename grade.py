InClassExercise = []
HomeAssignment = []
Quizzes = []
InClassLab = []
MidSemTheory = 0
MidSemLab = 0
EndSemTheory = 0
EndSemLab = 0

for i in range(0, 7):
    InClassExercise.append(input("Enter InClassExercise Marks: "))
for i in range(0, 5):
    HomeAssignment.append(input("Enter HomeAssignment Marks: "))
for i in range(0, 3):
    Quizzes.append(input("Enter Quizzes Marks: "))
for i in range(0, 3):
    InClassLab.append(input("Enter InClassLab Marks: "))
  
MidSemTheory=int((input("Enter MidSemTheory Marks: ")))
MidSemLab=int((input("Enter MidSemLab Marks: ")))
EndSemTheory=int((input("Enter EndSemTheory Marks: ")))
EndSemLab=int((input("Enter EndSemLab Marks: ")))

InClassExerciseAverage = 0
HomeAssignmentAverage = 0
    InClassLab[i] = int(InClassLab[i])
    InClassLabAverage += InClassLab[i]
    
InClassExerciseAverage = InClassExerciseAverage/7
HomeAssignmentAverage = HomeAssignmentAverage/5
QuizzesAverage = QuizzesAverage/3
InClassLabAverage = InClassLabAverage/3

OverallMarks = 0.12*InClassExerciseAverage + 0.06*HomeAssignmentAverage + 0.08*QuizzesAverage + 0.24*InClassLabAverage + 0.18*MidSemTheory + 0.06*MidSemLab + 0.18*EndSemTheory + 0.8*EndSemLab

if OverallMarks>80:
    print("Grade A")
elif OverallMarks>72:
    print("Grade A-")
elif OverallMarks>64:
    print("Grade B")
elif OverallMarks>56:
    print("Grade B-")
elif OverallMarks>44:
    print("Grade C")
elif OverallMarks>36:
    print("Grade C-")
elif OverallMarks>28:
    print("Grade D")
else:
    print("Grade F")