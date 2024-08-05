###Pixel Manipulation for Image Encryption 
# Develop a simple image encryption tool using pixel manipulation. 
# You can perform operations like swapping pixel values or applying a basic mathematical operation to each pixel.
#  Allow users to encrypt and decrypt images.from PIL import Image

def encrypt_image(image_path, key):
    image = Image.open(image_path)
    pixels = list(image.getdata())

    encrypted_pixels = [(pixel[0] + key, pixel[1] + key, pixel[2] + key) for pixel in pixels]

    encrypted_image = Image.new(image.mode, image.size)
    encrypted_image.putdata(encrypted_pixels)
    encrypted_image.save("encrypted_image.png")



def decrypt_image(image_path, key):
    image = Image.open(image_path)
    pixels = list(image.getdata())

    decrypted_pixels = [(pixel[0] - key, pixel[1] - key, pixel[2] - key) for pixel in pixels]

    decrypted_image = Image.new(image.mode, image.size)
    decrypted_image.putdata(decrypted_pixels)
    decrypted_image.save("decrypted_image.png")




# Example usage
image_path = input("Enter the image file path: ")
key = int(input("Enter the encryption key: "))



encrypt_image(image_path, key)
print("Image encrypted successfully!")

decrypt_image("encrypted_image.png", key)
print("Image decrypted successfully!")