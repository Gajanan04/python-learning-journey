# =====================================================
# File: operators.py
# Topic: Operators
# Questions: 10
# =====================================================


# -----------------------------------------------------
# Question 1 (Level 1)
# Take two numbers as input.
# Print their addition.
# -----------------------------------------------------

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Addition =", num1 + num2)

# -----------------------------------------------------
# Question 2 (Level 2)
# Take two numbers as input.
# Print:
# Addition
# Subtraction
# -----------------------------------------------------

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Addition =", num1 + num2)
print("Subtraction =", num1 - num2)

# -----------------------------------------------------
# Question 3 (Level 3)
# Take two numbers as input.
# Print:
# Multiplication
# Division
# -----------------------------------------------------

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Multiplication =", num1 * num2)
print("Division =", num1 / num2)


# -----------------------------------------------------
# Question 4 (Level 4)
# Take two numbers as input.
# Print:
# Floor Division
# Modulus
# -----------------------------------------------------

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Floor Division =", num1 // num2)
print("Modulus =", num1 % num2)

# -----------------------------------------------------
# Question 5 (Level 5)
# Take one number as input.
# Print:
# Square
# Cube
# -----------------------------------------------------

num = int(input("Enter a number: "))

print("Square =", num ** 2)
print("Cube =", num ** 3)

# -----------------------------------------------------
# Question 6 (Level 6)
# Take the radius of a circle as input.
# Use:
# pi = 3.14
#
# Print the area of the circle.
#
# Formula:
# Area = pi * radius * radius
# -----------------------------------------------------

radius = float(input("Enter radius: "))
pi = 3.14

area = pi * radius * radius

print("Area of Circle =", area)


# -----------------------------------------------------
# Question 7 (Level 7)
# Take length and breadth as input.
#
# Print:
# Area
# Perimeter
#
# Formula:
# Area = length * breadth
# Perimeter = 2 * (length + breadth)
# -----------------------------------------------------

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

area = length * breadth
perimeter = 2 * (length + breadth)

print("Area =", area)
print("Perimeter =", perimeter)


# -----------------------------------------------------
# Question 8 (Level 8)
# Take marks of three subjects as input.
#
# Print:
# Total Marks
# Average Marks
# -----------------------------------------------------

mark1 = float(input("Enter marks of Subject 1: "))
mark2 = float(input("Enter marks of Subject 2: "))
mark3 = float(input("Enter marks of Subject 3: "))

total = mark1 + mark2 + mark3
average = total / 3

print("Total Marks =", total)
print("Average Marks =", average)

# -----------------------------------------------------
# Question 9 (Level 9)
# Take:
# Salary
# Bonus
#
# Print:
# Total Salary
# Annual Salary
#
# Annual Salary = Total Salary * 12
# -----------------------------------------------------

salary = float(input("Enter salary: "))
bonus = float(input("Enter bonus: "))

total_salary = salary + bonus
annual_salary = total_salary * 12

print("Total Salary =", total_salary)
print("Annual Salary =", annual_salary)


# -----------------------------------------------------
# Question 10 (Level 10)
# Take one number as input.
#
# Print:
# Square
# Cube
# Double
# Half
# Remainder when divided by 2
# Floor Division by 2
#
# Example:
#
# Number = 8
#
# Square = 64
# Cube = 512
# Double = 16
# Half = 4.0
# Modulus = 0
# Floor Division = 4
# -----------------------------------------------------

num = int(input("Enter a number: "))

print("Square =", num ** 2)
print("Cube =", num ** 3)
print("Double =", num * 2)
print("Half =", num / 2)
print("Modulus =", num % 2)
print("Floor Division =", num // 2)

# -----------------------------------------------------