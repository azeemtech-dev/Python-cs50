import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO

def on_validate_click():
    plate = entry.get()
    if is_valid(plate):
        result_label.config(text="Valid", fg="green")
    else:
        result_label.config(text="Invalid", fg="red")

def is_valid(s):
    return (is_correct_length(s) and 
            starts_with_two_letters(s) and 
            no_invalid_characters(s) and 
            valid_number_usage(s))

def is_correct_length(s):
    return 2 <= len(s) <= 6

def starts_with_two_letters(s):
    return s[:2].isalpha()

def no_invalid_characters(s):
    return all(c.isalnum() for c in s)

def valid_number_usage(s):
    num_started = False
    for i, c in enumerate(s):
        if c.isdigit():
            if i == 0:
                return False  # Number at the start
            if not num_started:
                if c == '0':
                    return False  # First number is '0'
                num_started = True
        elif num_started:
            return False  # Letter after number
    return True

# Function to fetch image from URL
def fetch_image(url):
    try:
        response = requests.get(url)
        image_data = response.content
        image = Image.open(BytesIO(image_data))
        image = image.resize((100, 100), Image.ANTIALIAS)
        return ImageTk.PhotoImage(image)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch image: {e}")
        return None

# Create the main window
root = tk.Tk()
root.title("License Plate Validator")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

# URL of the image to display (replace with your image URL)
image_url = "https://example.com/your_image.png"  # Replace with your actual image URL

# Load image from URL
photo = fetch_image(image_url)
if photo:
    image_label = tk.Label(root, image=photo, bg="#f0f0f0")
    image_label.pack(pady=10)

# Create a label for instruction
instruction_label = tk.Label(root, text="Enter the license plate:", font=("Helvetica", 12), bg="#f0f0f0")
instruction_label.pack(pady=5)

# Create an entry widget
entry = tk.Entry(root, width=30, font=("Helvetica", 12))
entry.pack(pady=5)

# Create a button to validate
validate_button = tk.Button(root, text="Validate", command=on_validate_click, bg="#4CAF50", fg="white", font=("Helvetica", 12))
validate_button.pack(pady=5)

# Create a label to display the result
result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#f0f0f0")
result_label.pack(pady=10)
                          
# Run the application
root.mainloop()
