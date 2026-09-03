# Student Grade Tracker

class Student:
    def __init__(self, name):
        self.name = name
        self.grade = {}

    def add_grade(self, sub, cgpa):
        if cgpa < 0 or cgpa > 4:
            print(F"Not a valid input.")
        else:
            self.grade[sub] = cgpa

    def average(self):

        if len(self.grade) != 6:    # Assuming six subjects
            print(F"Complete grades have not been inserted yet!")
        else:
            avg = sum(self.grade.values()) / len(self.grade)
            print(F"CGPA of {self.name} is {avg}")

    def highest(self):
        print(F"Highest grade achieved by {self.name} is in {max(self.grade, key = self.grade.get)} with a CGPA of {max(self.grade.values())}")
    
    def lowest(self):
        print(F"Lowest grade achieved by {self.name} is in {min(self.grade, key = self.grade.get)} with a CGPA of {min(self.grade.values())}")



st_1 = Student("sabin")
subjects = ["Maths", "Chemistry", "Physics", "English", "Computer", "Nepali"]

for sub in subjects:
    gpa = float(input(F"Enter CGPA of {sub}: "))
    st_1.add_grade(sub, gpa)

st_1.average()
st_1.highest()
st_1.lowest()



        