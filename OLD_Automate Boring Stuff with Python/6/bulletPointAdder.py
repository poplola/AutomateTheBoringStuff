
#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.
print('\n=====================================================================\n')
import pyperclip

text = pyperclip.paste()

print('\npaste text to clipboard: \n', text)

# Seperate lines and add stars *
lines = text.split('\n')

# print(lines)

for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
    text = '\n'.join(lines)


print('\ncopy * text from clipboard: \n', text)

pyperclip.copy(text)

print('\n=====================================================================\n')