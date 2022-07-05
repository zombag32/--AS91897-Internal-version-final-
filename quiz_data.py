import requests
# to sort the amount (questions and answers) needed for Quiz as well as the data for quiz
parameters = {
    "amount": 10,
    "type": "multiple"
}

# to get the questions and answers from json data
response = requests.get(url="https://opentdb.com/api.php?amount=10&category=17&difficulty=medium&type=multiple", params=parameters)
question_data = response.json()["results"]