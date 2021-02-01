from tkinter import *
import Core
import ReadWriter


# Opens a new window with the given given and display the label as text
# Takes the title of the window (string), and the text to be displayed (string)
# Returns null
# Note: The current implementation is quite basic, with no way to open the window in a different size or move text
def open_new_window(window_title, window_label):
    # Toplevel object which will
    # be treated as a new window
    new_window = Toplevel()

    # sets the title of the
    # Toplevel widget
    new_window.title(window_title)

    # A Label widget to show in Toplevel
    Label(new_window, text = window_label).pack()


# Writes the current number of attempts for a particular mount into a save file
# Takes a mount name (string) and number of tries (int)
# Returns null
def save_attempts(mount, tries):
    line_number = ReadWriter.find_line_num("Attempts.txt", mount, 1)
    ReadWriter.write_line("Attempts.txt", line_number, str(tries))


# Loads the previous number of attempts for a particular mount from a save file
# Takes a mount name (string) and number of tries (int)
# Returns the number of attempts in the save file (string)
def load_attempts(mount):
    line_number = ReadWriter.find_line_num("Attempts.txt", mount, 1)
    return ReadWriter.read_line("Attempts.txt", line_number)


# Essentially just calls two other functions at once, one to open new text window, other to save data to txt file
# Takes the title of the window (string), the name of the mount (string), the number of attempts tried (int),
# and complement (boolean)
# Returns null
# The variable complement is controlled by a tkinter checkbox, and changes what value is printed depending on its value
def open_and_save(window_title, mount, tries, complement):
    if complement:
        open_new_window(window_title, Core.probability_message_complement(mount, tries))
    else:
        open_new_window(window_title, Core.probability_message(mount, tries))
    save_attempts(mount, tries)


# Generates a frame that also contains all the necessary widgets for all mounts in a list
# Takes the parent window the frame will be part of (TK()),
# the row (int) and column (int) the new frame will be located on the parent window,
# the name of the frame we're creating (string),
# and a list of all the mounts to go into the frame (list of string),
# the complement_checkbox (tkinter.CheckButton())
# Returns (tkinter.LabelFrame)
def generate_widgets(master, frame_name, mount_list, complement_checkbox):
    new_frame = LabelFrame(master, text = frame_name, font=("Arial Narrow", 18), padx = 5, pady = 5)
    new_frame.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = N + S + E + W)

    # We have row weight be equal to the number of mounts per frame
    master.rowconfigure(0, weight = len(mount_list))
    master.columnconfigure(0, weight = 1)

    label_widgets = {}
    attempts_string = {}
    spin_widgets = {}
    button_widgets = {}
    for i in range(len(mount_list)):

        full_name = mount_list[i]
        mount_name = full_name.split(' - ')[1]

        label_widgets[i] = Label(new_frame, text = mount_list[i], font = ("Arial Narrow", 12))
        label_widgets[i].grid(row = i, column = 0, sticky = W)

        attempts_string[i] = StringVar()
        attempts_string[i].set(load_attempts(mount_name))

        spin_widgets[i] = Spinbox(new_frame, from_ = 0, to = 255, width = 5, textvariable = attempts_string[i])
        spin_widgets[i].grid(row = i, column = 1, sticky = E)

        button_widgets[i] = Button(new_frame,
                                   text = "Calculate",
                                   # j = i saves the current value of i into j when lambda is defined,
                                   # if we don't have this line, the command will always use the value of i when the
                                   # command is called, which will be the last row (i-th)
                                   command = lambda j = i: open_and_save(mount_list[j],
                                                                         mount_list[j].split(' - ')[1],
                                                                         int(spin_widgets[j].get()),
                                                                         complement_checkbox.get()))
        button_widgets[i].grid(row = i, column = 2, sticky = E)

        new_frame.rowconfigure(i, weight = 1)

    # Column 0 is label, column 1 is spinbox, column 2 is button
    new_frame.columnconfigure(0, weight = 1)
    new_frame.columnconfigure(1, weight = 1)
    new_frame.columnconfigure(2, weight = 1)

    return new_frame
