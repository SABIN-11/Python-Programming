#Build an employee system where different types of employees calculate pay differently.

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def display_info(self):
        print(F"Employee Name: {self.name} & Employee ID: {self.id}")


class Full_time(Employee):
    def __init__(self, name, id, monthly_salary):
        super().__init__(name, id)
        self.monthly_salary = monthly_salary

    def annual_income(self):
        self.display_info()
        print(F"Annual Income = ${self.monthly_salary * 12}")

class Part_time(Employee):
    def __init__(self, name, id, hourly_salary, hours):
        super().__init__(name, id)
        self.hourly_salary = hourly_salary
        self.hours = hours

    def daily_income(self):
        self.display_info()
        print(F"Daily Income = ${self.hours * self.hourly_salary}")

emp_1 = Full_time("Sabin", "001", 15000)
emp_1.annual_income()

emp_2 = Part_time("Saral", "002", 50, 3)
emp_2.daily_income()
        
        
        