from tkinter import *
import InterfaceHelper


root = Tk()
root.rowconfigure(0, weight = 1)
root.columnconfigure(0, weight = 1)
root.title("WOW Statistical Probability Tracker")

# Scroll Bar
scrollbar = Scrollbar(root).grid(column = 5)

# Complement checkbox
complement_value = BooleanVar()
complement_checkbox = Checkbutton(root, text ="Complement", variable = complement_value)
complement_checkbox.grid(row = 0, column = 4, sticky = E)
# Column 4 is the complement checkbox
root.grid_columnconfigure(4, weight = 1)
# Row 0 is the complement checkbox
root.grid_rowconfigure(0, weight = 0)


# Burning Crusade -----------------------------------------------------------------------------------------------------
burning_crusade_mounts = ["Karazhan - Fiery Warhorse",
                          "The Eye - Ashes of Al'ar"]
InterfaceHelper.generate_widgets(root, 1, 0, "Burning Crusade", burning_crusade_mounts, complement_value)


# Wrath of the Lich King ----------------------------------------------------------------------------------------------
lich_king_mounts = ["Vault of Archavon - Grand Black War Mammoth",
                    "The Eye of Eternity - Azure Drake",
                    "The Eye of Eternity - Blue Drake",
                    "Onyxia's Lair - Onyxian Drake",
                    "Ulduar - Mimiron's Head",
                    "Icecrown Citadel - Invincible"]
InterfaceHelper.generate_widgets(root, 2, 0, "Wrath of the Lich King", lich_king_mounts, complement_value)


# Cataclysm ----------------------------------------------------------------------------------------------
cataclysm_mounts = ["Throne of the Four Winds - Drake of the South Wind",
                    "Firelands - Flametalon of Alysrazor",
                    "Firelands - Pureblood Fire Hawk",
                    "Dragon Soul - Experiment 12-B",
                    "Dragon Soul - Blazing Drake",
                    "Dragon Soul - Life-Binder's Handmaiden"]
InterfaceHelper.generate_widgets(root, 3, 0, "Cataclysm", cataclysm_mounts, complement_value)


root.mainloop()
