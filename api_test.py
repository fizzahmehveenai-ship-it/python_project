# import requests

# response = requests.get("https://github.com/")

# print(response.status_code)
# import requests

# response = requests.get("https://github.com/")

# data = response.json()
 
# print(data)
# import requests

# response = requests.get("https://api.github.com")

# data = response.json()

# print(data["current_user_url"])
# print(data.keys())
# user = input("You: ")

# if user == "hello":
#     print("Bot: Hi!")
# elif user == "how are you":
#     print("Bot: I am fine 😊")
# else:
#     print("Bot: I don't understand")
# while True:
#     user = input("You: ")

#     if user == "hello":
#         print("Bot: Hi!")
#     elif user == "bye":
#         print("Bot: Goodbye!")
#     elif user == "name":
#         print("Bot: My name is Fiza Bot 🤖")
#         break
#     else:
#         print("Bot: I don't understand")
# name = "fiza"
# age = 18
# city = "vehari"
# print("My name is", name)
# print("My age is", age)
# print("My city is", city)
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# city = input("Enter your city: ")

# print(f"My name is {name}")
# print(f"My age is {age}")
# print(f"I live in {city}")
# num1 = int(input("enter first number:"))
# num2 = int(input("enter second number:"))
# print("sum:", num1 + num2)
# print("sub:", num1 - num2)
# print("mul:", num1 * num2)
# print("div:", num1 / num2)
# num = 67
# if num > 0:
#     print("positive")
# elif num < 0:
#     print("negative")
# else:
#     print("zero")
# marks = int(input("enter your marks:"))
# if marks >= 50:
#     if marks >= 80:
#         print("A")
#     elif marks >= 60:
#         print("B")
#     else:
#         print("C")
# else:
#     print("Fail")
# age = int(input("Enter your age: "))

# if age >= 60:
#     print("Senior Citizen")
# elif age >= 18:
#     print("Adult")
# else:
#     print("Minor")
# num1 =  int(input("enter first number:"))
# num2 =  int(input("enter second number:"))
# if num1 > num2:
#     print(num1, "is greater than", num2)
# elif num2 > num1:
#     print(num2,"is greater than", num1)
# else:
#     print("Both numbers are equal.")
# a = int(input("enter first number:"))
# b = int(input("enter second number:"))
# c = int(input("enter third number:"))
# if a >= b and a >= c:
#     print(a, "is the greatest number")
# elif b >= a and b >= c:
#     print(b, "is the greatest number")
# else:
#     print(c," is the greatest number")
# a = int(input("enter a number:"))
# if a % 3 == 0 and a % 5 == 0:
#     print("a is divisible by both 3 and 5")
# elif a % 5 == 0:
#     print("a is divisible by 5")
# elif a % 3 == 0:
#     print("a is divisible by 3")
# else:
#     print("a is not divisible by 3 or 5")
# for i in range(1, 11):
#     print(i)
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)
# num = int(input("enter a number:"))   
# num = 5
# for i in range(1, 11):
#     print(f"{num} * {i} = {num * i}")
# for i in range(15, 0 , -1):
    # print(i)
# for i in range(1 , 6):
#     print("*" * i)
# for i in range(5, 0 , -1):
    # print("*" * i)
# for i in range(1, 6):
#     print(" " * (5 - i) + "*" * (2*i - 1))
# for i in range(4, 0, -1):
    # print(" " * (5 - i) + "*" * (2*i - 1))
# for i in range(1, 6):
#     spaces = 5 - i
#     stars = 2*i - 1

#     print(" " * spaces + "*" * stars)
# for i in range(1 , 11):
#     print(i)
# for i in range(2 , 21, 2):
#     print(i)
# for i in range(10 , 0 , -1):
#     print(i)
# for i in range(1 , 6):
#     print("*" * i)
# for i in range(1 , 6):
#     print(" " * (5 - i) + "*" * i)
# for i in range(0, 5):
#     print(" " * i + "*" * (2*(5-i) - 1))
# numbers = [10, 20, 30, 40]
# print(numbers)
# numbers = [1,3,5,7]
# numbers.append(9)
# print(numbers)
# numbers = [1,2,4,6,3,7]
# numbers.remove(4)
# print(numbers)
# numbers = [1,7,4,9,0,4,3,8]
# numbers.sort()
# print(numbers)
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))

# numbers = [num1, num2, num3]

# print(numbers)
# num1 = int(input("enter first number:"))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
# numbers = [num1, num2, num3]
# largest = max(numbers)
# smallest = min(numbers)
# print("The maximun number is:", max(numbers))
# print("The minimum number is:", min(numbers))
# numbers = [1,2,3,4,6]
# for num in numbers:
#     print(num)
# numbers = [1,2,3,4,6]
# total = 0
# for num in numbers:
#     total += num
# print("sum is:", total)
# numbers = [1,2,3,4,5,6,7,8,9,10]
# for num in numbers:
#     if num % 2 == 0:
#         print(num)
# numbers = []

# for i in range(5):
#     num = int(input("Enter number: "))
#     numbers.append(num)

# print(numbers)
# numbers = [1, 4, 7, 0, 3, 2, 6, 5]

# largest = numbers[0]

# for num in numbers:
#     if num > largest:
#         largest = num

# print("Largest number is:", largest)
# numbers = [1, 4, 7, 0, 3, 2, 6, 5]

# user_num = int(input("Enter a number: "))

# if user_num in numbers:
#     print("Number found")
# else:
#     print("Number not found")
# numbers = []
# total = 0
# even_count = 0

# input + list
# for i in range(5):
#     num = int(input("Enter a number: "))
#     numbers.append(num)

# print("Numbers:", numbers)

# # sum + even count + largest
# largest = numbers[0]

# for num in numbers:
#     total += num

#     if num % 2 == 0:
#         even_count += 1

#     if num > largest:
#         largest = num

# print("Sum is:", total)
# print("Even count:", even_count)
# print("Largest number is:", largest)
# numbers = []
# odd_count = 0

# # input
# for i in range(5):
#     num = int(input("Enter a number: "))
#     numbers.append(num)

# print("Numbers:", numbers)

# smallest = numbers[0]
# greater_than_10 = False

# # processing
# for num in numbers:
    
#     # odd count
#     if num % 2 != 0:
#         odd_count += 1
    
#     # smallest number
#     if num < smallest:
#         smallest = num
    
#     # check > 10
#     if num > 10:
#         greater_than_10 = True

# print("Odd count:", odd_count)
# print("Smallest number is:", smallest)

# if greater_than_10:
#     print("Number greater than 10 exists")
# else:
#     print("No number greater than 10")
# def great():
#     print("hello")
# great()
# def add(a , b):
#     return a + b
# result = add(4 , 8)
# print(result)
# def check_even_odd(num):
#     if num % 2 == 0:
#         print("even")
#     else:
#         print("odd")
# check_even_odd(7)
# def find_values(numbers):
#     largest = numbers[0]
#     smallest = numbers[0]

#     for num in numbers:
#         if num > largest:
#             largest = num

#         if num < smallest:
#             smallest = num

#     return largest, smallest


# nums = [3, 5, 6, 7, 9]

# largest, smallest = find_values(nums)

# print("Largest is:", largest)
# print("Smallest is:", smallest)
# def check_even(num):
#     if num % 2 == 0:
#      print("even")
#     else:
#         print("odd")
# check_even(7)
# def check_even(num):
#     if num % 2 == 0:
#         return "even"
#     else:
#         return "odd"
# result   = check_even(7)
# print(result)
# def check_even(num):
#     if num % 2 == 0:
#         return "even"
#     else:
#         return "odd"
# numbers = [5,8,3,10,7]
# for num in numbers:
#     print(num , check_even(num))
# def count_odd(numbers):
#     count = 0
#     for num in numbers:
#         if num % 2 != 0:
#             count += 1
#     return count
# nums = [5, 8, 3, 10, 7]
# result = count_odd(nums)
# print("odd numbers count:", result)
# def analyze_numbers(numbers):
#     total = 0
#     even_count = 0
#     odd_count = 0
#     smallest = numbers[0]
#     for num in numbers:
#         total += num
#     if num % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
#     if num < smallest:
#         smallest = num
#     return total,even_count,odd_count,smallest
# nums =[5,8,3,10,7]
# total , even ,odd , smallest = analyze_numbers(nums)
# print("sum:",total)
# print("Even count:",even)
# print("Odd count:",odd)
# print("smallest:",smallest)
# def analyze_numbers(numbers):
#     total = 0
#     even_count = 0
#     odd_count = 0
#     largest = numbers[0]
#     smallest = numbers[0]

#     for num in numbers:
#         total += num

#         if num % 2 == 0:
#             even_count += 1
#         else:
#             odd_count += 1

#         if num > largest:
#             largest = num

#         if num < smallest:
#             smallest = num

#     return total, even_count, odd_count, largest, smallest


# nums = [5, 8, 3, 10, 7]

# total, even, odd, largest, smallest = analyze_numbers(nums)

# print("Sum:", total)
# print("Even count:", even)
# print("Odd count:", odd)
# print("Largest:", largest)
# print("Smallest:", smallest)
# numbers = (5,12,7)
# print("first:", numbers[0])
# print("last:", numbers[-1])
# largest = numbers[0]

# for num in numbers:
#     if num > largest:
#         largest = num

# print("largest:", largest)
# numbers = (10,20,30)
# a , b , c = numbers
# print(a)
# print(b)
# print(c)
# def calculate(a, b):
#     sum_result = a + b
#     difference_result = a - b
#     product = a * b
#     result_division = a / b

#     return sum_result,difference_result ,product , result_division


# result_sum, result_difference, result_product, result_division = calculate(4, 5)

# print("The sum is:", result_sum)
# print("The difference is:",result_difference)
# print("The product is:", result_product)
# print("The  division is:", result_division)
# num1 = int(input("enter first number:"))
# num2 = int(input("enter second number:"))
# def calculate(a,b):
#     sum_result = a + b
#     difference = a - b
#     product = a * b
#     if b != 0:
#         division =  a / b
#     else:
#         division = "not allowed"
#     return sum_result , difference , product , division
# sum_result , difference , product , division = calculate(num1,num2)
# print("sum_result:", sum_result)
# print("difference:", difference)
# print("product:", product)
# print("division:",division)
# menu based calculator:
# print("1. Add")
# print("2. Subtract")
# print("3. Multiply")
# print("4. Division")
# choice = int(input("enter a choice(1-4):"))
# num1 = int(input("enter first number:"))
# num2 = int(input("enter second number:"))
# if choice == 1:
#     print("result:", num1 + num2)
# elif choice == 2:
#     print("result:", num1 - num2)
# elif choice == 3:
#     print("result:", num1 * num2)
# elif choice == 4:
#     if num1 != 0:
#         print("result:",num1 / num2)
#     else:
#         print("Division not allowed")
# else:
#     print("invalid choice")      
# def calculator(choice, num1, num2):

#     if choice == 1:
#         return num1 + num2

#     elif choice == 2:
#         return num1 - num2

#     elif choice == 3:
#         return num1 * num2

#     elif choice == 4:
#         if num2 != 0:
#             return num1 / num2
#         else:
#             return "Division not allowed"

#     else:
#         return "Invalid choice"


# while True:
#     print("\n1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Division")
#     print("5. Exit")

#     choice = int(input("Enter a choice: "))

#     if choice == 5:
#         print("Calculator closed")
#         break

#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))

#     result = calculator(choice, num1, num2)

#     print("Result:", result)
# def calculator(choice, num1, num2):
#     if choice == 1:
#         return num1 + num2

#     elif choice == 2:
#         return num1 - num2

#     elif choice == 3:
#         return num1 * num2

#     elif choice == 4:
#         if num2 != 0:
#             return num1 / num2
#         else:
#             return "Division not allowed"

#     else:
#         return "Invalid choice"
# history = []
# while True:
#     print("\n1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Division")
#     print("5. show history")
#     print("6. Exit")

#     choice = int(input("Enter a choice: "))

#     if choice == 6:
#         print("Calculator closed")
#         break
#     if choice == 5:
#         print("History",history)
#         continue
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))

#     result = calculator(choice, num1, num2)

#     print("Result:", result)
#     history.append(result)   # result save ho raha hai

#     again = input("Do you want to continue? (yes/no): ")

#     if again.lower() != "yes":
#         print("Calculator closed")
#         break
# Dictionary:
# student = {
#     "name" : "fiza",
#    "age"  : 18,
#     "city" : "vehari",
#  }
# student["class"] = "1st year"
# student["age"] = 19
# del student["city"]
# print(student)
# for key, value in student.items():
#     print(key, ":", value)
# name =input("enter your name:")
# age = input("enter your age:")
# student = {
#     "name" : name,
#     "age"  :  age,
# }
# for key, value in student.items():
#     print(key, ":", value)
# users = [
#     {"username" : "fizzah" , "password" : "123"},
#     {"username" : "ali" , "password" : "456"}
# ]

# username = input("Enter username:")
# password = input("Enter password:")
# found = False
# for user in users:
#  if username == user["username"] and password == user["password"]:
#     print("login succesful")
#     found = True
#     break
# if not found:
#     print("wrong login")
# real login app
# users = [
#     {"username": "fiza", "password": "123"},
#     {"username": "ali", "password": "456"}
# ]

# while True:
#     print("\n1. Login")
#     print("2. Signup")
#     print("3. Exit")

#     choice = input("Enter choice: ")

#     # 🔐 LOGIN
#     if choice == "1":
#         attempts = 3

#         while attempts > 0:
#             username = input("Enter username: ")
#             password = input("Enter password: ")

#             found = False

#             for user in users:
#                 if user["username"] == username and user["password"] == password:
#                     print("Login successful")
#                     found = True
#                     break

#             if found:
#                 break
#             else:
#                 attempts -= 1
#                 print("Wrong login")
#                 print("Attempts left:", attempts)

#         if attempts == 0:
#             print("Account locked")

#     # 🆕 SIGNUP
#     elif choice == "2":
#         new_username = input("Create username: ")
#         new_password = input("Create password: ")

#         users.append({
#             "username": new_username,
#             "password": new_password
#         })

#         print("Signup successful")

#     # ❌ EXIT
#     elif choice == "3":
#         print("Program closed")
#         break

#     else:
#         print("Invalid choice")
# class LoginSystem:
#     def __init__(self):
#         self.users = [
#             {"username": "fiza", "password": "123"},
#         ]

#     def login(self):
#         username = input("Enter username: ")
#         password = input("Enter password: ")

#         for user in self.users:
#             if user["username"] == username and user["password"] == password:
#                 print("Login successful")
#                 return

#         print("Wrong password")

#     def signup(self):
#         new_username = input("Create username: ")
#         new_password = input("Create password: ")

#         self.users.append({
#             "username": new_username,
#             "password": new_password
#         })

#         print("Signup successful")

#     def menu(self):
#         while True:
#             print("\n1. Login")
#             print("2. Signup")
#             print("3. Exit")

#             choice = input("Enter choice: ")

#             if choice == "1":
#                 self.login()

#             elif choice == "2":
#                 self.signup()

#             elif choice == "3":
#                 print("Program closed")
#                 break

#             else:
#                 print("Invalid choice")


# system = LoginSystem()
# system.menu()

                # Practice Question:

# name  = input("enter your name:")
# age = input("enter your age:")
# city = input("enter your city:")
# print("name:" , name)
# print("age:", age)
# print("city:", city)
# num1 = int(input("enter first number:"))
# num2 = int(input("enter second number:"))
# print("add:", num1 + num2)
# print("sub:", num1 - num2)
# print("mul:", num1 * num2)
# print("div:", num1 / num2)
# a = int(input("enter a number:"))
# if a > 0:
#    print(" positive:")
# elif a < 0:
#    print("Negative:")
# else:
#  print("zero:")
# marks = int(input("enter a number:"))
# if marks >= 80:
#    print("A")
# elif marks >= 60:
#    print("B")
# elif marks >= 50:
#    print("C")
# else:
#    print("Fail")
# a = int(input("enter first number:"))
# b = int(input("enter second number:"))
# c = int(input("enter third number:"))
# if a >= b and a >= c:
#     print(a ,"is greatest:")
# elif b >= c and b >= a:
#     print(b ,"is greatest:")
# else:
#     print(c, "is greatest:")
# for i in range(2 , 21 , 2):
#     print(i)
# for i in range(10 , 0 ,-1):
    # print(i)
# for i in range(1,6):
#     print("*" * i)
# numbers = []
# for i in range(5):
#     num = int(input("enter a number:"))
#     numbers.append(num)
# print(numbers)
# numbers = [1,2,3,4,5]
# total = 0
# even_count = 0
# largest = numbers[0]
# for num in numbers:
#     total += num
#     if num % 2 == 0:
#      even_count += 1
#     if num > largest:
#      largest = num
# print("sum:", total)
# print("even_count:", even_count)
# print("largest:", largest)
# class calculator:
#     def add(self , a , b):
#         return a + b
#     def mul(self , a , b):
#         return a * b
# calc = calculator()
# print(calc.add(2 , 5))
# print(calc.mul(2 , 5))
      
# class student :
#     def __init__(self , name , age , city):
#         self.name = name
#         self.age = age
#         self.city = city
#     def display(self):
#         print("name:", self.name)
#         print("age:", self.age)
#         print("city:", self.city)
# s1 = student("fiza", 18 , "vehari")
# s2 = student("ali", 19 , "lahore")
# s1.display()
# s2.display()
# class student:
#     def __init__(self , name , marks1 , marks2 , marks3 ):
#         self.name = name
#         self.m1 = marks1
#         self.m2 = marks2
#         self.m3 = marks3
#     def total(self):
#         total = (self.m1 + self.m2 + self.m3)
#         print("name:", self.name)
#         print("total:", total)
#     def average(self):
#         average  =  (self.m1 + self.m2 + self.m3)/3
#         print("average:", average)
# s1 = student("fiza" , 20 , 40 , 50)
# s2 = student("ali" , 30 , 60 , 50)
# s1.total()
# s2.average()
# 
# class Student:
#     def __init__(self, name, marks1, marks2, marks3):
#         self.name = name
#         self.m1 = marks1
#         self.m2 = marks2
#         self.m3 = marks3
#     def total(self):
#         return self.m1 + self.m2 + self.m3
#     def average(self):
#         return (self.m1 + self.m2 + self.m3) / 3
# s1 = Student("Fiza", 20, 40, 50)
# s2 = Student("Ali", 30, 60, 50)
# t = s1.total()
# a = s2.average()
# print("Total:", t)
# print("Average:", a)
# class Student:
#     def __init__(self, name, m1, m2, m3):
#         self.name = name
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
#     def total(self):
#         return self.m1 + self.m2 + self.m3
#     def average(self):
#         return (self.m1 + self.m2 + self.m3) / 3
#     def result(self):
#         avg = self.average()
#         if avg >= 50:
#             return "Pass"
#         else:
#             return "Fail"
#     def display(self):
#         print("Name:", self.name)
#         print("Total:", self.total())
#         print("Average:", self.average())
#         print("Result:", self.result())
# s1 = Student("Fiza", 60, 70, 80)
# s2 = Student("Ali", 30, 40, 20)
# s1.display()
# print("------")
# s2.display()
# name = input("Enter your name: ")
# file = open("data.txt", "w")
# file.write(name)
# file.close()
# file = open("data.txt", "r")
# data = file.read()
# print(data)
# file.close()
# username = input("Enter username: ")
# password = input("Enter password: ")
# with open("users.txt", "a") as file:
#     file.write(username + "," + password + "\n")
# print("Saved!")
# with open("users.txt", "r") as file:
#     data = file.read()
# print(data)
# username = input("Enter username: ")
# password = input("Enter password: ")
# found = False
# with open("users.txt", "r") as file:
#     for line in file:
#         user, pwd = line.strip().split(",")
#         if user == username and pwd == password:
#             print("Login successful")
#             found = True
#             break
# if not found:
#     print("Wrong login")
# while True:
#     print("\n1. Signup")
#     print("2. Login")
#     print("3. Exit")
#     choice = input("Enter choice: ")
#     if choice == "1":
#         username = input("Create username: ")
#         password = input("Create password: ")
#         with open("users.txt", "a") as file:
#             file.write(username + "," + password + "\n")
#         print("Signup successful")
#     elif choice == "2":
#         username = input("Enter username: ")
#         password = input("Enter password: ")
#         found = False
#         with open("users.txt", "r") as file:
#             for line in file:
#                 user, pwd = line.strip().split(",")
#                 if user == username and pwd == password:
#                     print("Login successful")
#                     found = True
#                     break
#         if not found:
#              print("Wrong login")
#     elif choice == "3":
#         print("Program closed")
#         break
#     else:
#         print("Invalid choice")
# try:
#     a = int(input("enter first number:"))
#     b = int(input("enter second number:"))
#     result = a / b
# except ZeroDivisionError:
#     print("cannot divided by zero:")
# except ValueError:
#     print("invalid input:")
# else:
#     print("result:", result)
# finally:
#     print("program finished")
# num = int(input("enter number:"))
# if num < 0:
#     raise ValueError("Negative number are not allowed:")
#     print("Valid number")
# while True:
#     print("\n1. Add")
#     print("2 . subtract")
#     print("3 . multiply")
#     print("4 . divide")
#     print("5. Exit")
#     choice = input("Enter choice:")
#     if choice == "5":
#      print("calculator closed")
#     break
# try:
#     num1 = int(input("enter first number:"))
#     num2 = int(input("enter second number:"))
#     if choice == "1":
#         print("result:", num1 + num2)
#     elif choice == "2":
#         print("result:", num1 - num2)
#     elif choice == "3":
#         print("result:", num1 * num2)
#     elif choice == "4":
#         if num2 == 0:
#                 raise ZeroDivisionError("Cannot divide by zero")
#         print("Result:", num1 / num2)

#     else:
#             print("Invalid choice")
# except ValueError:
#      print("invalid input (numbers only)")
# except ZeroDivisionError as e:
#      print("Error:", e)
# finally:
#      print("operation finished")
# from getpass import getpass

# class UserSystem:
#     def signup(self):
#         username = input("Create username: ")
#         try:
#             with open("user.txt", "r") as file:
#                 for line in file:
#                     user, pwd = line.strip().split(",")
#                     if user == username:
#                         print("Username already exists")
#                         return
#         except FileNotFoundError:
#             pass
#         password = getpass("Create password: ")
#         with open("user.txt", "a") as file:
#             file.write(username + "," + password + "\n")
#         print("Signup successful")
#     def login(self):
#         username = input("Enter username: ")
#         password = getpass("Enter password: ")
#         found = False
#         try:
#             with open("user.txt", "r") as file:
#                 for line in file:
#                     user, pwd = line.strip().split(",")
#                     if user == username and pwd == password:
#                         print("Login successful")
#                         found = True
#                         break
#         except FileNotFoundError:
#             print("No users found")
#         if not found:
#             print("Wrong login")
#     def menu(self):
#         while True:
#             print("\n1. Signup")
#             print("2. Login")
#             print("3. Exit")
#             choice = input("Enter choice: ")
#             if choice == "1":
#                 self.signup()
#             elif choice == "2":
#                 self.login()
#             elif choice == "3":
#                 print("Program closed")
#                 break
#             else:
#                 print("Invalid choice")
# system = UserSystem()
# system.menu()
# name = input("Enter your name: ")

# while True:
#     user = input(f"{name}: ").lower()

#     if "hello" in user:
#         print("Bot: Hi! How can I help you?")
    
#     elif "price" in user:
#         print("Bot: Bangles price is 300 PKR")
    
#     elif "order" in user:
#         print("Bot: Please contact 030XXXXXXX")
    
#     elif "bye" in user:
#         print("Bot: Goodbye!")
#         break
    
#     else:
#         print("Bot: Please ask something else")
# import tkinter as tk
# window = tk.Tk()
# label = tk.Label(window , text = "Hello Fiza")
# label.pack()
# window.mainloop()
# import tkinter as tk
# window = tk.Tk()
# def click():
#     print("Button clicked")
# button = tk.Button(window, text="Click Me", command=click)
# button.pack()
# window.mainloop()
# import tkinter as  tk
# window = tk.Tk()
# entry = tk.Entry(window)
# entry.pack()
# def show():
#    print(entry.get())
# Button = tk.Button(window , text = "show", command = show)
# Button.pack()
# window.mainloop()
# import tkinter as tk
# window = tk.Tk()
# window.title("Calculator")
# entry1 = tk.Entry(window)
# entry1.pack()
# entry2 = tk.Entry(window)
# entry2.pack()
# result_label = tk.Label(window , text = "Result will appear here")
# result_label.pack()
# def add():
#     num1 = int(entry1.get())
#     num2 = int(entry2.get())
#     result_label.config(text="Result: " + str(num1 + num2))

# def sub():
#     num1 = int(entry1.get())
#     num2 = int(entry2.get())
#     result_label.config(text="Result: " + str(num1 - num2))
# def mul():
#     num1 = int(entry1.get())
#     num2 = int(entry2.get())
#     result_label.config(text="Result: " + str(num1 * num2))
# def div():
#     num1 = int(entry1.get())
#     num2 = int(entry2.get())
#     if num2 == 0:
#         result_label.config(text="Cannot divide by zero")
#     else:
#         result_label.config(text="Result: " + str(num1 / num2))
# button = tk.Button(window , text = "Add" , command = add)
# button.pack()
# button = tk.Button(window , text = "Subtract" , command = sub)
# button.pack()
# button = tk.Button(window , text = "Multiply" , command = mul)
# button.pack()
# button = tk.Button(window , text = "Divide" , command = div)
# button.pack()
# window.mainloop()
import tkinter as tk
window = tk.Tk()
window.title("Pro Calculator")
window.geometry("300x300")
entry1 = tk.Entry(window)
entry1.pack(pady=5)
entry2 = tk.Entry(window)
entry2.pack(pady=5)
result_label = tk.Label(window, text = "Result will appear here")
result_label.pack(pady=5)
def calculator(op):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if op == "Add":
            result = num1 + num2
        elif op == "Subtract":
            result = num1 - num2
        elif op == "Multiply":
            result = num1 * num2
        elif op == "Divide":
            if num2 == 0:
                result_label.config(text="Cannot divide by zero")
                return
            result = num1 / num2
        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text = "enter valid numbers")   
def clear():
        entry1.delete(0, tk.END)
        entry2.delete(0, tk.END)
        result_label.config(text="Result will appear here")
frame = tk.Frame(window)
frame.pack(pady=5)
tk.Button(frame, text="Add", command=lambda: calculator("Add")).pack(side=tk.LEFT, padx=5)
tk.Button(frame, text="Subtract", command=lambda: calculator("Subtract")).pack(side=tk.LEFT, padx=5)
tk.Button(frame, text="Multiply", command=lambda: calculator("Multiply")).pack(side=tk.LEFT, padx=5)
tk.Button(frame, text="Divide", command=lambda: calculator("Divide")).pack(side=tk.LEFT, padx=5)
tk.Button(window, text="Clear", command=clear).pack(pady=10)
window.mainloop()
