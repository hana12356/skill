class Student:
    def __init__(self, name, reg_number, marks):
        self.name = name
        self.reg_number = reg_number
        self.marks = marks
        self.average = sum(self.marks) / len(self.marks)
    
    def __str__(self):
        return f"Name: {self.name}, Registration Number: {self.reg_number}, Marks: {self.marks}, Average Marks: {self.average}"

def main():
    num_students = int(input("Enter the number of students: "))
    students_dict = {}

    for i in range(1, num_students + 1):
        print(f"\nEnter details for student {i}:")
        name = input("Name: ")
        reg_number = input("Registration Number: ")
        marks = []
        for j in range(3):
            mark = float(input(f"Enter mark for Subject {j + 1}: "))
            marks.append(mark)
        
        student = Student(name, reg_number, marks)
        students_dict[name] = student
    
    print("\nStudent Details:")
    for name, student in students_dict.items():
        print(student)

if __name__ == "__main__":
    main()

