import json
import requests
import pandas as pd

# Name: Team TUNA (Henry Gruber, Lucas Ransick)
# email:  gruberhw@mail.uc.edu & ransiclg@mail.uc.edu
# Assignment Number: Assignment 10 
# Due Date:   11/14/2024
# Course #/Section:   IS 4010 - 001
# Semester/Year:  Fall 2024
# Brief Description of the assignment: API request, cleaned up, printed to console, converted to .csv located in working directory
# Brief Description of what this module does. gets api request, prints, converts to .csv
# Citations: our in class JSON VS project
# Anything else that's relevant: n/a

def TriviaAPI():
    response = requests.get('https://opentdb.com/api.php?amount=5&category=21&difficulty=easy&type=multiple')
    json_string = response.content
    
    parsed_json = json.loads(json_string)
    for question in parsed_json['results']:
        print(question['question'])
        print(question['correct_answer'])
        df = pd.DataFrame(parsed_json)
        df.to_csv('trvia.csv', index=False)

    
TriviaAPI()
