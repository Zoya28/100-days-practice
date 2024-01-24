from question_model import questions
from data import question_data
from quiz_brain import quiz_brain

question_bank = []

for index in question_data:
    ques = index["question"]
    answer = index["correct_answer"]
    question = questions(ques, answer)
    question_bank.append(question)

quiz = quiz_brain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("you've completed the quiz!")
print(f"your final score was {quiz.score}/{quiz.question_number}\n")
