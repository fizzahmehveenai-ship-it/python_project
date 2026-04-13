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
for i in range(0, 5):
    print(" " * i + "*" * (2*(5-i) - 1))