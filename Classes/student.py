# class Student:
#     name="Esther"
#     age=21
#     school = "AkiraChix"
#     nationality = "Kenyan"
#     first_name = "MaryJane"
#     last_name = "Blige"

#     country = "Kenya"

class Student:
    school = "AkiraChix"
    def __init__ (self,name,age,nationality,first_name,last_name,country):
        self.name = name
        self.age = age
        self.nationality = nationality
        self.first_name = first_name
        self.last_name = last_name
        self.country = country


    def greet_student(self):
            return f"Hello {self.name},welcome to {self.school}.Proudly {self.nationality}"
    def show_full_name(self):
         return f"{self.first_name} {self.last_name}"
    def year_of_birth(self):
         return f" {2023-self.age}"
    def show_initials(self):
         return f"{self.first_name[0]} {self.last_name[0]}"
    
    # 1) Update the Student Class to include these attributes - first_name, last_name, age, country
    #  - Add these methods to the Student class
    #          - show_full_name
    #          - year_of_birth
    #          - show_initials

