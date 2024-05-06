import requests

AMOUNT = 10
TYPE = "boolean"
DIFFICULTY = "hard"

parameters = {
    "amount": AMOUNT,
    "type": TYPE,
    "difficulty": DIFFICULTY,
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
print(question_data)
