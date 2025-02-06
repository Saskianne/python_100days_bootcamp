git: clone: https://github.com/YourUsername/YourRepository.git

import os
cwd = os.getcwd()
print(cwd)
os.chdir(C:\Users\swlee\python_100days_bootcamp)

from quiz_brain import QuizBrain

from question_model import Question
from data import question_data

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)


print(question_bank)
