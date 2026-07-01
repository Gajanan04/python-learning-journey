# =====================================================
# File: match_case.py
# Topic: Match Case
# =====================================================


# -----------------------------------------------------
# Question 1 (Level 1)
# Write a program to print the day of the week.
#
# Take the following input:
# - Day Number (1-7)
#
# Print:
#
# 1 -> Monday
# 2 -> Tuesday
# 3 -> Wednesday
# 4 -> Thursday
# 5 -> Friday
# 6 -> Saturday
# 7 -> Sunday
#
# Otherwise print:
# Invalid Day
# -----------------------------------------------------

day = int(input("Enter day number: "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid Day")

# -----------------------------------------------------
# Question 2 (Level 2)
# Write a program to display the month name.
#
# Take the following input:
# - Month Number (1-12)
#
# Print the corresponding month.
#
# Otherwise print:
# Invalid Month
# -----------------------------------------------------

month = int(input("Enter month number: "))

match month:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    case _:
        print("Invalid Month")

# -----------------------------------------------------
# Question 3 (Level 3)
# Write a calculator program.
#
# Take the following inputs:
# - First Number
# - Operator (+, -, *, /)
# - Second Number
#
# Perform the selected operation.
#
# Otherwise print:
# Invalid Operator
# -----------------------------------------------------

num1 = float(input("Enter first number: "))
operator = input("Enter operator: ")
num2 = float(input("Enter second number: "))

match operator:
    case "+":
        print("Answer :", num1 + num2)
    case "-":
        print("Answer :", num1 - num2)
    case "*":
        print("Answer :", num1 * num2)
    case "/":
        print("Answer :", num1 / num2)
    case _:
        print("Invalid Operator")

# -----------------------------------------------------
# Question 4 (Level 4)
# Write a program to display the menu.
#
# Menu:
# 1. Add Student
# 2. View Student
# 3. Update Student
# 4. Delete Student
# 5. Exit
#
# Take the user's choice and print the
# selected option.
#
# Otherwise print:
# Invalid Choice
# -----------------------------------------------------

print("1. Add Student")
print("2. View Student")
print("3. Update Student")
print("4. Delete Student")
print("5. Exit")

choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Add Student Selected")
    case 2:
        print("View Student Selected")
    case 3:
        print("Update Student Selected")
    case 4:
        print("Delete Student Selected")
    case 5:
        print("Exit")
    case _:
        print("Invalid Choice")

# -----------------------------------------------------
# Question 5 (Level 5)
# Write a program to check traffic signal colors.
#
# Take the following input:
# - Signal Color
#
# red    -> Stop
# yellow -> Wait
# green  -> Go
#
# Otherwise print:
# Invalid Signal
# -----------------------------------------------------

signal = input("Enter signal color: ")

match signal:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _:
        print("Invalid Signal")

# -----------------------------------------------------
# Question 6 (Level 6)
# Write a program to select a payment method.
#
# Take the following input:
# - Choice
#
# 1 -> Cash
# 2 -> UPI
# 3 -> Credit Card
# 4 -> Debit Card
#
# Otherwise print:
# Invalid Choice
# -----------------------------------------------------

choice = int(input("Enter payment choice: "))

match choice:
    case 1:
        print("Cash")
    case 2:
        print("UPI")
    case 3:
        print("Credit Card")
    case 4:
        print("Debit Card")
    case _:
        print("Invalid Choice")

# -----------------------------------------------------
# Question 7 (Level 7)
# Write a program to display the department.
#
# Take the following input:
# - Department Code
#
# CS -> Computer Science
# IT -> Information Technology
# EX -> Electronics
# ME -> Mechanical
#
# Otherwise print:
# Invalid Department
# -----------------------------------------------------

department = input("Enter department code: ")

match department:
    case "CS":
        print("Computer Science")
    case "IT":
        print("Information Technology")
    case "EX":
        print("Electronics")
    case "ME":
        print("Mechanical")
    case _:
        print("Invalid Department")

# -----------------------------------------------------
# Question 8 (Level 8)
# Write a program to check the grade.
#
# Take the following input:
# - Grade
#
# A -> Excellent
# B -> Very Good
# C -> Good
# D -> Average
# F -> Fail
#
# Otherwise print:
# Invalid Grade
# -----------------------------------------------------

grade = input("Enter grade: ")

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Very Good")
    case "C":
        print("Good")
    case "D":
        print("Average")
    case "F":
        print("Fail")
    case _:
        print("Invalid Grade")

# -----------------------------------------------------
# Question 9 (Level 9)
# Write a program to display the season.
#
# Take the following input:
# - Season Number
#
# 1 -> Summer
# 2 -> Rainy
# 3 -> Winter
#
# Otherwise print:
# Invalid Season
# -----------------------------------------------------

season = int(input("Enter season number: "))

match season:
    case 1:
        print("Summer")
    case 2:
        print("Rainy")
    case 3:
        print("Winter")
    case _:
        print("Invalid Season")

# -----------------------------------------------------
# Question 10 (Level 10)
# Write a program to create a simple ATM Menu.
#
# Menu:
# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Exit
#
# Take the user's choice and display the
# selected operation.
#
# Otherwise print:
# Invalid Choice
# -----------------------------------------------------
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Balance: ₹10,000")
    case 2:
        print("Deposit Selected")
    case 3:
        print("Withdraw Selected")
    case 4:
        print("Thank You!")
    case _:
        print("Invalid Choice")