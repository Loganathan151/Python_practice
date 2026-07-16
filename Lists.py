# Problem 1 – Find the First and Last Element

# numbers = input("Enter numbers: ").split()
# print(numbers[0])
# print(numbers[-1])
# print(len(numbers))

# Problem 2 – Add a New Skill

# Skills = ["Python","SQL","AI"]
# new_skill = input("Enter the Skill : ")
# Skills.append(new_skill)
# print(Skills)


# Problem 3 – Replace an Element

# skills = ["Python","SQL","Excel"]
# skills[2] = 'AI'
# print(skills)


# Problem 4 – Reverse a List

# numbers = (input("Enter the numbers : "))
# numbers = numbers.split()
# print(numbers[::-1])


# Problem 5 – Largest Number

# numbers = list(map(int,(input("Enter the numbers : ").split())))
# print(numbers)
# largest = numbers[0]
# for number in numbers:
#     if number > largest:
#         largest = number

# print(largest)        


# Problem 6 – Count Even Numbers

# numbers = list(map(int,input("Enter the numbers : ").split()))
# count = 0
# for num in numbers:
#     if (num % 2) == 0:
#         count +=1
# print(count)        


# Problem 7 – Remove Duplicates




#  Problem 8 – Second Largest Number

# numbers = list(map(int,input("Enter the numbers : ").split()))
# largest = numbers[0]
# second_largest = numbers[0]

# for number in numbers :
#      if number > largest :
#         second_largest = largest
#         largest = number
#      else:
#         if number>second_largest and number != largest :
#            second_largest = number  
# print(second_largest)


# Problem 9 – Frequency Counter

# words = input("Enter the words : ").split()
# frequency={}
# for word in words:
#     if word in frequency :
#         frequency[word]+=1
#     else:
#         frequency[word] = 1

# for key,value in frequency.items():
#     print(key, ":", value)    


    # Problem 10 – AI/Data Scenario   ,count (frequency) 
    
# predictions = ["Spam", "Spam", "Not Spam", "Spam", "Not Spam"]
# result = {}
# for prediction in predictions:
#     if prediction in result:
#         result[prediction]+=1

#     else:
#         result[prediction] = 1

# for key,value in result.items():
#  print(key,":",value)       