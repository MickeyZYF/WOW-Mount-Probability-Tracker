import ReadWriter

# Note: Currently the probability is displayed as a decimal number rather than a percentage, also if the number of
#       attempts is sufficiently high, then it would calculate as 1.00, or 100%. This is most likely due to how float
#       works, should probably change it sometimes, have it be percentage with two decimal spaces and rounded down


# Returns a message that states the statistical probability of getting the amount after the inputted attempts
# Takes name of a mount (string), and the current number of attempts (int)
# Returns a message (string)
# Does not need to print, as it is simply being displayed in a messages box in tkinter
def probability_message(mount, tries):
    return "The chance of getting " + mount + " within " + str(tries) + " tries is " \
            + str(probability(mount, tries))


# Returns a message that states the statistical probability of NOT getting the amount after the inputted attempts
# Takes name of a mount (string), and the current number of attempts (int)
# Returns a message (string)
# Does not need to print, as it is simply being displayed in a messages box in tkinter
def probability_message_complement(mount, tries):
    return "The chance of getting not " + mount + " within " + str(tries) + " tries is " \
            + str(probability_complement(mount, tries))


# Returns the drop rate of a mount dropping by parsing through the txt file that stores this info
# Takes names of a mount (string)
# Returns the drop rate of said mount (string)
# As the drop rates are all decimal, cannot be converted to int, must be converted to float
def get_probability(mount):
    line_num = ReadWriter.find_line_num("Drop Rates.txt", mount, 1)
    return ReadWriter.read_line("Drop Rates.txt", line_num)


# Returns the statistical probability of getting the amount after the inputted attempts
# Takes name of a mount (string), and the current number of attempts (int)
# Returns the probability (float)
# Has different behavior if the global variable, complement, is true or not
# If complement is true, returns the probability of not getting the mount
# If complement is false, returns the probability of getting the mount
def probability(mount, tries):
    prob = float(get_probability(mount))
    z = 1 - ((1 - prob) ** tries)
    return z


# Returns the statistical probability of NOT getting the amount after the inputted attempts
# Takes name of a mount (string), and the current number of attempts (int)
# Returns the probability (float)
# Has different behavior if the global variable, complement, is true or not
# If complement is true, returns the probability of not getting the mount
# If complement is false, returns the probability of getting the mount
def probability_complement(mount, tries):
    prob = float(get_probability(mount))
    z = 1 - ((1 - prob) ** tries)
    z = (1 - prob) ** tries
    return z
