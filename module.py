class Student:
    def __init__(self, name, roll, branch, sem, m1, m2):
        self.name = name
        self.roll = roll
        self.branch = branch
        self.sem = sem
        self.m1 = m1
        self.m2 = m2
        self.total = m1 + m2
        self.average = self.total / 2
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.average >= 80:
            return "A"
        elif self.average >= 60:
            return "B"
        elif self.average >= 35:
            return "C"
        else:
            return "F"
    def display(self):
        return f"{self.name}\t{self.roll}\t{self.branch}\t{self.sem}\t{self.total}\t{self.average:.2f}\t{self.grade}"
   
class Sportsstudent(Student):
    def __init__(self, name, roll, branch, sem, m1, m2, sport_marks):
        super().__init__(name, roll, branch, sem, m1, m2)
        self.sport_marks = sport_marks
        self.total+= sport_marks
        self.average = self.total / 3
        self.grade = self.calculate_grade()
    def calculate_grade(self):
        if self.average>=85:
            return "A+"
        elif self.average >= 70:
            return "A"
        elif self.average >= 50:
            return "B"
        elif self.average >= 35:
            return "C"
        else:
            return "F"
    def display(self):
        return f"{self.name}\t{self.roll}\t{self.branch}\t{self.sem}\t{self.total}\t{self.average:.2f}\t{self.grade}\t{self.sport_marks}"
        