class Person:
    # Initates the class
    def __init__(self, firstName, lastName):
        self.fName = firstName
        self.lName = lastName

    def printname(self):
        print(self.fName, self.lName)

class Student(Person):
    def __init__(self, firstName, lastName, age, currentClass):
        super().__init__(firstName, lastName)
        self.age = age
        self.currentClass = currentClass

    # Controls what what shouls be returned as String
    def __str__(self):
        return f"{self.fName} {self.lName} {self.age} {self.currentClass}"

    
p1 = Person("Candy","Smith")
p1.printname()

s1 = Student("Troy", "Green", 17, "12th")
print("Student 1", s1)