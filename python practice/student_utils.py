class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return f"{self.name} : {self.score} - {self.get_grade()}"

    def get_grade(self):
        if self.score >= 50:
            return "Pass"
        return "Fail"

    def display(self):
        print(f"{self.name} : {self.score} - {self.get_grade()}")

def get_failures(students):
    failures = [n.name for n in students if n.get_grade() == "Fail"]
    return failures
