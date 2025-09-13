# Passsword_Generator
This code creates a Graphical User Interface (GUI) for a password generator using Python's built-in tkinter library. It's a single, self-contained file that combines the password generation logic with a user-friendly interface.

How the Code Works
1. Password Generation Logic
The generate_password(length=12) function is the core of the app. It's designed to create strong passwords by:

Ensuring security: It makes sure the password is at least 4 characters long.

Mixing characters: It guarantees that the password includes at least one lowercase letter, one uppercase letter, one digit, and one punctuation mark. The rest of the password is filled with a random mix of all characters.

Randomizing: It uses random.choices to pick characters and random.shuffle to mix them up, ensuring the password is unpredictable.

2. GUI Setup
The create_gui() function handles all the visual elements.

Main Window: tk.Tk() creates the main application window, and root.title() sets its title.

Widgets: The code uses several tkinter widgets:

tk.Label: Displays text like "Password ki Lambai:" and "Generated Password:".

tk.Entry: Creates input fields for the user to enter the desired password length and to display the generated password.

tk.Button: Creates clickable buttons for "Password Banayen" (Generate Password) and "Copy karen" (Copy to Clipboard).

3. Button Actions
The code uses functions (on_generate_click and on_copy_click) to handle what happens when a button is clicked.

Generate Button: on_generate_click() reads the number from the length input field, calls the generate_password() function, and then displays the new password in the password entry field. It also includes error handling to catch non-numeric input.

Copy Button: on_copy_click() gets the text from the password field and copies it to the system's clipboard, showing a success message to the user.

4. Running the App
The if __name__ == "__main__": block is a standard Python practice. It ensures that the create_gui() function is called only when the script is run directly, not when it's imported as a module into another script. This is what makes the GUI window pop up when you run the file in VS Code.
