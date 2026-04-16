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
student = {
    "name" : "fiza",
    "age"  : 18,
    "city" : "vehari",
}
student["class"] = "1st year"
student["age"] = 19
del student["city"]
print(student)