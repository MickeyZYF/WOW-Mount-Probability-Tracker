from tkinter import *
import InterfaceHelper

# NOTE: Needs to gives some stuff here weight

root = Tk()
root.rowconfigure(0, weight = 1)
root.columnconfigure(0, weight = 1)
root.title("WOW Attempts Tracker")


# Complement Checkbox
complement_value = BooleanVar()
complement_checkbox = Checkbutton(root,
                                  text ="Complement",
                                  font = ("Arial Narrow", 11), variable = complement_value)
complement_checkbox.grid(row = 0, column = 4, sticky = W)
# Weights
root.grid_rowconfigure(0, weight = 0)
root.grid_columnconfigure(4, weight = 1)

# Calculate Also Saves Checkbox
saves_value = BooleanVar()
saves_value_checkbox = Checkbutton(root, text ="Calculate Also Saves", font = ("Arial Narrow", 11), variable = saves_value)
saves_value_checkbox.grid(row = 1, column = 4, sticky = W)
# Weights
root.grid_rowconfigure(1, weight = 0)

button_frame = LabelFrame(root, highlightbackground = "black", highlightthickness = 1)
button_frame.grid(row = 2, column = 0, sticky = N + E + S + W)
# Weights
root.grid_rowconfigure(2, weight = 1)
root.grid_columnconfigure(0, weight = 1)
button_frame.columnconfigure(1, weight = 1)

mount_frame = Frame(root, highlightbackground = "black", highlightthickness = 1)
mount_frame.grid(row = 2, column = 1, sticky = N + E + S + W)
# Weights
root.columnconfigure(1, weight = 1)
mount_frame.rowconfigure(0, weight = 1)
mount_frame.columnconfigure(0, weight = 1)


# Burning Crusade ------------------------------------------------------------------------------------------------------
burning_crusade_raids = ["Karazhan - Fiery Warhorse",
                         "The Eye - Ashes of Al'ar"]

burning_crusade_frame = Frame(mount_frame)
burning_crusade_frame.grid(row = 0, column = 0, sticky = N + S + E + W)

InterfaceHelper.generate_widgets(burning_crusade_frame,
                                 0,
                                 0,
                                 "Raids",
                                 burning_crusade_raids,
                                 complement_value, saves_value)

burning_crusade_button = Button(button_frame,
                                text = "The Burning Crusade",
                                font = ("Arial Narrow", 12),
                                command = lambda: burning_crusade_frame.tkraise())
burning_crusade_button.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = W)
button_frame.rowconfigure(1, weight = 1)

bc_image = PhotoImage(file ="Assets\\Icons\\BC.png")
bc_icon = Label(button_frame, image = bc_image)
bc_icon.grid(row = 1, column = 1)

# Wrath of the Lich King -----------------------------------------------------------------------------------------------
lich_king_raids = ["Vault of Archavon - Grand Black War Mammoth",
                   "The Eye of Eternity - Azure Drake",
                   "The Eye of Eternity - Blue Drake",
                   "Onyxia's Lair - Onyxian Drake",
                   "Ulduar - Mimiron's Head",
                   "Icecrown Citadel - Invincible"]

lich_king_frame = Frame(mount_frame)
lich_king_frame.grid(row = 0, column = 0, sticky = N + S + E + W)

InterfaceHelper.generate_widgets(lich_king_frame,
                                 0,
                                 0,
                                 "Raids",
                                 lich_king_raids,
                                 complement_value,
                                 saves_value)

lich_king_button = Button(button_frame,
                          text = "Wrath of the Lich King",
                          font = ("Arial Narrow", 12),
                          command = lambda: lich_king_frame.tkraise())
lich_king_button.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = W)
button_frame.rowconfigure(2, weight = 1)

wrath_image = PhotoImage(file = "Assets\\Icons\\WOLK.png")
wrath_label = Label(button_frame, image = wrath_image)
wrath_label.grid(row = 2, column = 1)

# Cataclysm ------------------------------------------------------------------------------------------------------------
cataclysm_raids = ["Throne of the Four Winds - Drake of the South Wind",
                   "Firelands - Flametalon of Alysrazor",
                   "Firelands - Pureblood Fire Hawk",
                   "Dragon Soul - Experiment 12-B",
                   "Dragon Soul - Blazing Drake",
                   "Dragon Soul - Life-Binder's Handmaiden"]

cataclysm_frame = Frame(mount_frame)
cataclysm_frame.grid(row = 0, column = 0, sticky = N + S + E + W)

InterfaceHelper.generate_widgets(cataclysm_frame,
                                 0,
                                 0,
                                 "Raids",
                                 cataclysm_raids,
                                 complement_value,
                                 saves_value)

cataclysm_button = Button(button_frame,
                          text = "Cataclysm",
                          font = ("Arial Narrow", 12),
                          command = lambda: cataclysm_frame.tkraise())
cataclysm_button.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = W)
button_frame.rowconfigure(3, weight = 1)

cata_image = PhotoImage(file = "Assets\\Icons\\CATA.png")
cata_icon = Label(button_frame, image = cata_image)
cata_icon.grid(row = 3, column = 1)

# Mists of Pandaria ----------------------------------------------------------------------------------------------------
pandaria_world_bosses = ["Sha of Anger - Heavenly Onyx Cloud Serpent",
                         "Galleon - Son of Galleon",
                         "Nalak - Thundering Cobalt Cloud Serpent",
                         "Oondasta - Cobalt Primordial Direhorn"]

pandaria_raids = ["Mogu'shan Vault - Astral Cloud Serpent",
                  "Throne of Thunder - Spawn of Horridon",
                  "Throne of Thunder - Clutch of Ji-Kun",
                  "Siege of Orgrimmar - Kor'kron Juggernaut"]

pandaria_frame = Frame(mount_frame)
pandaria_frame.grid(row = 0, column = 0, sticky = N + S + E + W)

InterfaceHelper.generate_widgets(pandaria_frame,
                                 0,
                                 0,
                                 "World Bosses", pandaria_world_bosses,
                                 complement_value,
                                 saves_value)

InterfaceHelper.generate_widgets(pandaria_frame,
                                 1,
                                 0,
                                 "Raids",
                                 pandaria_raids,
                                 complement_value,
                                 saves_value)


pandaria_button = Button(button_frame,
                         text = "Mists of Pandaria",
                         font = ("Arial Narrow", 12),
                         command = lambda: pandaria_frame.tkraise())
pandaria_button.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = W)
button_frame.rowconfigure(4, weight = 1)

mists_image = PhotoImage(file = "Assets\\Icons\\MISTS.png")
mists_icon = Label(button_frame, image = mists_image)
mists_icon.grid(row = 4, column = 1)

# Warlords of Draenor --------------------------------------------------------------------------------------------------
draenor_world_bosses = ["Rukhmar - Solar Spirehawk"]

draenor_raids = ["Blackrock Foundry - Ironhoof Destroyer",
                 "Hellfire Citadel - Felsteel Annihilator"]


draenor_frame = Frame(mount_frame)
draenor_frame.grid(row = 0, column = 0, sticky = N + S + E + W)

InterfaceHelper.generate_widgets(draenor_frame,
                                 0,
                                 0,
                                 "World Bosses",
                                 draenor_world_bosses,
                                 complement_value,
                                 saves_value)

InterfaceHelper.generate_widgets(draenor_frame,
                                 1,
                                 0,
                                 "Raids",
                                 draenor_raids,
                                 complement_value,
                                 saves_value)


draenor_button = Button(button_frame,
                        text = "Warlords of Draenor",
                        font = ("Arial Narrow", 12),
                        command = lambda: draenor_frame.tkraise())
draenor_button.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = W)
button_frame.rowconfigure(5, weight = 1)

wod_image = PhotoImage(file = "Assets\\Icons\\WoD.png")
wod_icon = Label(button_frame, image = wod_image)
wod_icon.grid(row = 5, column = 1)

# Legion ---------------------------------------------------------------------------------------------------------------
legion_dungeons = ["Return to Karazhan - Midnight's Eternal Reins"]

legion_raids = ["The Nighthold - Living Infernal Core",
                "The Nighthold - Fiendish Hellfire Core",
                "Tomb of Sargeras - Abyss Worm",
                "Antorus, the Burning Throne - Antoran Charhound",
                "Antorus, the Burning Throne - Shackled Ur'zul"]

legion_frame = Frame(mount_frame)
legion_frame.grid(row = 0, column = 0, sticky = N + S + E + W)

InterfaceHelper.generate_widgets(legion_frame,
                                 0,
                                 0,
                                 "Dungeons",
                                 legion_dungeons,
                                 complement_value,
                                 saves_value)

InterfaceHelper.generate_widgets(legion_frame,
                                 1,
                                 0,
                                 "Raids",
                                 legion_raids,
                                 complement_value,
                                 saves_value)

legion_button = Button(button_frame,
                       text = "Legion",
                       font = ("Arial Narrow", 12),
                       command = lambda: legion_frame.tkraise())
legion_button.grid(row = 6, column = 0, padx = 10, pady = 10, sticky = W)
button_frame.rowconfigure(6, weight = 1)

legion_image = PhotoImage(file = "Assets\\Icons\\LEGION.png")
legion_icon = Label(button_frame, image = legion_image)
legion_icon.grid(row = 6, column = 1)

# Battle for Azeroth ---------------------------------------------------------------------------------------------------
azeroth_dungeons = ["Freehold - Sharkbait",
                    "The Underrot - Underrot Crawg",
                    "Kings' Rest - Tomb Stalker"]

azeroth_raids = ["Battle of Dazar'alor - G.M.O.D.",
                 "Battle of Dazar'alor - Glacial Tidestorm"]


azeroth_frame = Frame(mount_frame)
azeroth_frame.grid(row = 0, column = 0, sticky = N + S + E + W)

InterfaceHelper.generate_widgets(azeroth_frame,
                                 0,
                                 0,
                                 "Dungeons",
                                 azeroth_dungeons,
                                 complement_value,
                                 saves_value)

InterfaceHelper.generate_widgets(azeroth_frame,
                                 1,
                                 0,
                                 "Raids",
                                 azeroth_raids, 
                                 complement_value,
                                 saves_value)

azeroth_button = Button(button_frame,
                        text = "Battle for Azeroth",
                        font=("Arial Narrow", 12),
                        command = lambda: azeroth_frame.tkraise())
azeroth_button.grid(row = 7, column = 0, padx = 10, pady = 10, sticky = W)
button_frame.rowconfigure(7, weight = 1)

bfa_image = PhotoImage(file = "Assets\\Icons\\BFA.png")
bfa_icon = Label(button_frame, image = bfa_image)
bfa_icon.grid(row = 7, column = 1)

# Default Frame --------------------------------------------------------------------------------------------------------
default_frame = LabelFrame(mount_frame, text = "Introduction", font = ("Arial Narrow", 18), padx = 5, pady = 5)
default_frame.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = N + S + E + W)

introduction_text = "Hello, welcome to my App! " \
                    "\n" \
                    "\n" \
                    "Press one of the buttons on the left to choose an expansion, and from there you can input in " \
                    "the number of attempts" \
                    "\n" \
                    "for each mount and press the calculate button to see how lucky (or unlucky) you " \
                    "would have to be for said mount to" \
                    "\n" \
                    "drop after said many attempts." \
                    "\n" \
                    "\n" \
                    "You can toggle the complement button to switch between chance of getting and not getting " \
                    "the mount." \
                    "\n" \
                    "\n" \
                    "The app saves the number of attempts when you press the calculate button, so you can keep track " \
                    "of your progress " \
                    "\n" \
                    "\n" \
                    "Please do not mess with the stuff in the Assets folder unless you know what your doing" \
                    "\n" \
                    "\n" \
                    "If you have any feed back or suggestion, I'm always open to them! ╰(▔∀▔)╯" \
                    "\n" \
                    "\n" \
                    "https://github.com/MickeyZYF"

introduction_label = Label(default_frame, text = introduction_text, font=("Arial Narrow", 14), justify = LEFT)
introduction_label.grid(row = 0, column = 0, sticky = E)

root.mainloop()
