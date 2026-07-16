# Problem 1 – Count Even Numbers

# to find even number
# each number we have to check num%2==0,if yes count =+1.


# numbers = list(map(int,input("Enter the numbers : ").split()))
# count=0
# for num in numbers:
#     if num % 2 == 0 :
#         count+=1
# print(count)    


# Problem 2 – Count Vowels    

# letters = input("Enter the letters : ")
# count = 0 
# vowels = ("a","e","i","o","u")
# for char in letters:
#     if char in vowels: 
#         count+=1
# print(count)        


# Problem 3 – Sum of Numbers

# to find sum of given numbers ,

# numbers = list(map(int,input('enter the numbers : ').split()))
# sum=0
# for num in numbers:
#     sum = sum+num

# print(sum)


# Problem 4 – Search an Item

# to find the given item in the given list,if yes,found,if no,not found

# Skills = ["Python","SQL","AI","Excel"]
# word="AI"
# found = False
# for char in Skills:
#  if char == word:
#   found = True
#   break
# if found:
#  print("found") 
 
# else:
#   print("not found") 


# Problem 5 — Multiplication Table("Like table format")

# num = int(input("Enter the number : "))
# for i in range(1,11):
#     print(f"{num} * {i} = {num * i}")


# Problem 6 — Factorial("like if n = 5,then it should be 5*4*3*2*1")

# n = int(input("Enter the number : "))
# factorial = 1
# for i in range(1,n+1):
#     factorial = factorial * i

# print(factorial)    


# Problem 7 — Count Positive & Negative Numbers

# numbers = list(map(int,input("Enter the numbers : ").split()))
# count_positive = 0
# count_negative = 0
# for num in numbers:
#     if num > 0:
#         count_positive += 1
#     elif num < 0:
#         count_negative += 1
#     elif num == 0:
#         print("0 is neither positive or negative")

# print("positive number count : " ,count_positive)   
# print("negative number count : ", count_negative)     


# Problem 8 — Prime Number(to find given num is prime or not,"prime means divisible by itself or by 1")

# n = int(input("Eneter the number : "))
# is_prime = True
# for i in range(2,n):
#     if n % i == 0:
#         is_prime = False 
#         break
# if is_prime :
#     print("Prime")
# else:
#     print("Not Prime")        


# Problem 9 – First Non-Repeating Character

# word = input("Enter the word : ")
# count = {}
# for char in word:
#     if char in count:
#         count[char]+=1
#     else:
#         count[char] = 1
# for char in word:
#     if count[char] ==1:
#         print(char)      
#         break


# Problem 10 — Password Strength Checker

# password = input("Enter the password : ")
# has_upper = False
# has_digit = False

# for char in password :
#     if char.isupper():
#         has_upper = True
#     if char.isdigit():
#          has_digit = True 

# if len(password)>=8 and has_upper and has_digit:
#            print("Strong")

# else:
#         print("Weak")            






    
