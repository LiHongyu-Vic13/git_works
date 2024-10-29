# Base class.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#Student
class Student(Person):
    def __init__(self, name, age, group_number, average_score):
        super().__init__(name, age)
        self.group_number = group_number
        self.average_score = average_score
    
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"
    
    def display_scholarship(self):
        if self.average_score == 5:
            return 6000
        elif self.average_score < 5:
            return 4000
        else :
            return 0
    
#Graduate
class Graduate(Student):
    def __init__(self, name, age, group_number, average_score, scientific_works):
        super().__init__(name, age, group_number, average_score)
        self.scientific_works = scientific_works
    
    def display_info(self):
        info = super().display_info()
        return info
    
    def display_scholarship(self):
        if self.average_score == 5:
            return 8000
        elif self.average_score < 5:
            return 6000
        else :
            return 0
    
    def compare_scholarship(self, other):
        if isinstance(other, Graduate):
            return "more" if self.display_scholarship() > other.display_scholarship() else "less" if self.display_scholarship() < other.display_scholarship() else "equal"
        elif isinstance(other, Student):
            return "more" if self.display_scholarship() > other.display_scholarship() else "less" if self.display_scholarship() < other.display_scholarship() else "equal"
        else:
            return "Invalid comparison"

# example
student = Student("Anton", 20, 20701, 4.5)
graduate = Graduate("Bob", 25, 24601, 5.0, "Python program")

print("Student Info:", student.display_info())
print("Student Scholarship:", student.display_scholarship())

print("Graduate Info:", graduate.display_info())
print("Graduate Scholarship:", graduate.display_scholarship())

print("Comparison between Graduate and Student Scholarship:", graduate.compare_scholarship(student))