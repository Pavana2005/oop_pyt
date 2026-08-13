# class Student:
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course

#     def display(self):
#         print("Student Name:", self.name)
#         print("Age:", self.age)
#         print("Course:", self.course)


# student1 = Student("Pavana", 21, "Computer Science")
# student1.display()


# class Car:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#     def display(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)
#         print("Price:", self.price)
#         print()
# car1 = Car("Toyota", "Fortuner", 4000000)
# car2 = Car("BMW", "X5", 9500000)
# car3 = Car("Mercedes", "C-Class", 7000000)
# car1.display()
# car2.display()
# car3.display()      
# 



# class Rectangle:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
#     def area(self):
#         return self.length * self.width
# rect1=Rectangle(10,2)
# print(rect1.area())



# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return 3.14* self.radius * self.radius
#     def circumference(self):
#         return 2 * 3.14 * self.radius
# circle1 = Circle(7)
# print("Area of Circle:", circle1.area())
# print("Circumference of Circle:", circle1.circumference())


# class Employee:
#     def __init__(self, name, employee_id, salary):
#         self.name = name
#         self.employee_id = employee_id
#         self.salary = salary
#     def display(self):
#         print("Employee Name:", self.name)
#         print("Employee ID:", self.employee_id)
#         print("Salary:", self.salary)
# employee1 = Employee("Pavana", "EMP101", 30000)
# employee1.display()
           
# class BankAccount:
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance += amount
#         print("Amount deposited:", amount)
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("Amount withdrawn:", amount)
#         else:
#             print("Insufficient balance")
#     def check_balance(self):
#         print("Current balance:", self.balance)
# account1 = BankAccount("Pavana", 10000)
# account1.deposit(5000)
# account1.withdraw(3000)
# account1.check_balance()


# class Book:
#     def __init__(self, title, author, price):
#         self.title =  title
#         self.author = author
#         self.price = price
#     def display(self):
#         print("title:", self.title)
#         print("author:", self.author)
#         print("price:", self.price)
# book1 = Book("alchemist", "Paulo Choelo", 300
# book1.display()


# class Mobile:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#     def display(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)
#         print("Price:", self.price)
# mobiles = [
#     Mobile("Samsung", "S24", 75000),
#     Mobile("Redmi", "Note 14", 18000),
#     Mobile("OnePlus", "13R", 42000),
#     Mobile("Realme", "GT 6", 30000),
#     Mobile("Vivo", "V30", 25000)
# ]
# for mobile in mobiles:
#     if mobile.price > 20000:
#         mobile.display()



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
# name = input("Enter name: ")
# age = int(input("Enter age: "))
# person1 = Person(name, age)
# person1.display()


# class Product:
#     def __init__(self,name,price,quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#     def total_price(self):
#         return self.price *self.quantity
#     def display(self):
#         print("product name", self.name)
#         print("price", self.price)
#         print("quantity", self.quantity)
#         print("total_price", self.total_price())
# name=input("enter product name:")
# price=float(input("enter price"))
# quantity = int(input("Enter quantity: "))
# Product1=Product(name,price,quantity)
# Product1.display()


# class Student:
#     def __init__(self, name, mark1, mark2, mark3):
#         self.name = name
#         self.mark1 = mark1
#         self.mark2 = mark2
#         self.mark3 = mark3
#     def total(self):
#         return self.mark1 + self.mark2 + self.mark3
#     def average(self):
#         return self.total() / 3
#     def grade(self):
#         avg = self.average()
#         if avg >= 90:
#             return "A"
#         elif avg >= 80:
#             return "B"
#         elif avg >= 70:
#             return "C"
#         elif avg >= 60:
#             return "D"
#         else:
#             return "F"
#     def display(self):
#         print("Student Name:", self.name)
#         print("Total:", self.total())
#         print("Average:", self.average())
#         print("Grade:", self.grade())
# name = input("Enter student name: ")
# mark1 = float(input("Enter mark for Subject 1: "))
# mark2 = float(input("Enter mark for Subject 2: "))
# mark3 = float(input("Enter mark for Subject 3: "))
# student1 = Student(name, mark1, mark2, mark3)
# student1.display() 


# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#     def increase_salary(self,percentage):
#         increase=self.salary*percentage/100
#         self.salary = self.salary + increase
#     def display(self):
#         print("employee name: ",self.name)
#         print("updated salary: ",self.salary)
# name=input("enter employee name")
# salary = float(input("enter sal"))
# percent = float(input("enter increased sal: "))
# employee1 = Employee(name,salary)
# employee1.increase_salary(percent)
# employee1.display()


# class Temperature:
#     def __init__(self, temperature):
#         self.temperature = temperature
#     def c_to_f(self):
#         return (self.temperature * 9/5) + 32
#     def f_to_c(self):
#         return (self.temperature - 32) * 5/9
# temp = float(input("Enter temperature: "))
# print("1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius")
# choice = int(input("\nEnter choice: "))
# t1 = Temperature(temp)
# if choice == 1:
#     print("Fahrenheit:", t1.c_to_f())
# elif choice == 2:
#     print("Celsius:", t1.f_to_c())
# else:
#     print("Invalid Choice")


# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
#     def deposit(self, amount):
#         self.__balance += amount
#         print("Deposited:", amount)
#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             print("Withdrawn:", amount)
#         else:
#             print("Insufficient balance")
#     def check_balance(self):
#         print("Balance:", self.__balance)
# account = BankAccount(10000)
# account.deposit(2000)
# account.withdraw(3000)
# account.check_balance()   


# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary
#     def get_salary(self):
#         return self.__salary
#     def set_salary(self, salary):
#         if salary > 0:
#             self.__salary = salary
#         else:
#             print("Invalid Salary")
#     def display(self):
#         print("Employee Name:", self.name)
#         print("Salary:", self.__salary)
# emp = Employee("Pavana", 30000)
# emp.display()
# emp.set_salary(35000)
# print("Updated Salary:", emp.get_salary())


# class PasswordManager:
#     def __init__(self, password):
#         self.__password = password
#     def change_password(self, old_password, new_password):
#         if old_password == self.__password:
#             self.__password = new_password
#             print("Password Changed Successfully")
#         else:
#             print("incorrect password")
#     def verify_password(self,password):
#         if password==self.__password:
#             print("password verified")
#         else:
#             print("wrong password")
# manager=PasswordManager("admin")
# old_pass=input("enter apassword: ")
# new_pass=input("enter apassword: ")
# manager.change_password(old_pass,new_pass)
# check =input("enter password to verify: ")
# manager.verify_password(check)

# class Animal:
#     def sound(self):
#         print("Animal makes a sound")
# class Dog(Animal):
#     def sound(self):
#         print("Dog says: Woof")
# class Cat(Animal):
#     def sound(self):
#         print("Cat says: Meow")
# class Cow(Animal):
#     def sound(self):
#         print("Cow says: Moo")
# dog = Dog()
# cat = Cat()
# cow = Cow()
# dog.sound()
# cat.sound()
# cow.sound()


# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     def display(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)
# class Car(Vehicle):
#     def __init__(self, brand, model, number_of_doors):
#         super().__init__(brand, model)
#         self.number_of_doors = number_of_doors
#     def display(self):
#         super().display()
#         print("Number of Doors:", self.number_of_doors)
# class Bike(Vehicle):
#     def __init__(self, brand, model, engine_capacity):
#         super().__init__(brand, model)
#         self.engine_capacity = engine_capacity
#     def display(self):
#         super().display()
#         print("Engine Capacity:", self.engine_capacity, "cc")
# car = Car("Toyota", "Fortuner", 4)
# bike = Bike("Yamaha", "R15", 155)
# car.display()
# print()
# bike.display()


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
# class Student(Person):
#     def __init__(self, name, age, course):
#         super().__init__(name, age)
#         self.course = course
#     def display(self):
#         super().display()
#         print("Course:", self.course)
# student = Student("Pavana", 21, "Full Stack")
# student.display()

# class Employee:
#     def __init__(self, name):
#         self.name = name
#     def calculate_salary(self):
#         return 0
# class FullTimeEmployee(Employee):
#     def __init__(self, name, monthly_salary):
#         super().__init__(name)
#         self.monthly_salary = monthly_salary
#     def calculate_salary(self):
#         return self.monthly_salary
# class PartTimeEmployee(Employee):
#     def __init__(self, name, hours, hourly_rate):
#         super().__init__(name)
#         self.hours = hours
#         self.hourly_rate = hourly_rate
#     def calculate_salary(self):
#         return self.hours * self.hourly_rate
# full_time = FullTimeEmployee("Pavana", 40000)
# part_time = PartTimeEmployee("Anu", 80, 300)
# print("Full-Time Employee:", full_time.name)
# print("Salary:", full_time.calculate_salary())
# print("Part-Time Employee:", part_time.name)
# print("Salary:", part_time.calculate_salary())


# class Payment:
#     def process_payment(self, amount):
#         print("Processing payment")
# class CreditCard(Payment):
#     def process_payment(self, amount):
#         print("Payment of ₹", amount, "processed using Credit Card")
# class UPI(Payment):
#     def process_payment(self, amount):
#         print("Payment of ₹", amount, "processed using UPI")
# class Cash(Payment):
#     def process_payment(self, amount):
#         print("Payment of ₹", amount, "processed using Cash")
# payments = [
#     CreditCard(),
#     UPI(),
#     Cash()
# ]
# for payment in payments:
#     payment.process_payment(1000)


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return 3.14 * self.radius * self.radius
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     def area(self):
#         return self.length * self.width
# class Triangle:
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#     def area(self):
#         return 0.5 * self.base * self.height
# shapes = [
#     Circle(7),
#     Rectangle(10, 5),
#     Triangle(8, 6)
# ]
# for shape in shapes:
#     print("Area:", shape.area())



# class Animal:
#     def sound(self):
#         print("Animal makes a sound")
# class Dog(Animal):
#     def sound(self):
#         print("Dog: Woof")
# class Cat(Animal):
#     def sound(self):
#         print("Cat: Meow")
# class Cow(Animal):
#     def sound(self):
#         print("Cow: Moo")
# class Lion(Animal):
#     def sound(self):
#         print("Lion: Roar")
# animals = [
#     Dog(),
#     Cat(),
#     Cow(),
#     Lion()
# ]
# for animal in animals:
#     animal.sound()



# class Student:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#         self.courses = {}
#     def add_course(self, course, marks):
#         self.courses[course] = marks
#     def display(self):
#         print("ID:", self.id)
#         print("Name:", self.name)
#         for course, marks in self.courses.items():
#             if marks >= 90:
#                 grade = "A+"
#             elif marks >= 80:
#                 grade = "A"
#             elif marks >= 70:
#                 grade = "B"
#             elif marks >= 60:
#                 grade = "C"
#             else:
#                 grade = "F"

#             print(course, "Marks:", marks, "Grade:", grade)
# s1 = Student(101, "Pavana")
# s2 = Student(102, "Anu")
# s1.add_course("Python", 85)
# s1.add_course("Java", 72)
# s2.add_course("Python", 95)
# s1.display()
# if s1.id == 101:
#     print("\nStudent Found")
#     s1.display()

