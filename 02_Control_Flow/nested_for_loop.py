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