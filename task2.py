class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old, and I am studying {self.course}.")

# Create three student objects
student1 = Student("Halaena", 20, "Computer Science")
student2 = Student("Ekko", 22, "Computer Engineering")
student3 = Student("Camille", 21, "Information Technology")

# Call their introduce() method
student1.introduce()
student2.introduce()
student3.introduce()
