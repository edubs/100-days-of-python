from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
import requests
import json

AMOUNT = 10
TYPE = "boolean"
CATEGORY = 18
DIFFICULTY = "hard"


def get_questions():
    parameters = {
        "amount": AMOUNT,
        "type": TYPE,
        "category": CATEGORY,
        "difficulty": DIFFICULTY,
    }
    response = requests.get("https://opentdb.com/api.php", params=parameters, verify=False)
    response.raise_for_status()
    data = response.json()
    question_data = data["results"]
    # print(question_data)

    with open('data.py', 'w', encoding='utf-8') as f:
        f.write(f"question_data = ")
        f.write(json.dumps(question_data, ensure_ascii=False, indent=4))


get_questions()
question_bank = []

for q in question_data:
    question = Question(q["question"], q["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
