class MITPerson:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

mit_persons = []
n = int(input("Enter the number of MITPersons: "))

rollno=0
for i in range(n):
    rollno+=1
    name = input("Enter Name: ")
    mit_person = MITPerson(name, rollno)
    mit_persons.append(mit_person)

for i in range(len(mit_persons)):
    for j in range(i+1, len(mit_persons)):
        if mit_persons[i].name > mit_persons[j].name:
            temp = mit_persons[i]
            mit_persons[i] = mit_persons[j]
            mit_persons[j] = temp


for mit_person in mit_persons:
    print("Name: {}, Roll Number: {}".format(mit_person.name, mit_person.rollno))
