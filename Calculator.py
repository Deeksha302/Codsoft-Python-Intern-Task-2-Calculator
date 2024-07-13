import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.create_widgets()

    def create_widgets(self):
        # Create input fields for numbers
        self.label1 = tk.Label(self.root, text="Enter first number:")
        self.label1.pack()

        self.num1_entry = tk.Entry(self.root)
        self.num1_entry.pack()

        self.label2 = tk.Label(self.root, text="Enter second number:")
        self.label2.pack()

        self.num2_entry = tk.Entry(self.root)
        self.num2_entry.pack()

        # Create dropdown menu for operations
        self.operations = ["Add", "Subtract", "Multiply", "Divide"]
        self.operation_var = tk.StringVar(self.root)
        self.operation_var.set(self.operations[0])

        self.label3 = tk.Label(self.root, text="Choose operation:")
        self.label3.pack()

        self.operation_menu = tk.OptionMenu(self.root, self.operation_var, *self.operations)
        self.operation_menu.pack()

        # Create button to perform calculation
        self.calc_button = tk.Button(self.root, text="Calculate", command=self.calculate)
        self.calc_button.pack()

        # Create label to display result
        self.result_label = tk.Label(self.root, text="Result:")
        self.result_label.pack()

    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            operation = self.operation_var.get()

            if operation == "Add":
                result = num1 + num2
            elif operation == "Subtract":
                result = num1 - num2
            elif operation == "Multiply":
                result = num1 * num2
            elif operation == "Divide":
                if num2 != 0:
                    result = num1 / num2
                else:
                    messagebox.showerror("Error", "Cannot divide by zero.")
                    return
            else:
                result = "Invalid Operation"

            self.result_label.config(text=f"Result: {result}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
