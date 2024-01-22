class quiz_brain:
    def __init__(self, q_list):
        self.question_number = 0
        self.queston_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.queston_list)

    def next_question(self):
        current_question = self.queston_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {current_question.question} (True/False)? :")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_ans, correct_answer ):
        if user_ans.lower() == correct_answer.lower():
            print("you got it right!")
            self.score += 1
        else:
            print("you got it wrong!")
        print(f"the correct answer is {correct_answer}")
        print(f"your current score is: {self.score}/{self.question_number}")
        print("\n")