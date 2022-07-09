#flashcards.py

#import the json module from python3
import json

#open the file and parse the JSON
with open('me-capitals.json', 'r') as f:
    data = json.load(f)
    
# data["cards"] is a way to access a value in a key value pair inside a python dictionary
# the structure looks like this {'cards': [{'q': 'What is the capital of Syria', 'a': 'Damascus'}]}
for i in data["cards"]:
    #i["q"] is used to access the question in each object
    # We'll use the input built-in function to prompt the user to enter an input
    guess = input(i["q"]+">")
    
    #checks for correct answers
    if guess ==i["a"]:
        print("Correct!")
    else:
        #Displays the correct answer
        print("Incorrect! The correct answer was", i["a"])