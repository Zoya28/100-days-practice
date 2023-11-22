#  Simple functions 
def greeting():
    print("hello there!")
    print("what are you doing?")
# greeting()


# functions with single parameter(input)
def greeting_with_name(name):#parameter
    print(f"hello there {name}!")
    print(f"what are you doing {name}?")
# greeting_with_name("zoya")#argument


# functions with more than one parameter(input)
def greeting_with_name(name,location):#parameter
    print(f"hello there {name}, I am from {location}!")
    print(f"what are you from {name}?")
# greeting_with_name("zoya","Dewas")#argument
# greeting_with_name("Dewas", "zoya")# positional argument

# to get the correct position we can use keyword argument
# greeting_with_name(location="Dewas", name="zoya")# keyword argument
