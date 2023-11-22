# write a code where you ask what is your name? and input the name and print the length of the name........
print(len(input("what is your name?\n")))




#next is we need values of 2 variables exchange... 
a= input("a:")
b=input("b:")
temp=a
a=b
b=temp
print("a:",a)
print("b:",b)





# final assignment is band name generator....
print("welcome to the band name generator...")
city_name=input("what's the name of the city you grew up in?\n")
pet_name= input("what is your pet's name?\n")
# print("your band name could be " + city_name +" "+ pet_name)
# or we can use f string.......
print(f"your band name could be {city_name} {pet_name}") 