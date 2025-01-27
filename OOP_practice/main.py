
class Student:
    name: str
    age: int
    ID: int
    def __init__(self, name: str, age: int, ID: int) -> None:
        self.name = name
        self.age = age
        self.ID = ID
    
    def __repr__(self):
        return f"{self.name}\n{self.age}\n{self.ID}"

samir: Student = Student("Samir Fadi Samir Alhindi", 19, 23465288)

print(samir)

def calculate_student_GPA(student: Student) -> float:
    return 3.65