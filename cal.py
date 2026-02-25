from tkinter import *

# Window
root = Tk()
root.title("My Calculator")
root.geometry("362x380")
root.configure(bg="#000000")
root.resizable(False, False)

# Entry display
entry = Entry(
    root,
    width=16,
    font=("Arial", 28),
    borderwidth=0,
    bg="#2d2d2d",
    fg="white",
    justify="right"
)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=10)

# Functions
def click(value):
    entry.insert(END, value)

def clear():
    entry.delete(0, END)

def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Button style
btn_style = {
    "font": ("Arial", 14),
    "width": 5,
    "height": 2,
    "bd": 0,
    "fg": "white",
    "bg": "#3a3a3a",
    "activebackground": "#505050"
}

op_style = {
    "font": ("Arial", 14),
    "width": 5,
    "height": 2,
    "bd": 0,
    "fg": "white",
    "bg": "#ff9500",
    "activebackground": "#ffaa33"
}

# Row 1
Button(root, text="7", command=lambda: click("7"), **btn_style).grid(row=1, column=0, pady=5)
Button(root, text="8", command=lambda: click("8"), **btn_style).grid(row=1, column=1)
Button(root, text="9", command=lambda: click("9"), **btn_style).grid(row=1, column=2)
Button(root, text="/", command=lambda: click("/"), **op_style).grid(row=1, column=3)

# Row 2
Button(root, text="4", command=lambda: click("4"), **btn_style).grid(row=2, column=0, pady=5)
Button(root, text="5", command=lambda: click("5"), **btn_style).grid(row=2, column=1)
Button(root, text="6", command=lambda: click("6"), **btn_style).grid(row=2, column=2)
Button(root, text="", command=lambda: click(""), **op_style).grid(row=2, column=3)

# Row 3
Button(root, text="1", command=lambda: click("1"), **btn_style).grid(row=3, column=0, pady=5)
Button(root, text="2", command=lambda: click("2"), **btn_style).grid(row=3, column=1)
Button(root, text="3", command=lambda: click("3"), **btn_style).grid(row=3, column=2)
Button(root, text="-", command=lambda: click("-"), **op_style).grid(row=3, column=3)

# Row 4
Button(root, text="0", command=lambda: click("0"), **btn_style).grid(row=4, column=0, pady=5)
Button(root, text="C", command=clear, bg="#ff3b30", fg="white",
       font=("Arial", 14), width=5, height=2, bd=0).grid(row=4, column=1)
Button(root, text="=", command=equal, bg="#34c759", fg="white",
       font=("Arial", 14), width=5, height=2, bd=0).grid(row=4, column=2)
Button(root, text="+", command=lambda: click("+"), **op_style).grid(row=4, column=3)

root.mainloop()