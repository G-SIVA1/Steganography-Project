import cv2
import os
import string

# Load the image
img = cv2.imread("mypic.jpg")  # Replace with the correct image path

# Input the secret message and password
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Dictionaries for character mapping
d = {}
c = {}

# Populate dictionaries for character -> integer and integer -> character mappings
for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

# Initialize pixel positions
n = 0
m = 0
z = 0

# Encrypt the message into the image pixels
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3  # Loop through RGB channels

# Save the encrypted image
cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Open the encrypted image on Windows

# Save the password for later decryption
with open("password.txt", "w") as pw_file:
    pw_file.write(password)
