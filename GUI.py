import tkinter
import Core
import ReadWriter

window = tkinter.Tk()
window.title("WOW Statistical Probabily Tracker")


# Opens a new window with the given given and display the label as text
# Takes the title of the window (string), and the text to be displayed (string)
# Returns null
# Note: The current implementation is quite basic, with no way to open the window in a different size or move text
def open_new_window(window_title, window_label):
    # Toplevel object which will
    # be treated as a new window
    new_window = tkinter.Toplevel(window)

    # sets the title of the
    # Toplevel widget
    new_window.title(window_title)

    # sets the geometry of the Toplevel
    new_window.geometry("200x100")

    # A Label widget to show in toplevel
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
# Takes the title of the window (string), the name of the mount (string), and the number of attempts tried (int)
# Returns null
def open_and_save(window_title, mount, tries):
    open_new_window(window_title, Core.probability_message(mount, tries))
    save_attempts(mount, tries)


# Below is the code that is generating the current tkinter window
var = tkinter.StringVar(window)
var.set(load_attempts("Invincible"))
spin = tkinter.Spinbox(window, from_=0, to=100, width = 10, textvariable=var)
spin.grid(column = 1, row = 0)

# spinbox.get() always return a string
tkinter.Button(window,
               text = "Click Me!",
               command = lambda: open_and_save("Invincible", "Invincible", int(spin.get()))
               ).grid(column = 2, row = 2)
window.geometry('250x250')
window.mainloop()
