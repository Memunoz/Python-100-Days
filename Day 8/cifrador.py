alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
'''
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
shit = shift % 24'''
status = True

while status:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    def cesar(cipher_text, shift_amount, cipher_direction):
        cipher = ""
        for letter in cipher_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                if cipher_direction == "encode":
                    new_position = position + shift_amount
                elif cipher_direction == "decode":
                    new_position = position - shift_amount
                new_letter = alphabet[new_position]
                cipher += new_letter
            else:
                cipher += letter
        print(f"The {cipher_direction} text is {cipher}")

    cesar(text, shift, direction)
    result = input(
        "Type yes if you want to run again, otherwise type no:\n").lower
    if result == "no":
        status = False
        print("goodbye")
