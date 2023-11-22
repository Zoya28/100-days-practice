# ------------password generator-------------------
import random
import string
letters = list(string.ascii_letters)
digits = list(string.digits)
symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '_', '+']
print(".....Welcome to the PyPassword Generator.....")
letters_length = int(input("how many letters do you want in the password?\n"))
digit_length = int(input("how many digits do you want in the password?\n"))
symbol_length = int(input("how many symbol do you want in the password?\n"))
# print("\n")

# for sequencial password----easy level
# password = ""
# for let in range(letters_length):
#     random_letter = random.choice(letters)
#     password += random_letter
# for dig in range(digit_length):
#     random_digits = random.choice(digits)
#     password += random_digits
# for sym in range(symbol_length):
#     random_symbols = random.choice(symbol)
#     password += random_symbols
# print(f"your generated password is: {password}")


# for random order password----hard level
password_list =[]
for let in range(letters_length):
    random_letter = random.choice(letters)
    password_list.append(random_letter)
for dig in range(digit_length):
    random_digits = random.choice(digits)
    password_list.append(random_digits)
for sym in range(symbol_length):
    random_symbols = random.choice(symbol)
    password_list.append(random_symbols)
random.shuffle(password_list)
string_password = ""
for each in password_list:
    string_password+= each
print(f"your generated password_list is: {string_password}")
