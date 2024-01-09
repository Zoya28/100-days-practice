# check ehether number is even or odd.....

# number = int(input("enter your number:"))
# if number % 2 == 0:
#     print("number is even...")
# else:
#     print("number is odd...")


# write a program for BMI with conditional statement...

# height = float(input("enter your height: "))
# weight = int(input("enter your weight in kg:"))

# bmi = round(weight/height**2)

# if bmi<18.5:
#     print(f"your BMI is {int(bmi)}, you are unerweight...")
# elif bmi<25:
#     print(f"your BMI is {int(bmi)}, you have normal weight...")
# elif bmi<30:
#     print(f"your BMI is {int(bmi)}, you are overweight...")
# elif bmi<35:
#     print(f"your BMI is {int(bmi)}, you are obese...")
# else:
#     print(f"your BMI is {int(bmi)}, you are clinically obese...")



# write a program to fint the leap year.......

# year = int(input("enter the year:"))
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print("it is a leap year")
#         else:
#             print("it is not a leap year")
#     else:
#         print("it is a leap year")
# else:
#     print("it is not a leap year")


# pizza delievery program........
# print("welcome to the piza delieveries...")
# size = input("what size of pizza do you want? S,M,L :")
# topping = input("do you want peproni? y/n ")
# cheese = input("do you want etra cheese? y/n ")
# bill=0
# if size=="s":
#     bill+=15
# elif size == "m":
#     bill+=20
# else:
#     bill+=25

# if topping =="y":
#     if size=="s":
#         bill+=2
#     else:
#         bill+=3

# if cheese == "y":
#         bill+=1

# print(f"your total bill is ${bill}")






# rollercoster program.......
# height = float(input("enter your height:"))
# if height>120:
#     print("you can ride...")
#     age = int(input("enter your age:"))
#     photo=input("do you want to take a photo? y/n")
#     if age<12:
#         bill=5
#         print("child ticket is $5")
#     elif age<18:
#         bill=7
#         print("youth ticket is $7")
#     elif age<=45 and age<=55:
#         print("have a free ride on us!")
#     else:
#         bill=12
#         print("adults ticket is $7")

#     if photo=="y":
#         bill+=3
#     print(f"total bill is ${bill}")
# else:
#     print("sorry can't ride....")




# write a program to create a love calculator.....

name1 = input("enter your name?\n")
name2 = input("enter your lover's name?\n")
combine = name1 + name2
combine = combine.lower()

count_t = combine.count("t")
count_r = combine.count("r")
count_u = combine.count("u")
count_e = combine.count("e")
true_count = count_t + count_r + count_u + count_e

count_l = combine.count("l")
count_o = combine.count("o")
count_v = combine.count("v")
count_e1 = combine.count("e")
love_count = count_o + count_e + count_v + count_l

love_score = int(str(true_count)+str(love_count))

if love_score<10 or love_score>90:
    print(f"your score is {love_score},you go together like coke and mentos..")
elif love_score>40 and love_score<50:
    print(f"your score is {love_score},you are alright together.")
else:
    print(f"your score is {love_score}")
