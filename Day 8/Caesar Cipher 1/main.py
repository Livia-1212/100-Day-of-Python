alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_text, shift_amount):
    encrypted_text = ""

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.
    for letter in original_text:
        if letter in alphabet and letter not in 'z' :
            index_alphabet = alphabet.index(letter)

            new_index = (index_alphabet + shift_amount) % 26
            encrypted_text += alphabet[new_index]
        # TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?
        elif letter == 'z' or 'Z':
            index_alphabet = alphabet.index('z')
            new_index = (index_alphabet + 9) % 26
            encrypted_text += alphabet[new_index]
        else:
            encrypted_text += " "


# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

    print(f"Here is the encoded text: {encrypted_text}")

encrypt(original_text = text, shift_amount=shift)








