# docstring is a documentation string we write to tell what a function we have created actually do when we call it..

# ******* Function with output ***********

# def format_name(f_name, l_name):
#     name=f_name+" "+l_name 
#     return name.title()
# print(format_name("ZOYA","quREshi"))


def format_name(f_name, l_name):
    '''takes first and last name and return title case version of the string'''
    
    # if user doest give any input , this function return none that means there is nothing to return
    if f_name =="" or l_name == "":
        #by using return we can terminate the function that mens it will not execute anything after return
        return    
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

print(format_name(input("what's your first name? "),input("what's your last name? ")))


