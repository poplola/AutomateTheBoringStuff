#! python3
# displayMessageBox.py - DISPLAYING MESSAGE BOXES
"""
PyAutoGUI programs will use your entire desktop as its playground. The text-based window that your program runs in, whether it’s Mu or a Terminal window, will probably be lost as your PyAutoGUI program clicks and interacts with other windows. This can make getting input and output from the user hard if the Mu or Terminal windows get hidden under other windows.
To solve this, PyAutoGUI offers pop-up message boxes to provide notifications to the user and receive input from them. There are four message box functions:
    < pyautogui.alert(text) >
        Displays text and has a single OK button.
    < pyautogui.confirm(text) > 
        Displays text and has OK and Cancel buttons, returning either 'OK' or 'Cancel' depending on the button clicked.
    < pyautogui.prompt(text) >
        Displays text and has a text field for the user to type in, which it returns as a string.
    < pyautogui.password(text) >
        Is the same as prompt(), but displays asterisks so the user can enter sensitive information such as a password.

These functions also have an optional second parameter that accepts a string value to use as the title in the title bar of the message box. The functions won’t return until the user has clicked a button on them, so they can also be used to introduce pauses into your PyAutoGUI programs. 
"""
import pyautogui
pyautogui.alert('This is a message.', 'Important')
pyautogui.confirm('Do you want to continue?') # Click Cancel 
name = pyautogui.prompt("What is your cat's name?")
psd = pyautogui.password('What is the password?') 
print(f"{name}\npassword: {psd}")
