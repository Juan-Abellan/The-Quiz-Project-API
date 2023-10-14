from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(_q_text=question_text, _q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(_q_list=question_bank)
quiz_ui = QuizInterface(_quiz_brain=quiz)

