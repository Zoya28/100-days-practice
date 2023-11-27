import string
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# ************** one way ****************

# def cypher(direction,text,shift):
#     cypher_text=""
#     for letter in text:
#         position=alphabet.index(letter)
#         if direction=="encode":
#             new_pos= position+shift
#         else:
#             new_pos= position-shift
#         new_letter= alphabet[new_pos]
#         cypher_text += new_letter
#     print(f"The {direction}d text is {cypher_text}\n")

# **************** 2nd way *****************
def cypher(direction,text,shift):
    cypher_text=""
    if direction=="decode":
        shift *= -1
    for letter in text:
        position=alphabet.index(letter)
        new_pos= position+shift
        cypher_text += alphabet[new_pos]
    print(f"The {direction}d text is {cypher_text}\n")

direction=input("type 'encode' to incrypt, type 'decode' to decrypt:\n")
text = input("type your message:\n").lower()
shift= int(input("type the shift number:\n"))


cypher(direction,text,shift)
