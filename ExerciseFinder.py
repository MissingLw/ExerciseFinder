from flask import Flask
from flask import jsonify
from flask import request
import requests
import json

app = Flask(__name__)

# CALL COMMANDS FOR GET / returnExercise
#       response = requests.get("http://127.0.0.1:5000/exercises/chest")
#       response.json()

# return an item based on an exercise request

muscleBank = ["abdominals", "abductors", "adductors", "biceps", "calves", "chest", "forearms", "glutes", "hamstrings", "lats", "lower_back","middle_back","neck","quadriceps","traps","triceps"]

@app.route('/exercises/<string:muscle>', methods=['GET'])
def returnExercise(muscle):
    # Checks to see if the muscle is a valid input for the API, is not case sensitive
    if muscle.casefold() in (muscle.casefold() for muscle in muscleBank):
        # Creates an api request using the specified muscle
        api_url = 'https://api.api-ninjas.com/v1/exercises?muscle={}'.format(muscle)
        response = requests.get(api_url, headers={'X-Api-Key': 'YourAPI Key Goes Here'})
        # Checks to see if the response from the server is valid
        if response.status_code == requests.codes.ok:
            exercise_data = response.json()
            return exercise_data
        else:
            #returns an error if the response is an invalid request
            print("Error:", response.status_code, response.text)
            return jsonify({'Error' : 'Call to API experienced Failure'})
    else:
        #The muscle input was not valid, returns an error
        print("Error, input not valid")
        return jsonify({'Error' : 'Muscle input is not valid'})


if __name__ == "__main__":
    app.run(debug=True)