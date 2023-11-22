import string
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction=input("type 'encode' to incrypt, type 'decode' to decrypt:\n")
text = input("type your message:\n").lower()

shift= int(input("type the shift number:\n"))

def encrypt(plain_text,shift_amount):
    cypher_text=""
    for letter in plain_text:
        position=alphabet.index(letter)   #by using index we can find the position..
        new_pos= position+shift_amount
        new_letter= alphabet[new_pos]
        cypher_text += new_letter
    print(f"The encode text is {cypher_text}\n")
encrypt(text,shift)