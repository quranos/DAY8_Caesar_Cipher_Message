alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]

# caesar function (text, shift, direction)
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    # check direction
    if cipher_direction == "decode":
        shift_amount *= -1 # if shift = 5 * -1 = -5 *backward*
    elif cipher_direction == "encode":
        shift_amount *= 1 # if shift = 5 * 1 = 5 *forward*
  
    for char in start_text: # loop check char in text
        if char in alphabet: # if user enters alphabet
            position = alphabet.index(char) # position = h -> 7 <int>
            new_position = position + shift_amount # shift = 5 | new position = 7 + 5 = 12 <int>
            end_text += alphabet[new_position] # alphabet[12] = m <str>
        else: # if user enters a number/symbol/space | keep it
            end_text += char

    print(f"Here's the {cipher_direction}d result: {end_text}")

# LOGO
from art import logo
print(logo)

# Restart again
should_continue = True
while should_continue: # while True -> do this
    ans_direc = ["encode", "decode"] # I want user type 'encode' or 'decode' ONLY, so u can continue.
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    
    while direction not in ans_direc: # Is user type correct? if not loop till it correct.
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # if user type shift that's greater than num of alphabet (26) | shift > 26 alphabet
    shift = shift % 26 
    
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    # Restart or not?
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    ans_result = ["yes", "no"] # I want user type 'yes' or 'no' ONLY, so u can continue.
    while result not in ans_result: # Is user type correct? if not loop till it correct.
        result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    # check result
    if result == "no":
        should_continue = False
        print("Goodbye~")
    elif result == "yes":
        should_continue = True