import requests

def get_questions(no_of_questions):

    parameters = {
        "amount" : no_of_questions,
        "type" : "boolean",
    }
    response = requests.get(url="https://opentdb.com/api.php",params=parameters)
    response.raise_for_status()

    question_data = response.json()["results"]
    return question_data