#! python3
# bulletPointAdder.py - Adds bullet points to the start
# of each line of whatever text I copied into the clipboard

import pyperclip
text = pyperclip.paste()
newtext = "" # initialize empty string

for line in text.split('\n'):
    newtext += "* " + line + "\n"

pyperclip.copy(newtext)