student=[]

with open("students.csv") as file:
    for line in file:
        name, house= line.rstrip().split(",")
        student.append({"name":name,"hourse":house})

def get_name(student):
    return student["name"]

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")