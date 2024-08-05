### Implement Caesar Cipher 
# Create a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. 
# Allow users to input a message and a shift value to perform encryption and decryption.


letters='abcdefghijklmnopqrstuvwxyz'
num_letters=len(letters)
def encrypt(plaintext,key):
    ciphertext=''
    for letter in plaintext:
        letter=letter.lower()
        if not letter ==' ':
            index= letters.find(letter)
            if index==-1:
                ciphertext+=letter
            else:
                new_index=index+key
                if new_index>=num_letters:
                    new_index -= num_letters
                ciphertext +=letters[new_index]
    return ciphertext

def decrypt(ciphertext,key):
    plaintext=''
    for letter in ciphertext:
        letter=letter.lower()
        if not letter ==' ':
            index= letters.find(letter)
            if index == -1:
                plaintext+= letter
            else:
                new_index=index - key
                if new_index< 0:
                    new_index += num_letters
                plaintext +=letters[new_index]
    return plaintext


print("CEASAR cipher")

print('do you want encryption or decryption')
user_input=input('e/d: ').lower()

if user_input=='e':
    print('Encryption')
    key=int(input('Enter the key through(1 to 26): '))
    text=input('Enter the text to encrypt ')
    ciphertext=encrypt(text,key)
    print(f'CIPHERTEXT: {ciphertext}')

elif user_input=='d':
    print('Decryption')
    key=int(input('Enter the key through(1 to 26): '))
    text=input('Enter the text to decrypt ')
    plaintext=decrypt(text,key)
    print(f'PLAINTEXT: {plaintext}')


