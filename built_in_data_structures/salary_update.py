# You have a list of employee records as tuples in the form:
# (employee_id, name, salary)

# You also have a dictionary that contains salary increments for some employees, in the form:
# {employee_id: increment_amount}

# Write a function that:
# Updates the salaries of employees based on the increments given in the dictionary.
# Returns a list of tuples (employee_id, name, updated_salary) sorted by updated salary descending.

def salary_update(emp_list, sal_increment):

    result_list = []    # EMPTY LIST CREATION
    for id, name, salary in emp_list:   # UNPACKING THE TUPLES IN THE LIST
        if id in sal_increment: # If id is present for incrementing the salary, add the bonus
            salary += sal_increment[id]
        temp_tuple = id, name, salary   # make a tuple of id, name and updated or may be same salary
        result_list.append(temp_tuple)  # append it in a result list

    return  sorted(result_list, reverse = True, key = lambda x: x[2]) # SORTING THE LIST OF TUPLES BY THE SALARY AS CRITERIA


employees = [
    (101, "Alice", 5000),
    (102, "Bob", 4500),
    (103, "Charlie", 5500),
    (104, "David", 4000)
]

increments = {
    101: 500,
    103: 700,
    104: 300
}

print(salary_update(employees, increments))

