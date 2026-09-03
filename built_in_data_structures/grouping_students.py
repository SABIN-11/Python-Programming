# Grouping Students by Marks
# You are given a list of student records in the form of tuples: (name, mark)

# Write a function that:
# Groups students by their marks.
# Returns a dictionary where:
# Keys are the marks.
# Values are lists of names of students who got that mark.

def grouping_students(st_records):

    map_di = {} # EMPTY DICTIONARY
    # marks = [mark for name, mark in st_records]
    # marks = list(set(marks))    # GET ONLY THE UNIQUE ONES

    # for mark in marks:
    #     map_di[mark] = [name for name, score in st_records if mark == score]
    
    # OR DO THIS INSTEAD

    for name, mark in st_records:
        if mark in map_di:  # IF MARK KEY ALREADY EXISTS
            map_di[mark].append(name)
        else:
            map_di[mark] = [name]

    return map_di


records = [("Alice", 90), ("Bob", 80), ("Charlie", 90), ("David", 70), ("Eve", 80)]
print(grouping_students(records))
