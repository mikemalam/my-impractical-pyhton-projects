"""Load text file and transforme it as a list.

    -iput
    File name

    -output
    list
"""

def load(file_name):
    """Only function."""
    try:
        dictionnary_file = open(file_name, "r")
        return list(dictionnary_file)
    except IOError as e:
        print("An Input/Ouptu error occured : {}".format(e)")

