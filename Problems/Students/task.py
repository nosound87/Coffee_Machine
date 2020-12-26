class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the id here
        self.id = self.name[0] + self.last_name + self.birth_year

input_name = input()
input_lastname = input()
input_year = input()
new_student = Student(input_name, input_lastname, input_year)
print(new_student.id)