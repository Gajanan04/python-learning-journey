
# -----------------------------------------------------
# Question 1 (Level 1)
# Write a program to check whether a number is
# Positive, Negative, or Zero.
#
# Take the following input:
# - Number
#
# Print the result in the following format:
#
# Number is Positive
# OR
# Number is Negative
# OR
# Number is Zero
# -----------------------------------------------------

number = int(input("Enter a number: "))

if number > 0:
    print("Number is Positive")
elif number < 0:
    print("Number is Negative")
else:
    print("Number is Zero")

# -----------------------------------------------------
# Question 2 (Level 2)
# Write a program to check whether a number is
# Even or Odd.
#
# Take the following input:
# - Number
#
# Print the result in the following format:
#
# Number is Even
# OR
# Number is Odd
# -----------------------------------------------------

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

# -----------------------------------------------------
# Question 3 (Level 3)
# Write a program to find the largest of two numbers.
#
# Take the following inputs:
# - First Number
# - Second Number
#
# Print the result in the following format:
#
# Largest Number :
# -----------------------------------------------------

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest Number :", a)
else:
    print("Largest Number :", b)

# -----------------------------------------------------
# Question 4 (Level 4)
# Write a program to find the largest of three numbers.
#
# Take the following inputs:
# - First Number
# - Second Number
# - Third Number
#
# Print the result in the following format:
#
# Largest Number :
# -----------------------------------------------------

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest Number :", a)
elif b >= a and b >= c:
    print("Largest Number :", b)
else:
    print("Largest Number :", c)

# -----------------------------------------------------
# Question 5 (Level 5)
# Write a program to check whether a year is
# a Leap Year or Not.
#
# Take the following input:
# - Year
#
# Print the result in the following format:
#
# Leap Year
# OR
# Not a Leap Year
# -----------------------------------------------------

year = int(input("Enter year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# -----------------------------------------------------
# Question 6 (Level 6)
# Write a program to check whether a person is
# eligible to vote.
#
# Take the following input:
# - Age
#
# Print the result in the following format:
#
# Eligible to Vote
# OR
# Not Eligible to Vote
# -----------------------------------------------------

age = int(input("Enter age: "))

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")

# -----------------------------------------------------
# Question 7 (Level 7)
# Write a program to calculate the grade of a student.
#
# Take the following input:
# - Marks
#
# Grade Criteria:
# 90 - 100 : A
# 80 - 89  : B
# 70 - 79  : C
# 60 - 69  : D
# Below 60 : Fail
#
# Print the result in the following format:
#
# Grade :
# -----------------------------------------------------

marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade : A")
elif marks >= 80:
    print("Grade : B")
elif marks >= 70:
    print("Grade : C")
elif marks >= 60:
    print("Grade : D")
else:
    print("Grade : Fail")

# -----------------------------------------------------
# Question 8 (Level 8)
# Write a program to check the temperature condition.
#
# Take the following input:
# - Temperature (°C)
#
# Conditions:
# Above 35  : Hot
# 20 to 35  : Normal
# Below 20  : Cold
#
# Print the result in the following format:
#
# Weather :
# -----------------------------------------------------

temperature = int(input("Enter temperature: "))

if temperature > 35:
    print("Weather : Hot")
elif temperature >= 20:
    print("Weather : Normal")
else:
    print("Weather : Cold")

# -----------------------------------------------------
# Question 9 (Level 9)
# Write a program to verify a password.
#
# Take the following input:
# - Password
#
# Correct Password:
# python123
#
# Print the result in the following format:
#
# Access Granted
# OR
# Access Denied
# -----------------------------------------------------

password = input("Enter password: ")

if password == "python123":
    print("Access Granted")
else:
    print("Access Denied")

# -----------------------------------------------------
# Question 10 (Level 10)
# Write a program to create a simple login system.
#
# Take the following inputs:
# - Username
# - Password
#
# Correct Credentials:
# Username : admin
# Password : python123
#
# Print the result in the following format:
#
# Login Successful
# OR
# Invalid Username or Password
# -----------------------------------------------------

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "python123":
    print("Login Successful")
else:
    print("Invalid Username or Password")


# -----------------------------------------------------
# Medium Level
# -------------

# -----------------------------------------------------
# Question 11 (Level 11)
# Write a program to calculate the electricity bill.
#
# Take the following input:
# - Units Consumed
#
# Bill Criteria:
# First 100 Units   : ₹5 per unit
# Next 100 Units    : ₹7 per unit
# Above 200 Units   : ₹10 per unit
#
# Print the result in the following format:
#
# Total Electricity Bill :
# -----------------------------------------------------



# -----------------------------------------------------
# Question 12 (Level 12)
# Write a program to calculate income tax.
#
# Take the following input:
# - Annual Income
#
# Tax Criteria:
# Up to ₹2,50,000      : No Tax
# ₹2,50,001-₹5,00,000  : 5%
# ₹5,00,001-₹10,00,000 : 20%
# Above ₹10,00,000     : 30%
#
# Print the result in the following format:
#
# Income Tax :
# -----------------------------------------------------



# -----------------------------------------------------
# Question 13 (Level 13)
# Write a program to simulate ATM withdrawal.
#
# Take the following inputs:
# - Account Balance
# - Withdrawal Amount
#
# Print the result in the following format:
#
# Transaction Successful
# OR
# Insufficient Balance
# -----------------------------------------------------



# -----------------------------------------------------
# Question 14 (Level 14)
# Write a program for ticket booking.
#
# Take the following inputs:
# - Age
# - Number of Tickets
#
# Ticket Price:
# Child (<12)  : ₹100
# Adult         : ₹200
# Senior (60+)  : ₹150
#
# Print the result in the following format:
#
# Total Ticket Price :
# -----------------------------------------------------



# -----------------------------------------------------
# Question 15 (Level 15)
# Write a program to calculate the shopping discount.
#
# Take the following input:
# - Shopping Amount
#
# Discount:
# Above ₹5000 : 20%
# Above ₹2000 : 10%
# Otherwise   : No Discount
#
# Print the result in the following format:
#
# Final Amount :
# -----------------------------------------------------



# -----------------------------------------------------
# Question 16 (Level 16)
# Write a program to calculate BMI.
#
# Take the following inputs:
# - Weight (kg)
# - Height (m)
#
# BMI Formula:
# BMI = Weight / (Height × Height)
#
# Print the result in the following format:
#
# BMI :
# Category :
# -----------------------------------------------------



# -----------------------------------------------------
# Question 17 (Level 17)
# Write a program to check bank loan eligibility.
#
# Take the following inputs:
# - Age
# - Monthly Salary
# - Credit Score
#
# Eligibility:
# Age >= 21
# Salary >= ₹25,000
# Credit Score >= 700
#
# Print the result in the following format:
#
# Loan Approved
# OR
# Loan Rejected
# -----------------------------------------------------


# Hard Level


# -----------------------------------------------------
# Question 18 (Level 18)
# Write a menu-driven Mini Banking System.
#
# Display the following menu:
#
# 1. Check Balance
# 2. Deposit Money
# 3. Withdraw Money
# 4. Exit
#
# Take the user's choice and perform the
# corresponding operation.
# -----------------------------------------------------



# -----------------------------------------------------
# Question 19 (Level 19)
# Write a program to generate a restaurant bill.
#
# Take the following inputs:
# - Customer Name
# - Food Amount
#
# Bill Rules:
# GST : 5%
# Service Charge : 10%
#
# Print the bill in the following format:
#
# -------- Restaurant Bill --------
# Customer :
# Food Bill :
# GST :
# Service Charge :
# Total Bill :
# ---------------------------------
# -----------------------------------------------------

# -----------------------------------------------------
# Question 20 (Level 20)
# Write a program to generate a student result.
#
# Take the following inputs:
# - Student Name
# - Marks in 5 Subjects
#
# Calculate:
# - Total Marks
# - Percentage
# - Grade
# - Result (Pass/Fail)
#
# Print the result in the following format:
#
# -------- Student Result --------
# Name       :
# Total      :
# Percentage :
# Grade      :
# Result     :
# --------------------------------
# -----------------------------------------------------

