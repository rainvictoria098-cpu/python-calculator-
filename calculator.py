import tkinter as tk
from tkinter import messagebox


# -----------------------------
# FUNCTIONS
# -----------------------------

def get_numbers():
    """Get the two numbers typed by the user."""

    try:
        first_number = float(first_number_entry.get())
        second_number = float(second_number_entry.get())

        return first_number, second_number

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numbers."
        )

        return None, None


def calculate(operation):
    """Calculate the answer based on the selected operation."""

    first_number, second_number = get_numbers()

    if first_number is None or second_number is None:
        return

    if operation == "add":
        answer = first_number + second_number

    elif operation == "subtract":
        answer = first_number - second_number

    elif operation == "multiply":
        answer = first_number * second_number

    elif operation == "divide":

        if second_number == 0:
            messagebox.showerror(
                "Math Error",
                "You cannot divide a number by zero."
            )
            return

        answer = first_number / second_number

    result_label.config(text=f"Result: {answer:g}")


def clear_fields():
    """Remove everything from the input boxes."""

    first_number_entry.delete(0, tk.END)
    second_number_entry.delete(0, tk.END)

    result_label.config(text="Result: 0")

    first_number_entry.focus()


# -----------------------------
# MAIN WINDOW
# -----------------------------

window = tk.Tk()

window.title("Rain's Python Calculator")
window.geometry("500x580")
window.resizable(False, False)
window.configure(bg="#EEF2FF")


# -----------------------------
# HEADER
# -----------------------------

header = tk.Frame(
    window,
    bg="#4F46E5",
    height=110
)

header.pack(fill="x")

title_label = tk.Label(
    header,
    text="Python Calculator",
    font=("Arial", 24, "bold"),
    bg="#4F46E5",
    fg="white"
)

title_label.pack(pady=(20, 5))

subtitle_label = tk.Label(
    header,
    text="A beginner project by Rain Victoria",
    font=("Arial", 11),
    bg="#4F46E5",
    fg="#E0E7FF"
)

subtitle_label.pack()


# -----------------------------
# MAIN CARD
# -----------------------------

card = tk.Frame(
    window,
    bg="white",
    padx=35,
    pady=30,
    highlightbackground="#D1D5DB",
    highlightthickness=1
)

card.pack(padx=35, pady=30, fill="both", expand=True)

first_number_label = tk.Label(
    card,
    text="First Number",
    font=("Arial", 11, "bold"),
    bg="white",
    fg="#374151"
)

first_number_label.pack(anchor="w")

first_number_entry = tk.Entry(
    card,
    font=("Arial", 16),
    justify="center",
    bd=1,
    relief="solid"
)

first_number_entry.pack(fill="x", ipady=8, pady=(5, 15))

second_number_label = tk.Label(
    card,
    text="Second Number",
    font=("Arial", 11, "bold"),
    bg="white",
    fg="#374151"
)

second_number_label.pack(anchor="w")

second_number_entry = tk.Entry(
    card,
    font=("Arial", 16),
    justify="center",
    bd=1,
    relief="solid"
)

second_number_entry.pack(fill="x", ipady=8, pady=(5, 20))


# -----------------------------
# BUTTONS
# -----------------------------

button_frame = tk.Frame(card, bg="white")
button_frame.pack(fill="x")

add_button = tk.Button(
    button_frame,
    text="Add  +",
    font=("Arial", 11, "bold"),
    bg="#22C55E",
    fg="white",
    activebackground="#16A34A",
    cursor="hand2",
    command=lambda: calculate("add")
)

add_button.grid(row=0, column=0, padx=5, pady=5, ipadx=15, ipady=8)

subtract_button = tk.Button(
    button_frame,
    text="Subtract  −",
    font=("Arial", 11, "bold"),
    bg="#F59E0B",
    fg="white",
    activebackground="#D97706",
    cursor="hand2",
    command=lambda: calculate("subtract")
)

subtract_button.grid(row=0, column=1, padx=5, pady=5, ipadx=10, ipady=8)

multiply_button = tk.Button(
    button_frame,
    text="Multiply  ×",
    font=("Arial", 11, "bold"),
    bg="#3B82F6",
    fg="white",
    activebackground="#2563EB",
    cursor="hand2",
    command=lambda: calculate("multiply")
)

multiply_button.grid(row=1, column=0, padx=5, pady=5, ipadx=10, ipady=8)

divide_button = tk.Button(
    button_frame,
    text="Divide  ÷",
    font=("Arial", 11, "bold"),
    bg="#8B5CF6",
    fg="white",
    activebackground="#7C3AED",
    cursor="hand2",
    command=lambda: calculate("divide")
)

divide_button.grid(row=1, column=1, padx=5, pady=5, ipadx=15, ipady=8)

button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)


# -----------------------------
# RESULT
# -----------------------------

result_label = tk.Label(
    card,
    text="Result: 0",
    font=("Arial", 20, "bold"),
    bg="#EEF2FF",
    fg="#4338CA",
    pady=15
)

result_label.pack(fill="x", pady=(20, 10))

clear_button = tk.Button(
    card,
    text="Clear",
    font=("Arial", 11, "bold"),
    bg="#EF4444",
    fg="white",
    activebackground="#DC2626",
    cursor="hand2",
    command=clear_fields
)

clear_button.pack(fill="x", ipady=8)

first_number_entry.focus()

window.mainloop()
