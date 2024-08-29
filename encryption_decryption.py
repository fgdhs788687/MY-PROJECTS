import random
import string

chars=" " + string.punctuation + string.digits + string.ascii_letters
chars=list(chars)
keys=chars.copy()

random.shuffle(keys)

print(chars)
print(keys)

plain_text=input("Enter the message you want to encrypt: ")
cipher_text=""

#ENCRYPED-------------------
for letters in plain_text:
    index = chars.index(letters)
    cipher_text += keys[index]

print(f"Original message is : {plain_text}")
print(f"Encrypted message is: {cipher_text}")


cipher_text=input("Enter the message you want to decrypt: ")
plain_text=""

for letters in cipher_text:
    index = keys.index(letters)
    plain_text += chars[index]

print(f"Encrypted message is: {cipher_text}")
print(f"Decryped message is : {plain_text}")
