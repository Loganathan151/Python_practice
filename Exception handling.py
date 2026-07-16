# Problem 1 — Handle Division by Zero

# try:
#     num = int(input("Enter number: "))
#     print(100 / num)

# except ZeroDivisionError:
#     print("Cannot divide by zero")


# Problem 2 — Invalid Input

# try:
#     num = int(input("Enter number: "))
#     print(num)

# except ValueError:
#     print("Invalid input")


# Problem 3 — File Not Found

# try:
#     with open("data.txt", "r") as file:
#         print(file.read())

# except FileNotFoundError:
#     print("File not found")


# Problem 4 — Multiple Exceptions

# try:
#     num = int(input("Enter number: "))
#     print(100 / num)

# except ValueError:
#     print("Invalid input")

# except ZeroDivisionError:
#     print("Cannot divide by zero")


# Problem 5 — Generic Exception

# try:
#     num = int(input("Enter number: "))
#     print(100 / num)

# except Exception as e:
#     print("Something went wrong")
#     print(e)


# Problem 6 — finally

# try:
#     num = int(input("Enter number: "))
#     print(100 / num)

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# finally:
#     print("Program Finished")


# Problem 7 — Raise Your Own Exception

# age = int(input("Enter age: "))

# if age < 18:
#     raise ValueError("Age must be at least 18")

# print("Eligible")


# Problem 8 — Handle Custom Raised Error

# try:
#     age = int(input("Enter age: "))

#     if age < 18:
#         raise ValueError("Age must be at least 18")

#     print("Eligible")

# except ValueError as e:
#     print(e)


# Problem 9 — Safe File Read

# try:
#     with open("data.txt", "r") as file:
#         print(file.read())

# except FileNotFoundError:
#     print("No data available")


# Problem 10 — Interview Combination(Question:Take a filename from the user.handle:Invalid filename,Missing file,Any other error)

# try:
#     filename = input("Enter filename: ")

#     with open(filename, "r") as file:
#         print(file.read())

# except FileNotFoundError:
#     print("File not found")

# except Exception:
#     print("Unexpected error")