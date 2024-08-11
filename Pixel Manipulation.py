import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np

# Initialize the main window
window = tk.Tk()
window.title("Simple Image Encryption Tool")
window.geometry("1000x600")  # Increased width to accommodate both image panels

# Global variables to hold the image and the key
original_image = None
encrypted_image = None
key = 150 #50  # Simple key for encryption/decryption (can be any integer)

# Function to open an image file
def open_image():
    global original_image
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        original_image = Image.open(file_path)
        display_image(original_image, panel_original)

# Function to encrypt the image
def encrypt_image():
    global original_image, encrypted_image, key
    if original_image:
        # Convert the image to a numpy array for pixel manipulation
        img_array = np.array(original_image, dtype=np.uint8)
        
        # Encrypt by adding the key to each pixel value and keeping within 0-255 range
        encrypted_array = np.clip(img_array + key, 0, 255)  # Ensure values are within 0-255
        encrypted_image = Image.fromarray(encrypted_array.astype(np.uint8))

        # Display the encrypted image
        display_image(encrypted_image, panel_encrypted)

# Function to decrypt the image
def decrypt_image():
    global encrypted_image, key
    if encrypted_image:
        # Convert the encrypted image to a numpy array
        encrypted_array = np.array(encrypted_image, dtype=np.uint8)
        
        # Decrypt by subtracting the key from each pixel value and keeping within 0-255 range
        decrypted_array = np.clip(encrypted_array - key, 0, 255)  # Ensure values are within 0-255
        decrypted_image = Image.fromarray(decrypted_array.astype(np.uint8))

        # Display the decrypted image
        display_image(decrypted_image, panel_encrypted)

# Function to save the encrypted image
def save_image():
    if encrypted_image:
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
        if file_path:
            encrypted_image.save(file_path)

# Function to display image on a panel
def display_image(img, panel):
    img = img.resize((300, 300), Image.LANCZOS)  # Resize image to fit the panel
    img_display = ImageTk.PhotoImage(img)
    panel.configure(image=img_display)
    panel.image = img_display

# Create frames for image panels
frame_original = tk.Frame(window, width=300, height=300, bg="lightgray")
frame_original.pack(side="left", padx=10, pady=10)

frame_encrypted = tk.Frame(window, width=300, height=300, bg="lightgray")
frame_encrypted.pack(side="right", padx=10, pady=10)

# Create labels within the frames to hold images
panel_original = tk.Label(frame_original, text="Original Image", bg="lightgray")
panel_original.pack(expand=True)

panel_encrypted = tk.Label(frame_encrypted, text="Encrypted/Decrypted Image", bg="lightgray")
panel_encrypted.pack(expand=True)

# Create buttons
open_button = tk.Button(window, text="Open Image", command=open_image)
open_button.pack(pady=10)

encrypt_button = tk.Button(window, text="Encrypt Image", command=encrypt_image)
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(window, text="Decrypt Image", command=decrypt_image)
decrypt_button.pack(pady=10)

save_button = tk.Button(window, text="Save Encrypted Image", command=save_image)
save_button.pack(pady=10)

# Start the Tkinter loop
window.mainloop()
