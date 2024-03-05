import tkinter


# Calculate button function
def convert_to_km():
    miles = miles_variable.get()
    kms = miles * 1.609
    result_label.config(text=kms)


# Window setup
window = tkinter.Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=30, pady=25)

# input field for users to enter a number of miles, saved to miles_variable for future calculation
miles_variable = tkinter.IntVar()
miles_variable.set(0)
miles_input = tkinter.Entry(width=6, textvariable=miles_variable)
miles_input.grid(row=0, column=2)

# Entry label
top_text = tkinter.Label(text="Miles")
top_text.grid(row=0, column=3)

# Result labels
result_text_label = tkinter.Label(text="is equal to: ")
result_label = tkinter.Label(text="0")
km_label = tkinter.Label(text="Km")
result_text_label.grid(row=1, column=0)
result_label.grid(row=1, column=2)
km_label.grid(row=1, column=3)

# Calculate button
button = tkinter.Button(text="Calculate", command=convert_to_km)
button.grid(row=2, column=2)

window.mainloop()
