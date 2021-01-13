import tkinter
import Core
import ReadWriter

# NOTE: Probably move some of the functions here into a file, as most of the stuff here are actually
#       just helper functions. So separating the helpers and the actual tkinter stuff would makes things cleaner


# Opens a new window with the given given and display the label as text
# Takes the title of the window (string), and the text to be displayed (string)
# Returns null
# Note: The current implementation is quite basic, with no way to open the window in a different size or move text
def open_new_window(window_title, window_label):
    # Toplevel object which will
    # be treated as a new window
    new_window = tkinter.Toplevel(master)

    # sets the title of the
    # Toplevel widget
    new_window.title(window_title)

    # sets the geometry of the Toplevel
    new_window.geometry("200x100")

    # A Label widget to show in Toplevel
    tkinter.Label(new_window, text = window_label).pack()


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
#                                         and complement (boolean)
# Returns null
# The variable complement is controlled by a tkinter checkbox, and changes what value is printed depending on its value
def open_and_save(window_title, mount, tries, complement):
    if complement:
        open_new_window(window_title, Core.probability_message_complement(mount, tries))
    else:
        open_new_window(window_title, Core.probability_message(mount, tries))
    save_attempts(mount, tries)


master = tkinter.Tk()
master.title("WOW Statistical Probabily Tracker")


# Code for the complement checkbox
complement_checkbox = tkinter.BooleanVar()
tkinter.Checkbutton(master, text = "Complement", variable = complement_checkbox).grid(column = 4, row = 1)


# Below is the code that is generating the current tkinter window
var = tkinter.StringVar()
var.set(load_attempts("Invincible"))
spin = tkinter.Spinbox(master, from_ = 0, to = 100, width = 10, textvariable = var)
spin.grid(column = 1, row = 0)

# spinbox.get() always return a string
tkinter.Button(master,
               text = "Click Me!",
               command = lambda: open_and_save("Invincible", "Invincible", int(spin.get()), complement_checkbox.get())
               ).grid(column = 2, row = 2)
master.geometry('250x250')
master.mainloop()
