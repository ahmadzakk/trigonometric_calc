import math
import tkinter as tk
from tkinter import Label, Entry, Button, Text

# Define the TrigonometricCalculator class
class TrigonometricCalculator:
    def __init__(self, entry):
        # Initialize the TrigonometricCalculator instance with an entry widget
        self.entry = entry
        self.angle_degrees = None
        self.angle_radians = None

    def get_angle_from_user(self):
        try:
            # Get the angle in degrees from the entry widget and convert to radians
            self.angle_degrees = float(self.entry.get())
            self.angle_radians = math.radians(self.angle_degrees)
        except ValueError:
            # Handle invalid input by printing an error message
            print("Invalid input. Please enter a valid number.")

    def calculate_trigonometric_functions(self):
        if self.angle_degrees == 0:
            # If the angle is 0, return None
            return None

        # Calculate various trigonometric functions
        trig_results = {
            "Sine": math.sin(self.angle_radians),
            "Cosine": math.cos(self.angle_radians),
            "Tangent": math.tan(self.angle_radians),
            "Cosecant": 1 / math.sin(self.angle_radians),
            "Secant": 1 / math.cos(self.angle_radians),
            "Cotangent": 1 / math.tan(self.angle_radians)
        }

        return trig_results

# Define the function to calculate and display results
def calculate_and_display():
    calculator.get_angle_from_user()
    trig_results = calculator.calculate_trigonometric_functions()

    if trig_results is not None:
        # Display the results in the result_text widget
        result_text.config(state=tk.NORMAL)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"Degrees: {calculator.angle_degrees}\nRadians: {calculator.angle_radians}\n"
                                   f"Sine: {trig_results['Sine']:.4f}\nCosine: {trig_results['Cosine']:.4f}\n"
                                   f"Tangent: {trig_results['Tangent']:.4f}\nCosecant: {trig_results['Cosecant']:.4f}\n"
                                   f"Secant: {trig_results['Secant']:.4f}\nCotangent: {trig_results['Cotangent']:.4f}")
        result_text.config(state=tk.DISABLED)

    # Append results to the results_list
    results_list.append({
        "Degrees": calculator.angle_degrees,
        "Radians": calculator.angle_radians,
        **trig_results
    })

    # Write results to the trigonometric_results.txt file
    with open("trigonometric_results.txt", "w") as file:
        file.write("Degrees\tRadians\tSine\tCosine\tTangent\tCosecant\tSecant\tCotangent\n")
        for result in results_list:
            file.write(f"{result['Degrees']:.2f}\t{result['Radians']:.2f}\t")
            file.write(f"{result['Sine']:.4f}\t{result['Cosine']:.4f}\t{result['Tangent']:.4f}\t")
            file.write(f"{result['Cosecant']:.4f}\t{result['Secant']:.4f}\t{result['Cotangent']:.4f}\n")

# Define the function to exit the application
def on_exit():
    root.destroy()

# Create the main Tkinter window
root = tk.Tk()
root.title("Trigonometric Calculator")

# Create a label for user instructions
label = Label(root, text="Enter an angle in degrees:")
label.pack()

# Create an entry widget for user input
entry = Entry(root)
entry.pack()

# Create an instance of TrigonometricCalculator, passing the entry widget
calculator = TrigonometricCalculator(entry)

# Create a button to trigger the calculation and display of results
calculate_button = Button(root, text="Calculate", command=calculate_and_display)
calculate_button.pack()

# Create a Text widget to display results (read-only)
result_text = Text(root, height=10, width=50, state=tk.DISABLED)
result_text.pack()

# Create a button to exit the application
exit_button = Button(root, text="Exit", command=on_exit)
exit_button.pack()

# Initialize an empty list to store results
results_list = []

# Start the Tkinter event loop
root.mainloop()
print("test")
