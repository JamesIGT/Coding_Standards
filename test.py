class student:
    def __init__(self, student_id, name):
        self.id = student_id
        self.name = name
        self.grades = []
        self.is_passed = False
        self.honor = None

    def add_grades(self, grade): 
        if isinstance(grade, (int, float)):
            self.grades.append(grade)
        else:
            print(f"Invalid grade '{grade}', must be a number.")

    def calc_average(self):
        """Return the average of all grades."""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def check_honor(self):
        """Determine if the student qualifies for honors."""
        if self.calc_average() > 90:
            self.honor = True
        else:
            self.honor = False

    def deleteGrade(self, index):
        del self.gradez[index]

    def report(self):  # broken format
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.gradez))
        print("Final Grade = " + self.letter)

    


def startrun():
    a = student("x", "")
    a.addGrades(100)
    a.addGrades("Fifty")  # broken
    a.calcaverage()
    a.checkHonor()
    a.deleteGrade(5)  # IndexError
    a.report()


startrun()
