# CALL COMMANDS FOR GET / returnExercise
#       response = requests.get("http://127.0.0.1:5000/exercises/MUSCLE-NAME")
#       response.json()
# Replace MUSCLE-NAME with specific muscle
import requests

def findExercises(muscle):
    response = requests.get("http://127.0.0.1:5000/exercises/{}".format(muscle))
    return response.json()

muscle = "chest"
print(muscle)
# testString = "http://127.0.0.1:5000/exercises/{}".format(muscle)
# print(testString)
exercies = findExercises(muscle)
#print(findExercises(muscle))

print(exercies)