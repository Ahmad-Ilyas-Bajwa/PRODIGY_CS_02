This tool is designed as part of an internship task in Cyber Security at Prodigy InfoTech.

This project is a simple image encryption and decryption tool developed using Python. The program manipulates image pixels to encrypt and decrypt images by converting them to RGB format and adding a fixed value to each pixel for variation. The tool uses a basic encryption method where a key is added to the RGB values of each pixel in the image.

Prerequisites
- Tkinter (usually included with Python)
- Pillow (PIL Fork) - Used for image handling and manipulation.
- NumPy - Used for numerical operations on image arrays.

How It Works
- The program converts the image into a NumPy array for pixel manipulation.
- Each pixel's RGB value is altered by adding a fixed key (e.g., 150) to each channel (Red, Green, Blue).
- The modified pixel values are then clipped to ensure they remain within the valid range of 0-255.
- The encryption process can be reversed by subtracting the key from each pixel value, restoring the original image.
