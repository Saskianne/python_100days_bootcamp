import os
os.chdir(C:\Users\swlee\python_100days_bootcamp)
cwd = os.getcwd()
print(cwd)   

from main import question_bank
from question_model import Question


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self, question_number):
        next_question = self.question_list[question_number]
        question_number += 1
        input(f"Q.{self.question_number}: {next_question.text}(True/False)?")



