#! Python3 
# Mad Libs
# madLibs.py
"""
Create a Mad Libs program that reads in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file. For example, a text file may look like this:
    The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.

The program would find these occurrences and prompt the user to replace them.
    Enter an adjective:
    silly
    Enter a noun:
    chandelier
    Enter a verb:
    screamed
    Enter a noun:
    pickup truck

The following text file would then be created:
    The silly panda walked to the chandelier and then screamed. A nearby pickup truck was unaffected by these events.

The results should be printed to the screen and saved to a new text file.
"""

# Create and write a new text file with word word ADJECTIVE, NOUN, ADVERB, or VERB
text = "The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events."
textFile = open("./c9_ReadingAndWritingFiles/PracticeP/madLibsText", 'w')
textFile.write(text)
textFile.close()

# Read text file 
textFile = open("./c9_ReadingAndWritingFiles/PracticeP/madLibsText", 'r')
startText = textFile.read()
textFile.close()
wordList = startText.split(' ')
# print(wordList)

# Replace the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.
replaceWordList = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']
for word in wordList:
    for replaceWord in replaceWordList:
        if replaceWord in word:
            print(f"Enter an {replaceWord.lower()}:")
            newWord = input()
            wordList[wordList.index(word)] = word.replace(replaceWord, newWord)
            break

finishedText = ' '.join(wordList)

# Results should be printed to the screen and saved to a new text file.
print('\n', finishedText, '\n')
textFile = open("./c9_ReadingAndWritingFiles/PracticeP/madLibsText", 'a')
textFile.write('\n'*2)
textFile.write("After replaced the words of 'ADJECTIVE', 'NOUN', 'ADVERB', 'VERB' text is below: \n\n")
textFile.write(finishedText)
textFile.close()
