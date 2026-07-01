# =====================================================
# File: type_conversion.py
# Topic: Type Conversion
# Questions: 10
# =====================================================


# -----------------------------------------------------
# Question 1 (Level 1)
# Take your age as input.
# Convert it into an integer.
# PrinAt the age.
# -----------------------------------------------------

age = int(input("Enter your age: "))

print("Age =", age)

# -----------------------------------------------------
# Question 2 (Level 2)
# Take your height as input.
# Convert it into a float.
# Print the height.
# -----------------------------------------------------

height = float(input("Enter your height: "))

print("Height =", height)

# -----------------------------------------------------
# Question 3 (Level 3)
# Take two numbers as input.
# Convert both into integers.
# Print their addition.
# -----------------------------------------------------

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Addition =", num1 + num2)

# -----------------------------------------------------
# Question 4 (Level 4)
# Take two decimal numbers as input.
# Convert both into float.
# Print their multiplication.
# -----------------------------------------------------

num1 = float(input("Enter first decimal number: "))
num2 = float(input("Enter second decimal number: "))

print("Multiplication =", num1 * num2)

# -----------------------------------------------------
# Question 5 (Level 5)
# Take one number as input.
# Convert it into a string.
# Print the value.
# Print its data type using type().
# -----------------------------------------------------

number = input("Enter a number: ")

number = str(number)

print("Value =", number)
print("Data Type =", type(number))

# -----------------------------------------------------
# Question 6 (Level 6)
# Take a decimal number as input.
# Convert it into an integer.
# Print the converted value.
# -----------------------------------------------------

number = float(input("Enter a decimal number: "))

number = int(number)

print("Converted Value =", number)


# -----------------------------------------------------
# Question 7 (Level 7)
# Take your name as input.
# Print the data type before and after converting it
# using str().
# -----------------------------------------------------

name = input("Enter your name: ")

print("Before Conversion =", type(name))

name = str(name)

print("After Conversion =", type(name))

# -----------------------------------------------------
# Question 8 (Level 8)
# Take:
# Name
# Age
# Height
#
# Convert:
# Age -> int
# Height -> float
#
# Print all values.
# -----------------------------------------------------

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

print("Name =", name)
print("Age =", age)
print("Height =", height)

# -----------------------------------------------------
# Question 9 (Level 9)
# Take marks of three subjects as input.
# Convert all inputs into float.
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
# Question 10 (Level 10)
# Take the following inputs:
#
# Employee Name
# Employee ID
# Salary
#
# Convert:
# Employee ID -> int
# Salary -> float
#
# Print:
#
# -------- Employee Details --------
# Name     :
# ID       :
# Salary   :
#
# Also print the data type of each variable.
# -----------------------------------------------------

employee_name = input("Enter employee name: ")
employee_id = int(input("Enter employee ID: "))
salary = float(input("Enter salary: "))

print("-------- Employee Details --------")
print("Name   :", employee_name)
print("ID     :", employee_id)
print("Salary :", salary)
print("----------------------------------")

print("Data Type of Name   :", type(employee_name))
print("Data Type of ID     :", type(employee_id))
print("Data Type of Salary :", type(salary))

# -----------------------------------------------------