import os
#*********** Calculator *************
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)

def addition(num1,num2):
    '''take 2 input and add those'''
    return num1+num2
def subtraction(num1,num2):
    '''take 2 input and return the subtracton of those inputs'''
    return num1-num2
def multiply(num1,num2):
    '''take 2 input and multiply those inputs'''
    return num1*num2
def division(num1,num2):
    '''take 2 input and divide those inputs'''
    return round(num1/num2,2)

operations={
    "+":addition,
    "-":subtraction,
    "*":multiply,
    "/":division,
}

def calculator():
    num1=float(input("Enter the first number: "))
    for operator in operations:
        print(operator)
    is_continue= True
    while is_continue:
        operator = input("pick an operator. ")
        num2=float(input("Enter the next number: "))
        operation_function = operations[operator]
        answer = operation_function(num1=num1,num2=num2)
        print(f"{num1}{operator}{num2} = {answer}")
        choice = input(f"\nType 'y' to continue calculating with {answer} or  type 'n' to start new calculation: \n")
        if choice == "y":   
            num1 = answer
        else:
            is_continue=False
            os.system("cls")
            calculator()
            
calculator()