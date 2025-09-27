from question_model import Question
from data_otdb import question_data
from quiz_brain import QuizBrain

# Open Trivia Database
# https://opentdb.com/api_config.php
# JSON to Python Dict
# https://json-to.com/json-python

question_bank = []
for question in question_data:
    new_question = Question(question["question"], question["correct_answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}".format())


#print(question_bank[0].text)
#for question in question_bank:
#    print(question.text)
