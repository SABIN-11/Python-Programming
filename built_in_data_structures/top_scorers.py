# You are given a list of student records in the form of tuples, where each tuple contains: (name, score)

# Write a function that:
# Takes the list of tuples as input.
# Returns the name(s) of the student(s) who got the highest score.

# def highest_scorers(stud_records):

#     emp_li = []
#     highest_score = -1

#     for name, score in stud_records:    # UNPACKING THE TUPLE
#         if score > highest_score:
#             highest_score = score
#             emp_li.clear()  # EMPTY THE LIST
#             emp_li.append(name)
#             continue
#         if score == highest_score:
#             emp_li.append(name)


#     return emp_li

# OR SIMPY DO THIS INSTEAD
def highest_scorers(stud_records):

    highest = max(score for name, score in stud_records)
    result = [name for name, score in stud_records if score == highest]

    return result


records = [("Alice", 85), ("Bob", 92), ("Charlie", 88), ("David", 92), ("Sabin", 100), ("jas", 100)]
print(highest_scorers(records))


