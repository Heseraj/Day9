# This is the 9th day
# Dictionaries
# the game of bidders

#%%
programming_dictionary = {
    "bug":"an error in a program that prevents the program from running as expected",
    "function": "a piece of code that you cna esily call over and over again",
}

print(programming_dictionary["bug"])

#%%
# adding item to dictionaries

programming_dictionary["loop"] = "the action of doing something over and over again."
#%%
print(programming_dictionary)

#%% for looping in a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])






#%%
student_scores = {
    "Harry":82,
    "Ron":78,
    "Hermione":99,
    "Draco":74,
    "Neville":62,
}
#TODO-1 create a new empty dictionary
student_grading = {

}

for student in student_scores:
    score = student_scores[student]
    if score > 91:
        student_grading[student] = "OutSanding"
    elif score > 81:
        student_grading[student] = "Exceeds Expectation"
    elif score > 71:
        student_grading[student] = "Acceptable"
    elif score > 61:
        student_grading[student] = "needs improvement"
    else:
        student_grading[student] ="Fail"
    print(student)
print(student_grading)



#%% Nestiing Dictionaries
capitals = {
    "France":"Paris",
    "Germany": "Berlin"
}

travel_Log = {
    "France":["Paris", "Lille", "Dijon"],
    "Germany":["Berlin", "Hamburg", "Stuttgart"]
}

#%%
travel_Log_1 = {
    "France":{"Cities_Visited": ["Paris", "Lille", "Dijon"], "Numbers_of_Visit":3},
    "Germany":{"Cities_Visited": ["Berlin", "Hamburg", "Stuttgart"], "Numbers_of_Visit":1}
}
#%%
#TODO: Creaitng Dictionaries Inside List

travel_log2 = [
    {
        "country": "France",
        "Cities_Visited": ["Paris", "Lille", "Dijon"],
        "Numbers_of_Visit":3
    },
    {
        "country": "Germany",
        "Cities_Visited": ["Berlin", "Hamburg", "Stuttgart"],
        "Numbers_of_Visit":1
    },
]

#%%
#TODO create a function that add items to list
def add_new_country(country_traveled, cities, number_visits):
    new_country = {}
    new_country["country"] = country_traveled
    new_country["Cities_Visited"] = cities
    new_country["Numbers_of_Visit"] = number_visits
    travel_log2.append(new_country)

# Pay attention to not leave a comma at the end of your codes for defining functions

#%%
add_new_country(country_traveled="Russia", cities=["Moscow", "Sochi", "Tatar"], number_visits=3)

print(travel_log2)
#%%
#ToDO Blind Auction Program
from replit import clear
clear()
from blind_art_auction import logo
bidders = {}

def blind_auction():
    name = input("what is your name? \n")
    bid = (input("How much do you bid? \n"))
    bidders[name] = bid
def revealing_winner(bidders):
    for name in bidders:
        highest_bid = 0
        current_bid = bidders[name]
        if current_bid > highest_bid.__str__():
            highest_bid = current_bid
            winner = name
    
    print(f"the current winnder is {winner} and with the bid amount of ${highest_bid}")

# revealing_winner(bidders)

#%%
new_person = True

while new_person:
    blind_auction()
    new_bids = input("Is there a new bidder? Yes or NO:").lower()
    if new_bids == "yes":
        clear()
    elif new_bids == "no":
        new_person = False
        revealing_winner(bidders)
    else:
        print("Sorry! I can't understand")

#%%

#%%

#%%
#%%
#%%
#%%

