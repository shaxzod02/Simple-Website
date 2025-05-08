
# Employee class to represent an employee and their subordinates
class Employee:
    def __init__(self, name, subordinates=[]):
        self.name = name  # The name of the employee
        self.subordinates = subordinates  # List of employees who report to this employee
        
    def __repr__(self):
        return self.name  # String representation of an Employee is their name

# Recursive function to list all employees, with indentation to represent hierarchy levels
def list_employees(employee, level=0):
    # Print the employee's name with indentation based on their level in the hierarchy
    print(" " * (level * 4), employee)
    # Recursively list the subordinates of the current employee
    for subordinate in employee.subordinates:
        list_employees(subordinate, level + 1)

# Creating an organization structure (hierarchy of employees)
staff = Employee("Emilia",  # Emilia is the root employee (CEO)
                 [
                    Employee("Antti"),  # Antti reports directly to Emilia
                    Employee("Leena", [Employee("Jussi")]),  # Leena reports to Emilia, and Leena manages Jussi
                    Employee("Matti", [Employee("Sasu")])  # Matti reports to Emilia, and Matti manages Sasu
                 ])

# Calling the function to list all employees starting from Emilia
list_employees(staff)

# Output:
# The list_employees function will print each employee's name, indented according to their hierarchical level. The recursion allows us to go deeper into the hierarchy of subordinates.

# Expected Output:
# Emilia
#     Antti
#     Leena
#         Jussi
#     Matti
#         Sasu

# Explanation:
# Employee Class: The Employee class represents each employee in the company. Each employee has a name and a list of subordinates who report directly to them.

# Recursion: The list_employees function works recursively. It starts by printing the name of the employee, and then calls itself on each of the employee's subordinates. The level argument helps control the indentation to reflect the hierarchy structure visually.

# Output:

# Emilia is the top-level employee (the CEO, in this case).

# Antti, Leena, and Matti are direct subordinates of Emilia.

# Leena manages Jussi, and Matti manages Sasu, which is shown with proper indentation.

# Potential Issue with Default Argument (subordinates=[]):
# In the current code, the default value of subordinates is a mutable list ([]). This can lead to unintended behavior if you create an Employee object without specifying subordinates, as the same list might be shared across multiple instances of Employee. To avoid this, it's a good practice to use None as the default argument and initialize the list inside the __init__ method if needed:

class Employee:
    def __init__(self, name, subordinates=None):
        if subordinates is None:
            subordinates = []
        self.name = name
        self.subordinates = subordinates

