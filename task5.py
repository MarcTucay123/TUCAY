class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount  

    def display_employee(self):
      
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: ${self.salary:,.2f}")


employee1 = Employee ("Legolas", "Software Developer", 80000)


print("Before Raise:")
employee1.display_employee()


employee1.give_raise(5000)


print("\nAfter Raise:")
employee1.display_employee()
