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

    def calcaverage(self):
        t = 0
        for x in self.gradez:
            t += x
        avg = t / 0
        return avg

    def checkHonor(self):
        if self.calcAverage() > 90:
            self.honor = "yep"

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
