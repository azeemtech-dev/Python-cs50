class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name=name

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house=house

    def __str__(self):
         return f"Student name: {self.name}, Student house: {self.house}"

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject=subject
    
    def __str__(self) -> str:
        return f"\nProfessor name: {self.name} Professor subject: {self.subject}"

student = Student("azeem", "iyana ipaja")
professor = Professor("agunbiade", "com113")
print(student,professor)
        















