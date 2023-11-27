xt,shift):
    cypher_text=""
    for letter in text:
        position=alphabet.index(letter)
        if direction=="encode":
            new_pos= position+shift
        else:
            new_pos= position-shift
        new_letter= alphabet[new_pos]
        cypher_text += new_letter
    print(f"The {direction}d text is {cypher_text}\n")