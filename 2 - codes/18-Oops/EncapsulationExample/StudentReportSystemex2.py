class Student:
    def __init__(self, name, roll_no):
        self.name = name                   # Public
        self.__marks = {}                  # Private

    def add_marks(self, subject, score):
        if 0 <= score <= 100:
            self.__marks[subject] = score
        else:
            print("Invalid score.")

    def get_grade(self, subject):
        score = self.__marks.get(subject, None)
        if score is None:
            return "No score"
        elif score >= 90:
            return "A"
        elif score >= 75:
            return "B"
        elif score >= 60:
            return "C"
        else:
            return "Fail"

    def get_all_marks(self):
        return self.__marks.copy()  # Prevents external modification

# Usage
stud = Student("Sara", 21)
stud.add_marks("Math", 88)
stud.add_marks("Science", 92)
print(stud.get_grade("Science"))
print(stud.get_all_marks())
