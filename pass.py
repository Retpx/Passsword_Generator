import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length=12):
    """
    Generate a random password.
    
    A secure password should have a mix of characters. This function ensures
    at least one lowercase, one uppercase, one digit, and one punctuation mark.
    """
    if length < 4:
        raise ValueError("Password ki lambai kam se kam 4 aksharon ki honi chahiye.")
    
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    password += random.choices(all_characters, k=length - 4)
    random.shuffle(password)
    
    return ''.join(password)

def create_gui():
    """
    Creates and runs the GUI for the password generator.
    """
    def on_generate_click():
        """Handles the button click event to generate a password."""
        try:
            length = int(length_entry.get())
            password = generate_password(length)
            password_entry.delete(0, tk.END)  # Pichle password ko saaf karen
            password_entry.insert(0, password)  # Naya password dalen
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def on_copy_click():
        """Copies the generated password to the clipboard."""
        try:
            password = password_entry.get()
            if password:
                root.clipboard_clear()
                root.clipboard_append(password)
                messagebox.showinfo("Success", "Password copy has been successfully!")
            else:
                messagebox.showwarning("Warning", "You have a no password of copy")
        except Exception as e:
            messagebox.showerror("Error", f"Copy karne mein dikkat: {e}")

    # Main window
    root = tk.Tk()
    root.title("Password Generator")
    root.geometry("400x250")
    root.resizable(False, False)

    # Widgets
    label_length = tk.Label(root, text="Password ki Lambai:", font=("Arial", 12))
    label_length.grid(row=0, column=0, padx=10, pady=10)

    length_entry = tk.Entry(root, width=10, font=("Arial", 12))
    length_entry.grid(row=0, column=1, padx=10, pady=10)
    length_entry.insert(0, "12") # Default password length

    button_generate = tk.Button(root, text="Password Banayen", command=on_generate_click, font=("Arial", 12))
    button_generate.grid(row=1, columnspan=2, padx=10, pady=10)

    label_password = tk.Label(root, text="Generated Password:", font=("Arial", 12))
    label_password.grid(row=2, column=0, padx=10, pady=10)
    
    password_entry = tk.Entry(root, width=30, font=("Courier", 14), relief="solid")
    password_entry.grid(row=2, column=1, padx=10, pady=10)

    button_copy = tk.Button(root, text="Copy karen", command=on_copy_click, font=("Arial", 12))
    button_copy.grid(row=3, columnspan=2, padx=10, pady=10)

    # Start the GUI loop
    root.mainloop()

# Yeh line joadi gayi hai. Yeh create_gui() function ko shuru karti hai.
if __name__ == "__main__":
    create_gui()
