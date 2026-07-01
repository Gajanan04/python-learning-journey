# =====================================================
# File: nested_if.py
# Topic: Nested If
# =====================================================


# -----------------------------------------------------
# Question 1 (Level 1)
# Write a program to verify an ATM PIN.
#
# Take the following inputs:
# - Account Balance
# - Entered PIN
#
# Correct PIN:
# 1234
#
# If the PIN is correct:
#     Print "Access Granted"
# Else:
#     Print "Invalid PIN"
#
# If access is granted:
#     Print the Account Balance.
# -----------------------------------------------------

balance = int(input("Enter account balance: "))
pin = int(input("Enter PIN: "))

if pin == 1234:
    print("Access Granted")
    print("Account Balance :", balance)
else:
    print("Invalid PIN")

# -----------------------------------------------------
# Question 2 (Level 2)
# Write a program to create a login system.
#
# Take the following inputs:
# - Username
# - Password
#
# Correct Credentials:
# Username : admin
# Password : python123
#
# First verify the username.
# If the username is correct,
# then verify the password.
#
# Print the result in the following format:
#
# Login Successful
# OR
# Invalid Password
# OR
# Invalid Username
# -----------------------------------------------------

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "python123":
        print("Login Successful")
    else:
        print("Invalid Password")
else:
    print("Invalid Username")

# -----------------------------------------------------
# Question 3 (Level 3)
# Write a program to check bank loan eligibility.
#
# Take the following inputs:
# - Age
# - Monthly Salary
# - Credit Score
#
# Conditions:
# Age must be 21 or above.
# If age is valid,
# check salary (>= ₹25,000).
# If salary is valid,
# check credit score (>=700).
#
# Print the result:
#
# Loan Approved
# OR
# Loan Rejected
# -----------------------------------------------------

age = int(input("Enter age: "))
salary = int(input("Enter monthly salary: "))
credit_score = int(input("Enter credit score: "))

if age >= 21:
    if salary >= 25000:
        if credit_score >= 700:
            print("Loan Approved")
        else:
            print("Loan Rejected")
    else:
        print("Loan Rejected")
else:
    print("Loan Rejected")

# -----------------------------------------------------
# Question 4 (Level 4)
# Write a program to check scholarship eligibility.
#
# Take the following inputs:
# - Percentage
# - Family Income
#
# Conditions:
# Percentage must be 75 or above.
# If eligible,
# Family Income must be below ₹3,00,000.
#
# Print:
#
# Scholarship Approved
# OR
# Scholarship Rejected
# -----------------------------------------------------

percentage = float(input("Enter percentage: "))
income = int(input("Enter family income: "))

if percentage >= 75:
    if income < 300000:
        print("Scholarship Approved")
    else:
        print("Scholarship Rejected")
else:
    print("Scholarship Rejected")

# -----------------------------------------------------
# Question 5 (Level 5)
# Write a program to generate exam results.
#
# Take the following input:
# - Percentage
#
# Conditions:
# Percentage >= 40 → Pass
# If Pass:
# Percentage >= 75 → Distinction
# Otherwise → First Class
#
# Print:
#
# Pass with Distinction
# OR
# Pass
# OR
# Fail
# -----------------------------------------------------

percentage = float(input("Enter percentage: "))

if percentage >= 40:
    if percentage >= 75:
        print("Pass with Distinction")
    else:
        print("Pass")
else:
    print("Fail")

# -----------------------------------------------------
# Question 6 (Level 6)
# Write a program to check employee bonus eligibility.
#
# Take the following inputs:
# - Years of Experience
# - Performance Rating
#
# Conditions:
# Experience >= 2 years
# If eligible,
# Performance Rating >= 4
#
# Print:
#
# Bonus Approved
# OR
# Bonus Rejected
# -----------------------------------------------------

experience = int(input("Enter years of experience: "))
rating = int(input("Enter performance rating: "))

if experience >= 2:
    if rating >= 4:
        print("Bonus Approved")
    else:
        print("Bonus Rejected")
else:
    print("Bonus Rejected")

# -----------------------------------------------------
# Question 7 (Level 7)
# Write a program for movie ticket eligibility.
#
# Take the following inputs:
# - Age
# - Has ID Card (yes/no)
#
# Conditions:
# Age must be 18 or above.
# If age is valid,
# ID Card must be available.
#
# Print:
#
# Entry Allowed
# OR
# Entry Denied
# -----------------------------------------------------

age = int(input("Enter age: "))
id_card = input("Has ID Card (yes/no): ")

if age >= 18:
    if id_card == "yes":
        print("Entry Allowed")
    else:
        print("Entry Denied")
else:
    print("Entry Denied")

# -----------------------------------------------------
# Question 8 (Level 8)
# Write a program to check driving license eligibility.
#
# Take the following inputs:
# - Age
# - Passed Driving Test (yes/no)
#
# Conditions:
# Age must be 18 or above.
# If age is valid,
# Driving Test must be passed.
#
# Print:
#
# License Approved
# OR
# License Rejected
# -----------------------------------------------------

age = int(input("Enter age: "))
test = input("Passed Driving Test (yes/no): ")

if age >= 18:
    if test == "yes":
        print("License Approved")
    else:
        print("License Rejected")
else:
    print("License Rejected")

# -----------------------------------------------------
# Question 9 (Level 9)
# Write a program to calculate shopping discount.
#
# Take the following inputs:
# - Shopping Amount
# - Premium Member (yes/no)
#
# Conditions:
# Amount must be above ₹5000.
# If amount is valid,
# Premium Members get an extra discount.
#
# Print:
#
# Final Amount :
# -----------------------------------------------------

amount = float(input("Enter shopping amount: "))
member = input("Premium Member (yes/no): ")

if amount > 5000:
    if member == "yes":
        discount = amount * 0.30
    else:
        discount = amount * 0.20
else:
    discount = 0

final_amount = amount - discount

print("Final Amount :", final_amount)

# -----------------------------------------------------
# Question 10 (Level 10)
# Write a program to check admission eligibility.
#
# Take the following inputs:
# - Percentage
# - Entrance Exam Qualified (yes/no)
#
# Conditions:
# Percentage must be 60 or above.
# If percentage is valid,
# Entrance Exam must be qualified.
#
# Print:
#
# Admission Granted
# OR
# Admission Rejected
# -----------------------------------------------------
percentage = float(input("Enter percentage: "))
exam = input("Entrance Exam Qualified (yes/no): ")

if percentage >= 60:
    if exam == "yes":
        print("Admission Granted")
    else:
        print("Admission Rejected")
else:
    print("Admission Rejected")