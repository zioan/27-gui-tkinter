import tkinter

window = tkinter.Tk()
# window.config(width=500, height=350)
window.title("Mile to Km converter")
window.config(padx=20, pady=20)


def convert():
    result = float(input.get()) * 1.609
    label_result.config(text=round(result, 2))


input = tkinter.Entry(width=5)
input.grid(column=1, row=0)

label_miles = tkinter.Label(text="Miles")
label_miles.grid(column=2, row=0)

label_equal_to = tkinter.Label(text="is equal to", padx=0, pady=10)
label_equal_to.grid(column=0, row=1)

label_result = tkinter.Label(text="0", padx=0, pady=10)
label_result.grid(column=1, row=1)

label_km = tkinter.Label(text="Km")
label_km.grid(column=2, row=1)

button = tkinter.Button(text="Calculate", padx=10, pady=5, command=convert)
button.grid(column=1, row=2)


window.mainloop()
