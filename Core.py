import ReadWriter

complement = True


# Returns a message that states the statistical probability of (not) getting the amount after the inputted attempts
# Takes name of a mount (string), and the current number of attempts (int)
# Returns a message (string)
# Does not need to print, as it is simply being displayed in a messages box in tkinter
def calculate(mount, tries):
    return "The chance of getting " + mount + " within " + str(tries) + " tries is " + str(probability(mount, tries))


# Returns the drop rate of a mount dropping by parsing through the txt file that stores this info
# Takes names of a mount (string)
# Returns the drop rate of said mount (string)
# As the drop rates are all decimal, cannot be converted to int, must be converted to float
def get_probability(mount):
    line_num = ReadWriter.findLineNum("Drop Rates.txt", mount, 1)
    return ReadWriter.readLine("Drop Rates.txt", line_num)


# Returns the statistical probability of (not) getting the amount after the inputted attempts
# Takes name of a mount (string), and the current number of attempts (int)
# Returns the probability (float)
# Has different behavior if the global variable, complement, is true or not
# If complement is true, returns the probability of not getting the mount
# If complement is false, returns the probability of getting the mount
def probability(mount, tries):
    prob = float(get_probability(mount))
    if complement:
        z = 1 - ((1 - prob) ** tries)
        return z
    else:
        z = (1 - prob) ** tries
        return z
