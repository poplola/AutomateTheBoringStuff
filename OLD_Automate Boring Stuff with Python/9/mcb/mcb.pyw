#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# TODO: Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()

# delete contents
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]

    # pyperclip.copy(str(list(mcbShelf.keys())))

elif len(sys.argv) == 2 and sys.argv[1].lower() == 'delete':
    mcbShelf.clear

elif len(sys.argv) == 2 and sys.argv[1].lower() == 'list':
    # TODO: List keywords and load content.
    pyperclip.copy(str(list(mcbShelf.keys())))
    if sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()