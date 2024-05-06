import html


class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0
        self.current_question = None

    def still_has_questions(self):
        # runs the evaluation and returns the result, shorter than if/else statement
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        # converts html escape characters to plaintext
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer is {correct_answer}.")
