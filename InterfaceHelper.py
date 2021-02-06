from tkinter import *
import Core
import ReadWriter


# Opens a new window with the given given and display the label as text
# Takes the title of the window (string), and the text to be displayed (string)
# Returns null
# Note: The current implementation is quite basic, with no way to open the window in a different size or move text
def open_new_window(window_title, window_label):
    # Toplevel object which will be treated as a new window
    new_window = Toplevel()

    # sets the title of the Toplevel widget
    new_window.title(window_title)

    # A Label widget to show in Toplevel
    Label(new_window, text = window_label, font=("Arial Narrow", 12)).grid(row = 0, column = 0)
    new_window.grid_rowconfigure(0, weight = 1)
    new_window.grid_columnconfigure(0, weight = 1)


# Writes the current number of attempts for a particular mount into a save file
# Takes a mount name (string) and number of tries (int)
# Returns null
def save_attempts(mount, tries):
    # The user can input non valid inputs such as punctuation or letters into the spinbox, so we must check here first
    if not tries.isdigit():
        open_new_window("Save", "Invalid input, number of attempts must be an integer")
        return

    line_number = ReadWriter.find_line_num("Assets\\Attempts.txt", mount, 1)
    ReadWriter.write_line("Assets\\Attempts.txt", line_number, str(tries))


# Loads the previous number of attempts for a particular mount from a save file
# Takes a mount name (string) and number of tries (int)
# Returns the number of attempts in the save file (string)
def load_attempts(mount):
    line_number = ReadWriter.find_line_num("Assets\\Attempts.txt", mount, 1)
    return ReadWriter.read_line("Assets\\Attempts.txt", line_number)


# Essentially just calls two other functions at once, one to open new text window, other to save data to txt file
# Takes the title of the window (string), the name of the mount (string), the number of attempts tried (str),
# complement (boolean), and save (boolean)
# Returns null
# The variable complement is controlled by a tkinter checkbox, and changes what value is printed depending on its value
def open_and_save(window_title, mount, tries, complement, save):
    # The user can input non valid inputs such as punctuation or letters into the spinbox, so we must check here first
    if not tries.isdigit():
        open_new_window(window_title, "Invalid input, number of attempts must be an integer")
        return

    if save:
        save_attempts(mount, tries)

    # Convert to int here, as the open message functions takes int
    tries = int(tries)
    if complement:
        open_new_window(window_title, Core.probability_message_complement(mount, tries))
    else:
        open_new_window(window_title, Core.probability_message(mount, tries))


# Insert all the necessary widgets for all mounts in a list to an already existing frame
# Takes the parent window the frame will be part of (TK()),
# the row (int) and column (int) the new frame will be located on the parent window,
# the name of the frame we're creating (string),
# and a list of all the mounts to go into the frame (list of string),
# the complement_checkbox (tkinter.CheckButton())
# Returns (tkinter.LabelFrame)
def generate_widgets(master, row, column, frame_name, mount_list, complement_checkbox, save_checkbox):
    new_frame = LabelFrame(master, text = frame_name, font = ("Arial Narrow", 18), padx = 5, pady = 5)
    new_frame.grid(row = row, column = column, padx = 10, pady = 10, sticky = N + S + E + W)

    # We have row weight be equal to the number of mounts per frame
    master.rowconfigure(row, weight = len(mount_list))
    master.columnconfigure(column, weight = 1)

    label_widgets = {}
    new_frame.image = {}
    icon_label = {}
    attempts_string = {}
    spin_widgets = {}
    save_button_widgets = {}
    calculate_button_widgets = {}
    for i in range(len(mount_list)):

        full_name = mount_list[i]
        mount_name = full_name.split(' - ')[1]

        label_widgets[i] = Label(new_frame, text = mount_list[i], font = ("Arial Narrow", 12))
        label_widgets[i].grid(row = i, column = 0, sticky = W)

        new_frame.image[i] = PhotoImage(file = "Assets\\Icons\\" + mount_name + ".png")
        icon_label[i] = Label(new_frame, image = new_frame.image[i])
        icon_label[i].grid(row = i, column = 1, sticky = E)

        attempts_string[i] = StringVar()
        attempts_string[i].set(load_attempts(mount_name))

        spin_widgets[i] = Spinbox(new_frame, from_ = 0, to = 1024, width = 5, textvariable = attempts_string[i])
        spin_widgets[i].grid(row = i, column = 2, sticky = E)

        save_button_widgets[i] = Button(new_frame,
                                        text = "Save",
                                        font = ("Arial Narrow", 11),
                                        # j = i saves the current value of i into j when lambda is defined,
                                        # if we don't have this line, the command will always use the value of i when
                                        # the command is called, which will be the last row (i-th)
                                        command = lambda j = i: save_attempts(mount_list[j].split(' - ')[1],
                                                                              spin_widgets[j].get()))
        save_button_widgets[i].grid(row = i, column = 3, sticky = E)

        calculate_button_widgets[i] = Button(new_frame,
                                             text = "Calculate",
                                             font = ("Arial Narrow", 11),
                                             # j = i saves the current value of i into j when lambda is defined,
                                             # if we don't have this line, the command will always use the value of i
                                             # when the command is called, which will be the last row (i-th)
                                             command = lambda j = i: open_and_save(mount_list[j],
                                                                                   mount_list[j].split(' - ')[1],
                                                                                   spin_widgets[j].get(),
                                                                                   complement_checkbox.get(),
                                                                                   save_checkbox.get()))
        calculate_button_widgets[i].grid(row = i, column = 4, sticky = E)

        new_frame.rowconfigure(i, weight = 1)

    # Column 0 is label, column 1 is spinbox, column 2 is button
    new_frame.columnconfigure(0, weight = 1)
    new_frame.columnconfigure(1, weight = 1)
    new_frame.columnconfigure(2, weight = 1)
    new_frame.columnconfigure(3, weight = 1)
    new_frame.columnconfigure(4, weight = 1)
