# =====================================================
# File: for_loop.py
# Topic: For Loop
# Questions & Solutions: 5
# =====================================================


# -----------------------------------------------------
# Question 1 (Level 1)
# Print numbers from 1 to 10 using a for loop.
# -----------------------------------------------------

for i in range(1, 11):
    print(i)


# -----------------------------------------------------
# Question 2 (Level 2)
# Print numbers from 10 to 1 using a for loop.
# -----------------------------------------------------

for i in range(10, 0, -1):
    print(i)


# -----------------------------------------------------
# Question 3 (Level 3)
# Print all even numbers from 1 to 20.
# -----------------------------------------------------

for i in range(2, 21, 2):
    print(i)


# -----------------------------------------------------
# Question 4 (Level 4)
# Print all odd numbers from 1 to 20.
# -----------------------------------------------------

for i in range(1, 20, 2):
    print(i)


# -----------------------------------------------------
# Question 5 (Level 5)
# Take a number as input.
# Print its multiplication table up to 10.
#
# Example:
# Input : 5
#
# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50
# -----------------------------------------------------

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)