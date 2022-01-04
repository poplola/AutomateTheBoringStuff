#! Python 3
# randomQuizGenerator.py
# PROJECT: GENERATING RANDOM QUIZ FILES
"""
Say you’re a geography teacher with 35 students in your class and you want to give a pop quiz on US state capitals. Alas, your class has a few bad eggs in it, and you can’t trust the students not to cheat. You’d like to randomize the order of questions so that each quiz is unique, making it impossible for anyone to crib answers from anyone else. Of course, doing this by hand would be a lengthy and boring affair. Fortunately, you know some Python.

Here is what the program does:
    1. Creates 35 different quizzes
    2. Creates 50 multiple-choice questions for each quiz, in random order
    3. Provides the correct answer and three random wrong answers for each question, in random order
    4. Writes the quizzes to 35 text files
    5. Writes the answer keys to 35 text files

This means the code will need to do the following:
    1. Store the states and their capitals in a dictionary
    2. Call open(), write(), and close() for the quiz and answer key text files
    3. Use random.shuffle() to randomize the order of the questions and multiple-choice options
"""

import random, os
from pathlib import Path

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
'New Mexico': 'Santa Fe', 'New York': 'Albany',
'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

numOfQuizFile = 35
numOfQuizzes = 50
quizPath = str(Path.cwd()/'c9_ReadingAndWritingFiles/quizFile')

if not Path(quizPath).exists():
    os.mkdir(Path.cwd()/'c9_ReadingAndWritingFiles/quizFile')

for i in range(numOfQuizFile):
    StateList = list(capitals.keys())

    # print(len(StateList))

    quizFile = open(f'{quizPath}/Quiz_{i+1}.txt', 'w')

    quizFile.write('='*100+'\n')
    quizFile.write(('\t'+f'< Quiz Paper No.{i+1} >' + ' '*10+'Name:'+' '*30+'Date:'+' '*20).ljust(100)+'\n')
    quizFile.write('='*100+'\n'*2)

    answerFile = open(f'{quizPath}/Quiz_Answer_{i+1}.txt', 'w')    
    answerFile.write('='*100+'\n')
    answerFile.write((f'< Quiz Answer Paper No.{i+1} >').center(100)+'\n')
    answerFile.write('='*100+'\n'*2)
   
    for j in range(numOfQuizzes):
        randomState = random.choice(StateList)
        quizFile.write(f'Q{j+1} : What is the capital of {randomState} state?\n')
        StateList.remove(f'{randomState}')
        otherStateList = list(capitals.keys())
        otherStateList.remove(f'{randomState}')
        
        optList = []        
        optList.append(capitals[randomState])
        # print('\n', j, optList)
        wrongAnswer = ''
        while True:
            if len(optList) == 4:
                break
            wrongAnswer = random.choice(otherStateList)
            if wrongAnswer in optList:
                continue
            else:
                optList.append(capitals[wrongAnswer])
                otherStateList.remove(wrongAnswer)
            # print(optList)
            # print(wrongAnswer)
            # print(StateList)
        # print(optList)

        random.shuffle(optList)
        # print(optList)

        optSign = ['A', 'B', 'C', 'D']
        for n in range(4):
            quizFile.write(f'\t{optSign[n]}. {optList[n]}\n')
            if optList[n] == capitals[randomState]:
                answerFile.write(f'Q{j+1} : What is the capital of {randomState} state?\n')
                answerFile.write(f'\tAnswer ==> {optSign[n]}. {capitals[randomState]}\n\n')
        quizFile.write('\n')

    quizFile.close()
    answerFile.close()