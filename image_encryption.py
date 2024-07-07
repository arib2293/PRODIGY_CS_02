from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    image_array = np.array(image)

    encrypted_array = (image_array + key) % 256
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_image.save(output_path)

def decrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    image_array = np.array(image)

    decrypted_array = (image_array - key) % 256
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_image.save(output_path)

def main():
    print("Image Encryption Tool")
    choice = input("Type 'encrypt' to encrypt an image or 'decrypt' to decrypt an image: ").strip().lower()
    if choice not in ['encrypt', 'decrypt']:
        print("Invalid choice, please try again.")
        return

    image_path = input("Enter the path of the image: ").strip()
    output_path = input("Enter the path to save the output image: ").strip()
    try:
        key = int(input("Enter the encryption key (integer): ").strip())
    except ValueError:
        print("Invalid key, please enter an integer.")
        return

    if choice == 'encrypt':
        encrypt_image(image_path, output_path, key)
        print(f"Encrypted image saved to {output_path}")
    elif choice == 'decrypt':
        decrypt_image(image_path, output_path, key)
        print(f"Decrypted image saved to {output_path}")

if __name__ == "__main__":
    main()
