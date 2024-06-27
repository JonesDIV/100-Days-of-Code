import cipher_art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
restart = True

def caesar(start_text, number_shift, cipher_direction):
    cipher_message = ""
    if cipher_direction == "decode":
        number_shift *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + number_shift
            cipher_message += alphabet[new_position]
        else:
            cipher_message += letter
    print(f"The {cipher_direction}d message is: {cipher_message}")


print(cipher_art.logo)


while restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    caesar(text, shift, direction)

    to_restart = input("Type 'yes' to go again, otherwise type 'no':\n")
    if to_restart == 'no':
        break