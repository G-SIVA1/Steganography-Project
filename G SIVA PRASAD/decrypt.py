# decrypt.py
import cv2

# Decryption function
def decrypt_image(image_path, password, correct_password):
    img = cv2.imread(image_path)  # Load the image
    
    # Prepare the dictionaries for decoding
    c = {i: chr(i) for i in range(255)}  # Integer to character map

    message = ""
    m = 0
    n = 0
    z = 0

    # Ask for the passcode to decrypt
    pas = input("Enter passcode for Decryption: ")

    if password == pas:
        # Extract the hidden message from the image
        for i in range(len(secret_message)):
            message = message + c[img[n, m, z]]
            n = n + 1
            m = m + 1
            z = (z + 1) % 3
        print("Decryption message:", message)
    else:
        print("YOU ARE NOT AUTHORIZED")

# Main function to run the decryption process
def main():
    image_path = input("Enter the image path for decryption: ")
    correct_password = input("Enter the original passcode: ")
    
    decrypt_image(image_path, password, correct_password)

if __name__ == "__main__":
    main()

