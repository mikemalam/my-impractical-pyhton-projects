"""Load text file and transforme it as a list.

Arguments:
- File name.

Exceptions:
- IOError if filename not found

Returns:
-A list of all words in a text file in lower case.

Require-import sys
"""
import sys

def load(file_name):
    """Only function."""
    try:
        with open(file_name) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt] #list comprehension
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}".format(e, file_name), file=sys.stderr)
        sys.exit(1)

