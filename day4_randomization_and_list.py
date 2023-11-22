# random module, lists


# random module generates number randomly. when we want random numbers in anything such as playing ludo game and cards etc. we can use random module.
# import random 
# random_number = random.randint(0,10) #random integer from range 0 to 10
# random_float = random.random() #random float from range 0 to 1 (e.g. 0.0000001-0.999999....)
# print(random_number)
# print(random_float)


# tossing the coin and generate random Heads and Tails
# import random
# random_integer = random.randint(0,1)
# if random_integer == 0:
#     print("Heads")
# else:
#     print("Tails")



# -----------list data structure-----------
# fruit = ["apple", "orange" ,"graps"]
# print(fruit[2])
# fruit.append("papaya")
# fruit.insert(2,"strawberry")
# fruit.extend(["banana","kivi","dragon fruit","lichi"])
# fruit.remove("graps")
# fruit.pop()
# print(fruit.count("apple"))


# program to pick a random name to pay the bill in a restaurant.
# import random
# names = input("Enter all the the names seperated by comma.\n")
# list_of_names = names.split(", ")
# rand_name = random.randint(0,len(list_of_names)-1)
# print(list_of_names[rand_name])