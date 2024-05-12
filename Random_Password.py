import string
import random
import tkinter as tk
from tkinter import messagebox


class Password_Generator:

    def __init__(self):
        # Initialize the Password_Generator class
        self.string = []
        # Create a list of printable characters
        for i in range(0, 94):
            self.string.append(string.printable[i])

        # Shuffle the list of printable characters
        random.shuffle(self.string)
        # Initialize an empty password list
        self.password = []

    def get_pass(self, pass_len):
        # Shuffle the list of printable characters each time get_pass is called
        random.shuffle(self.string)
        # Reset the password list to an empty state
        self.password = []

        if 0 < pass_len <= 94:
            # Generate a password of the specified length
            for i in range(0, pass_len):
                self.password.append(self.string[i])
            return self.password
        elif pass_len > 94:
            raise ValueError(
                "Sorry! the password length is too large, kindly choose a smaller length")
        else:
            raise ValueError("Invalid Input")


class Password_Generator_App:

    def __init__(self, master):
        # Initialize the Password_Generator_App class
        self.master = master
        self.master.title("Password Generator")

        # Create an instance of the Password_Generator class
        self.password_generator = Password_Generator()

        # Set up the GUI components
        self.widgets()

    def widgets(self):
        # Create and configure GUI components
        tk.Label(
            self.master,
            text="Enter The Length Of Password:",
            font=("Helvetica", 10, "bold"),
            padx=75,
            pady=6,
        ).grid(row=0, column=0, sticky="e")

        self.length_entry = tk.Entry(
            self.master,
            width=18,
            font=("Helvetica", 12, "italic"),
        )

        self.length_entry.grid(row=0, column=1, padx=10, ipadx=10, ipady=6)

        generate_pass_button = tk.Button(
            self.master,
            text="Generate",
            command=self.generate,
            bg="pink",
            fg="#63017a",
            font=("Helvetica", 14),
        )
        generate_pass_button.grid(row=1, column=0, columnspan=2, pady=10)

    def generate(self):
        # Get the desired password length from the user input
        pass_len_str = self.length_entry.get()

        try:
            # Checking wheater input is int type or not
            pass_len = int(pass_len_str)
            # Generate a password using the Password_Generator instance
            generated_password = self.password_generator.get_pass(pass_len)
            # Display the generated password in a dialog
            self.show_password_dialog(
                "Generated Password", "".join(generated_password))
        except ValueError as e:
            # Display an error message if an invalid value is entered
            messagebox.showerror("Error", str(e))
        except Exception as e:
            # Display an error message for unexpected errors
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

    def show_password_dialog(self, title, password_text):
        # Create a dialog to display the generated password
        password_dialog = tk.Toplevel(self.master)
        password_dialog.title(title)

        # Create a Text widget to display the password
        password_text_widget = tk.Text(
            password_dialog, wrap=tk.WORD, height=5, width=30)
        password_text_widget.insert(tk.END, password_text)
        password_text_widget.config(state=tk.DISABLED)
        password_text_widget.pack(padx=10, pady=10)


def main():
    try:
        # Create the main Tkinter window and run the application
        root = tk.Tk()
        app = Password_Generator_App(root)
        root.mainloop()
    except Exception as e:
        # Handle unexpected errors and display a message
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
