from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    """
    Encrypt an image by performing a XOR operation on each pixel value
    """
    image = Image.open(image_path)
    pixels = np.array(image)
    encrypted_pixels = pixels ^ key
    encrypted_image = Image.fromarray(encrypted_pixels)
    encrypted_image.save("encrypted_image.png")

def decrypt_image(image_path, key):
    """
    Decrypt an image by performing a XOR operation on each pixel value
    """
    image = Image.open(image_path)
    pixels = np.array(image)
    decrypted_pixels = pixels ^ key
    decrypted_image = Image.fromarray(decrypted_pixels)
    decrypted_image.save("decrypted_image.png")

def main():
    print("Image Encryption Tool")
    print("--------------------")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    choice = input("Enter your choice: ")

    if choice == "1":
        image_path = input("Enter the image path: ")
        key = int(input("Enter the encryption key: "))
        encrypt_image(image_path, key)
        print("Image encrypted successfully!")
    elif choice == "2":
        image_path = input("Enter the encrypted image path: ")
        key = int(input("Enter the decryption key: "))
        decrypt_image(image_path, key)
        print("Image decrypted successfully!")
    else:
        print("Invalid choice. Exiting...")

if __name__ == "__main__":
    main()