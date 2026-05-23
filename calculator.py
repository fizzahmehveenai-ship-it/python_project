import tkinter as tk

window = tk.Tk()
window.title("Pro Calculator")
window.geometry("300x300")

entry1 = tk.Entry(window)
entry1.pack(pady=5)

entry2 = tk.Entry(window)
entry2.pack(pady=5)

result_label = tk.Label(window, text="Result will appear here")
result_label.pack(pady=5)

def calculator(op):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if op == "Add":
            result = num1 + num2

        elif op == "Subtract":
            result = num1 - num2

        elif op == "Multiply":
            result = num1 * num2

        elif op == "Divide":
            if num2 == 0:
                result_label.config(text="Cannot divide by zero")
                return
            result = num1 / num2

        result_label.config(text="Result: " + str(result))

    except ValueError:
        result_label.config(text="Enter valid numbers")

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Result will appear here")

frame = tk.Frame(window)
frame.pack(pady=5)

tk.Button(frame, text="Add", command=lambda: calculator("Add")).pack(side=tk.LEFT, padx=5)
tk.Button(frame, text="Subtract", command=lambda: calculator("Subtract")).pack(side=tk.LEFT, padx=5)
tk.Button(frame, text="Multiply", command=lambda: calculator("Multiply")).pack(side=tk.LEFT, padx=5)
tk.Button(frame, text="Divide", command=lambda: calculator("Divide")).pack(side=tk.LEFT, padx=5)

tk.Button(window, text="Clear", command=clear).pack(pady=10)

window.mainloop()