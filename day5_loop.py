# for loop----------------

# fruits = ["apple", "mango","banana","orange"]
# for fruit in fruits:
#     print(fruit)

# --------find average height---------
# heights=input("enter the list elements divided by space:\n").split(" ")
# for i in range(0,len(heights)):
#     heights[i]=int(heights[i])
# print(heights)
# # sum of list
# total_height=0
# for height in heights:
#     total_height+=height
# # print(total_height)
# total_length=0
# for length in heights:
#     total_length=length
# # print(total_length)
# avg_height=round(total_height//total_length)
# print(avg_height)


# ---------find highest number-------------

# student_score = input("enter the list of student score:").split(" ")
# for a in range(0,len(student_score)):
#     student_score[a] = int(student_score[a])
# print(student_score)

# max = 0
# for score in student_score:
#     if score>max:
#         max=score
# print(f"the highest score in the class is: {max}")


# -----------add all the even number from 0 to 100 usiing loop----------
# total=0
# for num in range(0,101,2):
#     total+=num
#     print(num)
# print(total)
# or
# total2=0
# for num in range (0,101):
#     if num%2==0:
#         total2+=num
# print(total2)


# ---------------fizz-buzz game---------------
# for num in range(1,101):
    
#     if num%3==0 and num%5==0:
#         print("fizz-buzz")
#     elif num%3==0:
#         print("fizz")
#     elif num%5==0:
#         print("buzz")
#     else:
#         print(num)