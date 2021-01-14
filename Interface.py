import tkinter
import InterfaceHelper


master = tkinter.Tk()
master.title("WOW Statistical Probability Tracker")


# Code for the complement checkbox
complement_checkbox = tkinter.BooleanVar()
tkinter.Checkbutton(master, text = "Complement", variable = complement_checkbox).grid(column = 4, row = 1)


# Below is the code that is generating the current tkinter window
var = tkinter.StringVar()
var.set(InterfaceHelper.load_attempts("Invincible"))
spin = tkinter.Spinbox(master, from_ = 0, to = 100, width = 10, textvariable = var)
spin.grid(column = 1, row = 0)

# spinbox.get() always return a string
tkinter.Button(master,
               text = "Click Me!",
               command = lambda: InterfaceHelper.open_and_save("Invincible", "Invincible", int(spin.get()),
                                                               complement_checkbox.get())
               ).grid(column = 2, row = 2)
master.geometry('250x250')
master.mainloop()
