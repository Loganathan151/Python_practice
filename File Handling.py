# Problem 1 — Read a File

# with open("data.txt","r") as file:
#     content = file.read()
# print(content) 


# Problem 2 — Write to a File

# with open("notes.txt","w")as file
#    file.write("Python is powerful.")


# Problem 3 — Append

# with open("notes.txt", "a") as file:
#     file.write("\nAI")


# Problem 4 — Count Lines

# with open("notes.txt","r") as file
#    content = file.readlines()
# print(len(content))   


# Problem 5 — Count Words

# with open("data.txt","r") as file
#     text = file.read()
#     words = text.split()
# print(len(words))


# Problem 6 — Count Characters

# with open("data.txt", "r") as file:
#     text = file.read()

# print(len(text))


# Problem 7 — Search a Word

# with open("data.txt","r")as file
#     text = file.read()
# if "python" in text:
#     print("found")
# else:
#     print("not found")        


# Problem 8 — Read CSV 

# with open("employees.csv","r") as file
#     for line in file:
#         print(line)


# Problem 9 — File Not Found

# try:
#     with open("abc.txt", "r") as file:
#         print(file.read())

# except FileNotFoundError:
#     print("File not found")


# Problem 10 — Copy File

# with open("data.txt", "r") as file:
#     content = file.read()

# with open("backup.txt", "w") as file:
#     file.write(content)