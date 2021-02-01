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

button_frame = LabelFrame(root, highlightbackground = "black", highlightthickness = 1)
button_frame.grid(row = 1, column = 0, sticky = N + E + S + W)
button_frame.columnconfigure(0, weight = 1)

mount_frame = Frame(root, highlightbackground = "black", highlightthickness = 1)
mount_frame.grid(row = 1, column = 1, sticky = N + E + S + W)


# Burning Crusade ------------------------------------------------------------------------------------------------------
burning_crusade_mounts = ["Karazhan - Fiery Warhorse",
                          "The Eye - Ashes of Al'ar"]

burning_crusade_frame = InterfaceHelper.generate_widgets(mount_frame,
                                                         "Burning Crusade",
                                                         burning_crusade_mounts,
                                                         complement_value)

burning_crusade_button = Button(button_frame,
                                text = "The Burning Crusade",
                                command = lambda: burning_crusade_frame.tkraise())
burning_crusade_button.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = W)

# Wrath of the Lich King -----------------------------------------------------------------------------------------------
lich_king_mounts = ["Vault of Archavon - Grand Black War Mammoth",
                    "The Eye of Eternity - Azure Drake",
                    "The Eye of Eternity - Blue Drake",
                    "Onyxia's Lair - Onyxian Drake",
                    "Ulduar - Mimiron's Head",
                    "Icecrown Citadel - Invincible"]

lich_king_frame = InterfaceHelper.generate_widgets(mount_frame,
                                                   "Wrath of the Lich King",
                                                   lich_king_mounts,
                                                   complement_value)

lich_king_button = Button(button_frame,
                          text = "Wrath of the Lich King",
                          command = lambda: lich_king_frame.tkraise())
lich_king_button.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = W)

# Cataclysm ------------------------------------------------------------------------------------------------------------
cataclysm_mounts = ["Throne of the Four Winds - Drake of the South Wind",
                    "Firelands - Flametalon of Alysrazor",
                    "Firelands - Pureblood Fire Hawk",
                    "Dragon Soul - Experiment 12-B",
                    "Dragon Soul - Blazing Drake",
                    "Dragon Soul - Life-Binder's Handmaiden"]

cataclysm_frame = InterfaceHelper.generate_widgets(mount_frame,
                                                   "Cataclysm",
                                                   cataclysm_mounts,
                                                   complement_value)

cataclysm_button = Button(button_frame,
                          text = "Cataclysm",
                          command = lambda: cataclysm_frame.tkraise())
cataclysm_button.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = W)

# Mists of Pandaria ----------------------------------------------------------------------------------------------------
pandaria_mounts = ["Mogu'shan Vault - Astral Cloud Serpent",
                   "Throne of Thunder - Spawn of Horridon",
                   "Throne of Thunder - Clutch of Ji-Kun",
                   "Siege of Orgrimmar - Kor'kron Juggernaut"]

pandaria_frame = InterfaceHelper.generate_widgets(mount_frame,
                                                  "Mists of Pandaria",
                                                  pandaria_mounts,
                                                  complement_value)

pandaria_button = Button(button_frame,
                         text = "Mists of Pandaria",
                         command = lambda: pandaria_frame.tkraise())
pandaria_button.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = W)

# Warlords of Draenor --------------------------------------------------------------------------------------------------
draenor_mounts = ["Blackrock Foundry - Ironhoof Destroyer",
                  "Hellfire Citadel - Felsteel Annihilator"]

draenor_frame = InterfaceHelper.generate_widgets(mount_frame,
                                                 "Warlords of Draenor",
                                                 draenor_mounts,
                                                 complement_value)

draenor_button = Button(button_frame, text = "Warlords of Draenor", command = lambda: draenor_frame.tkraise())
draenor_button.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = W)

# Legion ---------------------------------------------------------------------------------------------------------------
legion_mounts = ["The Nighthold - Living Infernal Core",
                 "The Nighthold - Fiendish Hellfire Core",
                 "Tomb of Sargeras - Abyss Worm",
                 "Antorus, the Burning Throne - Antoran Charhound",
                 "Antorus, the Burning Throne - Shackled Ur'zul"]

legion_frame = InterfaceHelper.generate_widgets(mount_frame,
                                                 "Legion",
                                                 legion_mounts,
                                                 complement_value)

legion_button = Button(button_frame,
                       text = "Legion",
                       command = lambda: legion_frame.tkraise())
legion_button.grid(row = 6, column = 0, padx = 10, pady = 10, sticky = W)

# Battle for Azeroth ---------------------------------------------------------------------------------------------------
azeroth_mounts = ["Battle of Dazar'alor - G.M.O.D.",
                  "Battle of Dazar'alor - Glacial Tidestorm"]

azeroth_frame = InterfaceHelper.generate_widgets(mount_frame,
                                                 "Battle for Azeroth",
                                                 azeroth_mounts,
                                                 complement_value)

azeroth_button = Button(button_frame,
                        text = "Battle for Azeroth",
                        command = lambda: azeroth_frame.tkraise())
azeroth_button.grid(row = 7, column = 0, padx = 10, pady = 10, sticky = W)

# Default Frame --------------------------------------------------------------------------------------------------------
default_frame = LabelFrame(mount_frame, text = "Introduction", font = ("Arial Narrow", 18), padx = 5, pady = 5)
default_frame.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = N + S + E + W)

introduction_text = "Hello, welcome to my App! \n " \
                    "Press one of the buttons on the left to choose an expansion, \n" \
                    "and from there you can input in the number of attempts for each mount and press \n" \
                    "the calculate button to see how lucky (or unlucky) you would have to be for said mount" \
                    "to drop after said many attempts. \n" \
                    "You can toggle the complement button to switch between chance of " \
                    "getting and not getting the mount \n" \
                    "The app saves the number of attempts when you press the calculate button, " \
                    "so you can keep track of your progress \n" \
                    "If you have any feed back or suggestion, I'm always open to them! :)"

introduction_label = Label(default_frame, text = introduction_text, font=("Arial Narrow", 12))
introduction_label.grid(row = 0, column = 0, sticky = E)

root.mainloop()
