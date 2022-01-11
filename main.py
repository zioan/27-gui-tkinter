import tkinter
from tkinter.constants import Y


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


window = tkinter.Tk()
window.title("First GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)  # add padding to the window


# Label
my_label = tkinter.Label(text="This is a label", font=("Arial", 22, "normal"))
my_label["text"] = "New text"
my_label.config(text="Label changed again")
# my_label.pack()  # put the label on the window
# my_label.place(x=0, y=150)
my_label.grid(column=0, row=0)
my_label.config(padx=30, pady=30)

# Button
button = tkinter.Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)


# Entry (input)
input = tkinter.Entry(width=20)
print(input.get())
input.grid(column=3, row=2)

# Layouts
"""
pack() - basic layout manager, align the elements one after another
place(x=0, y=123) - percise positioning in px
grid(column=2, row=0) - is a relative position system (relative to other elements)
    - specify the position based on a grid system
    - start with column=0 row=0 and is spreading based on the elements asigned

### Cannot mix layout systems inside a program !!!
"""

button2 = tkinter.Button(text="New button")
button2.grid(column=2, row=0)

window.mainloop()  # keeps the window open
