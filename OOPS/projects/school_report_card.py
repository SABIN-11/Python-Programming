# 🧩 Problem: School Report Card System
# You're going to design a system that handles student report cards. Each student can be enrolled in multiple subjects, and each subject will have a score. The system should be able to:

# 🔧 Features to Implement
# Class Student:

# Attributes:
# name (string)
# roll_no (int)
# subjects (dictionary of subject name → marks)

# Methods:
# add_subject(subject_name, marks)
# get_average(): returns average of all subject marks.
# display_report(): prints the full report card.

# Class School:

# Attribute:
# students (dictionary of roll number → Student object)

# Methods:
# add_student(student)
# remove_student(roll_no)
# get_topper(): returns the student with the highest average marks.
# display_all_reports(): prints report for all students.

from tabulate import tabulate

class Student():
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.sub_mark = {}   # Initially empty dictionary as there is no record

    def add_subject(self, subject, marks):
        self.sub_mark[subject] = marks  # Key - Subject, Value - Marks

    def get_average(self):
        total_marks = sum([mark for mark in self.sub_mark.values()])    # Get the iterator for only marks and then pass that as argument to sum function
        total_subjects = len(self.sub_mark) # no of subjects
        avg = total_marks / total_subjects
        return avg

    def display_report(self):
        data = [{"Subject": key, "Marks": value} for key, value in self.sub_mark.items()]   # making a list of dictionaries where key of sub_mark is the value of "Subject" key in this case
        print(f"REPORT CARD OF {self.name}: 😂")
        print(tabulate(data, headers="keys", tablefmt="grid"))  # tabulate() function requires list of lists or list of dictionaries as argument

class School():
    def __init__(self):
        self.students = {}

    def add_student(self, std):
        self.students[std.roll_no] = std    # Roll no - key, student object - value
        print()
        print(f"{std.name} has been enrolled in our school❤️")
        
    def remove_student(self, roll):
        if roll in self.students:
            del self.students[roll] # Remove the student of roll roll number from school database
            print()
            print(f"Student of roll number {roll} is restigated from our school💔")
        else:
            print(f"Student of {roll} roll number is not in our school.")

    def get_topper(self):
        comparision_dict = {}   # Key - name, value - average marks
        for student in self.students.values():  # students dictionary contains all the enrolled student objects as values
            comparision_dict[student.name] = student.get_average()  # in new dictionary, have student names - key and their avg marks - values

        topper = max(comparision_dict, key=comparision_dict.get)    # find maximum value with values but return the key
        print()
        print(f"Topper of our school is {topper}")

    def display_all_reports(self):
        for student in self.students.values():
            student.display_report()
        


st1 = Student("Sabin", 1001)
st1.add_subject("Math", 90)
st1.add_subject("Physics", 100)
st1.add_subject("Chemistry", 80)

st2 = Student("Gorey", 1002)
st2.add_subject("Math", 100)
st2.add_subject("Physics", 100)
st2.add_subject("Chemistry", 80)

st1.display_report()

st2.display_report()

school_1 = School()
school_1.add_student(st1)
school_1.add_student(st2)

school_1.get_topper()
school_1.display_all_reports()