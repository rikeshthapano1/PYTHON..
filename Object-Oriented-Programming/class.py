#  this is a class in python

class Employee:                                #this is noun-> class -> employee
    Name = "Rikesh Thapa"                      #these are the attributes of the class
    Age = 22
    language = "Python", "JS"
    salary = 10000000

#this is object of the class
print("The Name is:", Employee.Name)
print("The Age is:", Employee.Age)
print("The Languages are:", Employee.language)
print("The Salary is:", Employee.salary, "\n")

#this is instance attribute and instance method

sudesh = Employee
sudesh.Name = "Sudesh Thapa"  
sudesh.salary = 20000000                                         
print("The Name is:", sudesh.Name)                          
print("The Languages are:", sudesh.language)
print("The Salary is:", sudesh.salary, "\n")


sushmita = Employee
sushmita.Name = "Sushmita Thapa"
sushmita.language = "English, Nepali"
sushmita.position = "Manager"
sushmita.salary = 30000000
print("The Name is:", sushmita.Name)
print("The Languages are:", sushmita.language)
print("The Position is:", sushmita.position)
print("The Salary is:", sushmita.salary)



