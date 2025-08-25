# 1. Odd or Even Checker
# Write a Python program that asks the user for a number and tells if it’s odd or even.
# x = int(input("Enter a number : "))
# if x%2 == 0:
#     print("Num is even")
# else:
#      print("Num is odd")


# 2. Simple Calculator
# Ask the user for two numbers and an operator (+, -, *, /). Perform the correct operation.
# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))
# op = input("Enter operator (+, -, *, /): ")

# if op == '+':
#     print("Result:", x + y)
# elif op == '-':
#     print("Result:", x - y)
# elif op == '*':
#     print("Result:", x * y)
# elif op == '/':
#     if y != 0:
#         print("Result:", x / y)
#     else:
#         print("Cannot divide by zero!")
# else:
#     print("Invalid operator.")


# l1
# age = input("Enter your age: ")
# print(age + 5)


# l2
# age = input("Enter your age: ")
# age = int(age)  # convert str to int
# print(age + 5)


# # l3
# n = int(input("Enter a number: "))

# for i in range(1, n+1):   # range goes up to n (exclusive), so we do n + 1
#     print(i)


# l4
# i = int(input("Enter a number : " ))

# while i >= 0:
#     print(i)
#     i  = i- 1


# l5
# i = int(input("Enter a number "))
# def NumCheck(i):
#     if i % 2 == 0:
#         print(" Num is even")
#     else:
#         print("Num is odd")


# NumCheck(i)


# l6
#  A function that takes a number and returns square of the number.

# def square(num):
#     return num * num

# i = int(input("Enter a number "))
# print(square(i))


# # c1
# 🧠 Challenge 1: FizzBuzz with a Twist
# Write a function fizzbuzz_plus(n) that:
# For every number from 1 to n:
# Print "Fizz" if divisible by 3
# Print "Buzz" if divisible by 5
# Print "FizzBuzz" if divisible by both
# Else, print the number
# BUT — instead of printing directly, store all results in a list and return that list.

# def fizzBuzz(n):
#     result = []
#     for num in range(1, n + 1):
#         if num % 3 == 0 and num % 5 == 0:
#             result.append("FizzBuzz")
#         elif num % 3 == 0:
#             result.append("Fizz")
#         elif num % 5 == 0:
#             result.append("Buzz")
#         else:
#             result.append(str(num))
#     return result

# print(fizzBuzz(15))


# c2
# List Sorter (Ascending and Descending)
# Ask the user to input 5 numbers. Sort and print them in both ascending and descending order.


# i1 = list((input("enter a numbers :")))
# i1 = input("Enter numbers separated by commas: ").split(",")
# i1 = [int(x.strip()) for x in i1]


# def sorting(nums):
#         nums.sort()
#         print(nums)

#         nums.sort(reverse=True)
#         print(nums)
#         return

# sorting(i1)


'''
c3
Write a Python program to find the factorial of a number
provided by the user.
'''

# i = int(input("Enter a Number :"))
# z = 1
# x = 2
# result = 0
# for i in range(1, i):
#     result = z*x
#     z = result
#     x+=1


# print(result)


# l7
# test of dictionary
# dict1 = {"key1": "value1", "key2": "value2"}
# print(dict1.keys())
# print(dict1.values())
# list1 = list(dict1.values())
# print(list1[1])  # output : value2


# l8
# clg example
# a = range(10)
# print(type(a))


# l9
# list2 = [1,23,4,5,6,9]
# print(list2[0:5])


# l10
# rows = int(input("Enter a number"))
# i = 1
# while i <= rows:
#     j=rows
#     while j > i:
#         print(" ",end=" ")
#         j=j-1
#     k=1
#     while k<=i:
#         print("*",end=" ")
#         k=k+1
#     print()
#     i = i + 1


# l11
# list3 = [1,"ravi",14.6]

# for i in list3:
#     print(i)


# l12
# reverse a string / list
# text = "Hello world, how are you?"
# words = text.split()
# words.append("Hello")
# print(words)
# Output: ['Hello', 'world,', 'how', 'are', 'you?']
# text = "Hello world, how are you?"
# words = text.split()
# words.extend("Hello")
# print(words)
# Output: ['Hello', 'world,', 'how', 'are', 'you?', 'H', 'e', 'l', 'l', 'o']
# text = "Hello world, how are you?"
# words = text.split().reverse
# words.insert(6, "Hello")
# print(words)
#  Output: ['Hello', 'world,', 'how', 'are', 'you?']


# # l13
# # Does the tuple[0:5] print fifth index value
# tuple1 = (0, 1, 2, 3, 4, 5, 6, 7)
# a = 5
# print(tuple1[0:a])  # (0, 1, 2, 3, 4)  doesnt include 5th index
# print(tuple1[:-a])  # (0, 1, 2) include 5th index
