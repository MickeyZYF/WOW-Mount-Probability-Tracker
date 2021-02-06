# Returns the line number that contains the search term
# Takes file name (string), the term we're searching for (string), and an offset (int)
# Returns a line number or string that tells us searched term doesn't appear on the file (int or string)
# The offset is how much we want to add to the line number the function is returning,
# as sometimes we want the line after the searched term
def find_line_num(file_name, search_term, offset):
    line_number = "Term not found"
    with open(file_name, 'r') as saveFile:
        for number, line in enumerate(saveFile):
            if search_term in line:
                line_number = number
                break
    saveFile.close()
    if line_number == "Term not found":
        return line_number
    else:
        return line_number + offset


# Returns the text on a specific line of a file
# Takes file name (string) and line number to read (int)
# Returns text on the specific line (string)
def read_line(file_name, line_num):
    line_text = ""
    with open(file_name, 'r') as save_file:
        lines = save_file.readlines()
        line_text = lines[line_num]
    save_file.close()
    return line_text


# Replaces the text on a specific line of a file with specified text
# We use the below function to update the # of times the user has attempted a particular roll
# Takes file name (string), line number to be overwritten (int), and new # of attempts (string)
# Returns null
def write_line(file_name, line_num, write):
    with open(file_name, 'r') as save_file:
        lines = save_file.readlines()
        lines[line_num] = write + "\n"
        with open(file_name, 'w') as out:
            out.writelines(lines)
            out.close()
    save_file.close()
