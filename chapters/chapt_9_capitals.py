import random

capitals_dict = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne",
    }

#def take_only_keys(dict_with_state):
#    """Return only keys form a dics"""
#    list_form_keys = []
#    for state in dict_with_state:
#        list_form_keys.append(state)
#    return list_form_keys

#all_states = take_only_keys(capitals_dict)
#state = random.choice(all_states)
#capital = capitals_dict[state]

state, capital = random.choice(list(capitals_dict.items()))

#user_answear = input(f"Enter a capital of {state}: ")
#while user_answear.lower() != capital.lower():
#    user_answear = input(f"Incorrect, (press 'exit' to finish) enter a capital of {state}: ")
#    if user_answear.lower() == "exit":
#        print("Goodbye")
#        break
#if user_answear.lower() == capital.lower():
#    print("Correct")

while True:
    guess = input(f"What is the capital of '{state}'? ").lower()
    if guess == "exit":
        print(f"The capital of '{state}' is '{capital}'.")
        print("Goodbye")
        break
    elif guess == capital.lower():
        print("Correct! Nice job.")
        break


