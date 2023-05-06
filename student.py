# class Student():
#     name = "Joyce"
#     age =22
#     school = "Akirachix"
#     nationality = "Kenyan"

# class Student:
#     school = "Akirachix"
#     def __init__(self,name,age,nationality):
#         self.name = name
#         self.age = age
#         self.nationality = nationality

class Student:
    school = "Akirachix"
    def __init__(self,first_name,last_name,country,age,nationality):
        self.age = age
        self.nationality = nationality
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
    # def greet_student(self):
    #     return f"Hello {self.name} welcome to {self.school}"
    def year_of_birth(self):
        year = 2023-self.age
        return f"Hello {self.first_name} {self.last_name},you were born in{year}"
    def show_full_name(self):
        return (f"Hi {self.first_name} {self.last_name}")
    def show_initials(self):
        return (f"{self.first_name[0]} {self.last_name[0]}")
    
    
    
            
        