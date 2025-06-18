
class QuizBrain:
    def __init__(self,q_list):
        self.q_number = 0
        self.score = 0
        self.q_list = q_list

    def still_has_questions(self):
        return  self.q_number < len(self.q_list)

    def next_question(self, user_answer):
        current_question = self.q_list[self.q_number]
        self.q_number += 1
        user_answer = input(f"Q.{self.q_number}: {current_question.text} (True/False)")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer == correct_answer.lower() or user_answer == correct_answer.upper():
            print("you got it right!")
            self.score+=1

        else:
            print("wrong answer!")
            print(f"correct answer: {user_answer}")
            print("your current score: {self.score}/{self.q_number}")
            print("\n")




