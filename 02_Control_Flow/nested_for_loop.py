# =====================================================
# File: nested_for_loop.py
# Topic: Nested For Loop
# Questions & Solutions: 5
# =====================================================


# -----------------------------------------------------
# Question 1 (Level 1)
# Print the following pattern:
#
# *
# *
# *
# *
# *
# -----------------------------------------------------

for i in range(5):
    for j in range(1):
        print("*")
        
        
# -----------------------------------------------------
# Question 2 (Level 2)
# Print the following pattern:
#
# * * * * *
# -----------------------------------------------------

for i in range(1):
    for j in range(5):
        print("*", end=" ")
    print()


# -----------------------------------------------------
# Question 3 (Level 3)
# Print the following pattern:
#
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# -----------------------------------------------------

for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()


# -----------------------------------------------------
# Question 4 (Level 4)
# Print the following pattern:
#
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# -----------------------------------------------------

for i in range(5):
    for j in range(1, 6):
        print(j, end=" ")
    print()


# -----------------------------------------------------
# Question 5 (Level 5)
# Print the following pattern:
#
# A B C D E
# A B C D E
# A B C D E
# A B C D E
# A B C D E
# -----------------------------------------------------

for i in range(5):
    for j in range(65, 70):
        print(chr(j), end=" ")
    print()

    # =====================================================
# File: nested_for_loop.py
# Topic: Nested For Loop
# Questions 6 - 10
# =====================================================


# -----------------------------------------------------
# Question 6 (Level 6)
# Print the following pattern:
#
# *
# **
# ***
# ****
# *****
# -----------------------------------------------------

for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end="")
    print()


# -----------------------------------------------------
# Question 7 (Level 7)
# Print the following pattern:
#
# 1
# 12
# 123
# 1234
# 12345
# -----------------------------------------------------

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()


# -----------------------------------------------------
# Question 8 (Level 8)
# Print the following pattern:
#
# A
# AB
# ABC
# ABCD
# ABCDE
# -----------------------------------------------------

for i in range(65, 70):
    for j in range(65, i + 1):
        print(chr(j), end="")
    print()


# -----------------------------------------------------
# Question 9 (Level 9)
# Print the following pattern:
#
# 1
# 22
# 333
# 4444
# 55555
# -----------------------------------------------------

for i in range(1, 6):
    for j in range(1, i + 1):
        print(i, end="")
    print()


# -----------------------------------------------------
# Question 10 (Level 10)
# Print the following pattern:
#
# A
# BB
# CCC
# DDDD
# EEEEE
# -----------------------------------------------------

for i in range(65, 70):
    for j in range(65, i + 1):
        print(chr(i), end="")
    print()