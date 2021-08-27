#! Python3 
# Extending the Multi-Clipboard
# mcb_P.py
"""
Extend the multi-clipboard program in this chapter so that it has a delete <keyword> command line argument that will delete a keyword from the shelf. Then add a delete command line argument that will delete all keywords.
"""

import shelve, pyperclip, sys
mcbShelf = shelve.open('mcb_P')

# TODO: Save clipboard content.
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    if sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # TODO: List keywords and load content.
    if sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
        pyperclip.copy(str(list(mcbShelf.keys())))         
    elif sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys()))) 
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()