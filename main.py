import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Quote of the Day")
root.geometry("500x300")
root.resizable(False, False)
root.configure(bg="white")

# === Quote text variable ===
quote_var = tk.StringVar(value="💬 Need a little motivation?\nClick the button!")

# === Welcome Label ===
quote_label = tk.Label(
    root,
    textvariable=quote_var,
    wraplength=440,
    justify="center",
    font=("Helvetica", 16),
    bg="white",
    fg="#333333",
    padx=20,
    pady=20
)
quote_label.pack(pady=(40, 20))

# === Get Quote Button ===
get_quote_button = tk.Button(
    root,
    text="💡 Inspire Me",
    font=("Helvetica", 13, "bold"),
    bg="#007acc",
    fg="white",
    activebackground="#005f99",
    activeforeground="white",
    relief="flat",
    padx=15,
    pady=8,
    command=lambda: quote_var.set("This is where the quote will go!")
)
get_quote_button.pack(pady=10)

#Start the main event loop
root.mainloop()
# End of the code
# This is a simple Tkinter application that displays a quote of the day.
# The user can click the button to get a new quote.
# The application is designed to be user-friendly and visually appealing.