from tkinter import *
import InterfaceHelper

root = Tk()
root.rowconfigure(0, weight = 1)
root.columnconfigure(0, weight = 1)
root.title("WOW Statistical Probability Tracker")

# Complement checkbox
complement_checkbox = BooleanVar()
Checkbutton(root, text ="Complement", variable = complement_checkbox).grid(column = 4, row = 0, sticky = E)
# Column 4 is the complement checkbox
root.grid_columnconfigure(4, weight = 1)
# Row 0 is the complement checkbox
root.grid_rowconfigure(0, weight = 0)


# Burning Crusade -----------------------------------------------------------------------------------------------------
bc_frame = LabelFrame(root, text = "Burning Crusade", font=("Arial Narrow", 18), padx = 5, pady = 5)
bc_frame.grid(row = 1, column = 0, rowspan = 2, columnspan = 4, padx = 10, pady = 10, sticky = N + S + E + W)


# Fiery Warhorse
fiery_warhorse_label = Label(bc_frame, text = "Karazhan - Fiery Warhorse", font=("Arial Narrow", 12))
fiery_warhorse_label.grid(column = 0, row = 0, sticky = W)

fiery_warhorse_attempts = StringVar()
fiery_warhorse_attempts.set(InterfaceHelper.load_attempts("Fiery Warhorse"))

fiery_warhorse_spin = Spinbox(bc_frame, from_ = 0, to = 255, width = 5, textvariable = fiery_warhorse_attempts)
fiery_warhorse_spin.grid(column = 1, row = 0)

# spinbox.get() always return a string
Button(bc_frame,
       text = "Calculate",
       command = lambda: InterfaceHelper.open_and_save("Karazhan - Fiery Warhorse",
                                                       "Fiery Warhorse",
                                                       int(fiery_warhorse_spin.get()),
                                                       complement_checkbox.get())
       ).grid(column = 2, row = 0)


# Ashes of Al'ar
ashes_alar_label = Label(bc_frame, text = "The Eye - Ashes of Al'ar", font=("Arial Narrow", 12))
ashes_alar_label.grid(column = 0, row = 1, sticky = W)

ashes_alar_attempts = StringVar()
ashes_alar_attempts.set(InterfaceHelper.load_attempts("Ashes of Al'ar"))

ashes_alar_spin = Spinbox(bc_frame, from_ = 0, to = 255, width = 5, textvariable = ashes_alar_attempts)
ashes_alar_spin.grid(column = 1, row = 1)

# spinbox.get() always return a string
Button(bc_frame,
       text = "Calculate",
       command = lambda: InterfaceHelper.open_and_save("The Eye - Ashes of Al'ar",
                                                       "Ashes of Al'ar",
                                                       int(ashes_alar_spin.get()),
                                                       complement_checkbox.get())
       ).grid(column = 2, row = 1)


# Burning Crusade Weights

# BC FrameFrame
root.rowconfigure(1, weight = 1)
root.columnconfigure(0, weight = 1)

# Row 0 is Fiery Warhorse, Row 1 is Ashes of Al'ar
bc_frame.rowconfigure(0, weight = 1)
bc_frame.rowconfigure(1, weight = 1)

# Column 0 is label, column 1 is spinbox, column 2 is button
bc_frame.columnconfigure(0, weight = 1)
bc_frame.columnconfigure(1, weight = 1)
bc_frame.columnconfigure(2, weight = 1)


# Wrath of the Lich King ----------------------------------------------------------------------------------------------
wotlk_frame = LabelFrame(root, text = "Wrath of the Lich King", font=("Arial Narrow", 18), padx = 5, pady = 5)
wotlk_frame.grid(row = 3, column = 0, rowspan = 1, columnspan = 4, padx = 10, pady = 10, sticky = N + S + E + W)


# Invincible
invincible_label = Label(wotlk_frame, text = "Icecrown Citadel - Invincible", font=("Arial Narrow", 12))
invincible_label.grid(column = 0, row = 0, sticky = W)

invincible_attempts = StringVar()
invincible_attempts.set(InterfaceHelper.load_attempts("Invincible"))

invincible_spin = Spinbox(wotlk_frame, from_ = 0, to = 255, width = 5, textvariable = invincible_attempts)
invincible_spin.grid(column = 1, row = 0)

# spinbox.get() always return a string
Button(wotlk_frame,
       text = "Calculate",
       command = lambda: InterfaceHelper.open_and_save("Icecrown Citadel - Invincible",
                                                       "Invincible",
                                                       int(invincible_spin.get()),
                                                       complement_checkbox.get())
       ).grid(column = 2, row = 0)


# Wrath of the Lich King

# WotLK FrameFrame
root.rowconfigure(3, weight = 1)
root.columnconfigure(0, weight = 1)

# Row 0 is Fiery Warhorse, Row 1 is Ashes of Al'ar
wotlk_frame.rowconfigure(0, weight = 1)
wotlk_frame.rowconfigure(1, weight = 1)

# Column 0 is label, column 1 is spinbox, column 2 is button
wotlk_frame.columnconfigure(0, weight = 1)
wotlk_frame.columnconfigure(1, weight = 1)
wotlk_frame.columnconfigure(2, weight = 1)


# root.geometry('250x250')
root.mainloop()
