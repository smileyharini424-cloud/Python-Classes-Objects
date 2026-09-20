class Student:

    def display(self, name, age, course):
        print("Student Details:")
        print("Name:", name)
        print("Age:", age)
        print("Course:", course)
        print()


student1 = Student()
student2 = Student()

student1.display("Harini", 20, "CSE")
student2.display("Anu", 21, "ECE")
