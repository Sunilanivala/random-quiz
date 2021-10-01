import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix','Arkansas': 'Little Rock', 'California': 'Sacramento'
, 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta'
, 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines'
, 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis'
, 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City'
, 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton'
, 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus'
, 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence'
, 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City'
, 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison'
, 'Wyoming': 'Cheyenne'}

# 35 question papers - 35 answer papers
# Each question paper should have 50 questions.
# Each question should have 4 options with 1 correct answer.

for file_no in range(35):
    with open('/home/channelbridge//Quiz_questionpaper/Question_Paper_' + str(file_no + 1) + '.txt', 'w') as questionPaper:
        with open('/home/channelbridge/Quiz_questionpaper/Answer_File_' + str(file_no + 1) + '.txt', 'w') as answerPaper:
            questionPaper.write('\nName: \nClass: \nDate: \n\n')
            questionPaper.write(' '*20 + 'Random Quiz Generator - Question Paper ' + str(file_no + 1) + '\n')

            for questionNum in range(50):
                states = list(capitals.keys())
                random.shuffle(states)   # state name = states[questionNum]
                correctAnswer = capitals[states[questionNum]] # My 4 options = correct ans + 3 wrong ans
                wrongAnswer = list(capitals.values())
                wrongAnswer.remove(correctAnswer)
                wrongOptions = random.sample(wrongAnswer, 3) # wrongOptions = 3 wrong ans
                options = wrongOptions + [correctAnswer]
                random.shuffle(options)

                questionPaper.write('\n#' + str(questionNum+1) + ' What is the capital of ' + states[questionNum] + '?\n')
                for optionNum in range(4):
                    questionPaper.write(' '*4 + 'ABCD'[optionNum]  + '. ' + options[optionNum] + '\n')

                answerPaper.write(str(questionNum+1) + '. ' + 'ABCD'[options.index(correctAnswer)] + '\n')
