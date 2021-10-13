#! python3
# formFiller.py - Automatically fills in the form.

import pyautogui, time

formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
            'robocop': 4, 'comments': 'Tell Bob I said hi.'},
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,
            'comments': 'n/a'},
            {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball',
            'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
            {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
            'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
           ]

pyautogui.PAUSE = 0.5
print('Ensure that the browser window is active and the form is loaded!')

for person in formData:
    # Give the user a chance to kill the script.
    print('>>> 5-SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
    time.sleep(5)

    print('Entering %s info...' % (person['name']))
    # pyautogui.write(['\t', '\t'])
    pyautogui.write('\t')

    # Fill out the Name field.
    pyautogui.write(person['name'] + '\t')

    # Fill out the Greatest Fear(s) field.
    pyautogui.write(person['fear'] + '\t')

    # Fill out the Source of Wizard Powers field.
    if person['source'] == 'wand':
        pyautogui.write(['down', ' ', '\t'] , 0.5)
    elif person['source'] == 'amulet':
        pyautogui.write(['down', 'down', ' ', '\t'] , 0.5)
    elif person['source'] == 'crystal ball':
        pyautogui.write(['down', 'down', 'down', ' ', '\t'] , 0.5)
    elif person['source'] == 'money':
        pyautogui.write(['down', 'down', 'down', 'down', ' ', '\t'] , 0.5)
    # pyautogui.click()

    # Fill out the RoboCop field.
    if person['robocop'] == 1:
        pyautogui.write([' ', '\t', '\t'] , 0.5)
    elif person['robocop'] == 2:
        pyautogui.write(['right', '\t', '\t'] , 0.5)
    elif person['robocop'] == 3:
        pyautogui.write(['right', 'right', '\t', '\t'] , 0.5)
    elif person['robocop'] == 4:
        pyautogui.write(['right', 'right', 'right', '\t', '\t'] , 0.5)
    elif person['robocop'] == 5:
        pyautogui.write(['right', 'right', 'right', 'right', '\t', '\t' ] , 0.5)

    # Fill out the Additional Comments field.
    pyautogui.write(person['comments'] + '\t')

    # "Click" Submit button by pressing Enter.
    time.sleep(0.5)             # Wait for the button to activate.
    pyautogui.press('enter')

    # Wait until form page has loaded.
    print('Submitted form.')
    time.sleep(5)
    # pyautogui.click(155,268)
    pyautogui.write(['\t','\t','enter'], 0.5)

    # Click the Submit another response link.
    # pyautogui.click(submitAnotherLink[0], submitAnotherLink[1])
    # print(pyautogui.mouseInfo())
    # pyautogui.click('SubmitAnotherResponse.png')
    # fw = pyautogui.getActiveWindow()
    # print(fw.title)


    # TODO: Wait until the form page has loaded.

    ## TODO: Fill out the Name Field.

    ## TODO: Fill out the Greatest Fear(s) field.

    ## TODO: Fill out the Source of Wizard  Powers field.

    ## TODO: Fill out the RoboCop field.

    ## TODO: Fill out the Additional Comments field.

    ## TODO: Click Submit.

    ## TODO: Wait until form page has loaded.

    ## TODO: Click the Submit another response link.