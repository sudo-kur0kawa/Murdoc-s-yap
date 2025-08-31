#19/07/2025
print ("i am murdoc, i'm looking for the bath.")
print ("what should i call you, distinguished young lad?")
user_name = input("tell me, mate. ")

anger = 0

while anger < 3:
    print("do you have any bath in your house, " + user_name + "?")
    answer = input("answer me, mate: ")
    if answer == "YES":
        print("OKAY! OKAY! THANK YOU! DON'T SHOUT, I TRY TO BE NICE!")
        break
    elif answer.lower() == "yes":
        print("thank you. now, tell me where your house is.")
        break
    else:
        anger += 1
        if anger == 1:
            print("oh, aren't you a dirty liar? everyone has bath in their house! be honest with me, " + user_name + ".")
        elif anger == 2:
            print("I don't have time for holding the sexual tension between me and the bath, mate. answer me in a proper way! ")
        else:
            print("ALRIGHT THAT'S IT! YOu BLoOdY gREEedy! you smell anyway!")

mood = input("how's today? ")

if mood == "sad":
    print(mood, "? ", "as i said, world isn't the place for you to rely on. don't be dramatic.")
elif mood == "angry":
    print("calm down, you gremlin.")
else:
    print("i won't deal with that.")

print("anyway, mate, you haven't answered me yet.")

while True:
    answer = input("where is the bath?: ")
    if answer == "i have it":
        break

def murdoc_forgor(name):
    print("oi! ", name, ", show me the bath quickly.")

user_name = input("I am not the one to apologise, blame the time for moving to much forwards, what should i call you? ")
murdoc_forgor(user_name)

#20/07/2025
def get_food():
    return input("what's your favourite food?: ")

def get_drink():
    return input("how about the drink?: ")

def go_bath():
    return input("do you have a bath at your house?: ")

def murdoc_summary(food, drink, bath):
    print("\nMurdoc: ALRIGHT, you gremlin. so you like ", food, " and ", drink, ".")
    if bath == "yes":
        print("and you have a bath! what a lovely thing!")
    else:
        print("shame you don't have a bath. No wonder I can smell you half kilometres away.")

def start():
    food = get_food()
    drink = get_drink()
    bath = go_bath()
    murdoc_summary(food, drink, bath)

start()
            #my bro summarising
answer = []

for i in range (3):
    response = input("what's your favourite Gorillaz songs, mate?: ").lower()
    answer.append(response)

print("\nMurdoc: ugh, those are my least. 2-D wrote these without my supervisor:")
for a in answer:
    print("-", a)

#21/07/2025
memory = {}

album = input("what's your favourite Gorillaz album? ")
track = input("which track? ")
hmm = input("what about Plastic Beach? do you like it? ")

memory["album"] = album
memory["track"] = track
memory ["hmm"] = hmm

print("\nMurdoc summary:")
print(f"album: {memory['album']}")
print(f"track: {memory['track']}")
if memory["hmm"] == "yes":
    print("you like Plastic Beach? Be my guest.")
else:
    print("you can't say you don't like Plastic Beach. not in front of my face. Get out!")

import json

name = input("what's your name? ")
hmm = input("do you like Plastic Beach? ")
drink = input("what's your drink of choice? ").lower()
    #bro storing his memory
murdoc = {
    "name": name,
    "hmm": hmm,
    "drink": drink
}

with open("memory.json", "w") as file:
    json.dump(murdoc, file)

print("\nMurdoc: saved that in my brain, i'll remember.")

with open("memory.json", "r") as file:
    memory = json.load(file)

print (f"\nMurdoc: so... {memory['name']}, yeah?")
if memory['drink'] == "tea":
    print(f"and {memory['drink']}?? Ugh, you're hanging out with 2-D too much")
else:
    print(f"i don't have {memory['drink']} right now in me, you poor thing.")

if memory['hmm'] == "yes":
    print("at least your taste in music is banger.")
else:
    print("what a terrible taste of music you have. you must be getting possessed by a scary gargoyle.")

#22/07/2025
print("\nMurdoc: what do you want to say, gremlin? (type 'exit' to stop)")

while True:
    user_input = input("type something: ").lower()

    if user_input == "exit":
        print("Murdoc: alright. get out.")
        break
    elif user_input == "how are you?":
        print("nothing the best when talking to you, obviously.")
    elif user_input == "Gorillaz?":
        print("I AM!!")
    elif user_input == "2-D?":
        print("shut up. you're with me now. ignore that idiot.")
    elif user_input == "i don't like you":
        print("rubbish. one hate doesn't equal to a thousand loves.")
    elif user_input == "i love 2-D":
        print("get well soon,")
    else:
        print("Murdoc: why did you say ", user_input, "?")

mood = "bored"

while True:
    user_input = input("You: ").lower()

    if user_input == "exit":
        print("Murdoc: alright, get out.")
        break
    if "2-d" in user_input:
        mood = "angry"
    elif "i love you" in user_input:
        mood = "chaotic"
    elif "vodka" in user_input:
        mood = "chill"
    elif "gorillaz" in user_input:
        mood = "proud"
    else:
        mood = "bored"
    if mood == "angry":
        print("Murdoc: Ugh!! SHut uP! don't talk about that.")
    elif mood == "chaotic":
        print("Murdoc: RRRRAAAGAGAGGSGGSGSGSGSGGDSAGSFAFSGDFGSF")
    elif mood == "chill":
        print("Murdoc: now we're speaking in my language!")
    elif mood == "proud":
        print("Murdoc: yessssss, YESS! say it LOUDER!!")
    else:
        print("Murdoc: ok, lad.")

#23/07/2025
    #bro remembering users
username = input("Murdoc: who the hell are you? ").lower()
filename = f"{username}.json"

import os
import json

if os.path.exists(filename):
    with open(filename, "r") as file:
        memory = json.load(file)
    print(f"Murdoc: ugh, you again. {memory['name']}")
    if memory["bath"] == "yes":
        print("Murdoc: and you do have bath.")
    else:
        print("Murdoc: dare you come again without your bath!?")
else:
    drink = input("what's your drink? ").lower()
    bath = input("do you have a bath? ").lower()

    memory = {
        "name": username,
        "drink": drink,
        "bath": bath
    }
    with open(filename, "w") as file:
        json.dump(memory, file)
    print("Murdoc: fine, i'll remember this.")

    #bro make u diary
import json
import os
from datetime import datetime

filename = "murdoc_diary.json"

if os.path.exists(filename):
    with open(filename, "r") as file:
        memory = json.load(file)
else:
    memory = {
        "name": input("Murdoc: your name? "),
        "logs": []
    }
    print(f"\nMurdoc: back again {memory['name']}? let's talk.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Murdoc: bye now.")
        break
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")        #timestamp btw
    love_2d_count = sum(1 for entry in memory["logs"]       #heon like when u fw 2-d so he counts
                        if "i love 2-d" in entry["text"].lower())
    if "i love 2-d" in user_input:
        if love_2d_count >= 2:
            print("Murdoc: again??")
        else:
            print("Murdoc: get well soon.")
    log_entry = {
        "time": timestamp,
        "text": user_input
    }
    memory["logs"].append(log_entry)

    print("Murdoc: alright. noted")             #minus in ts, he rlly said that after every words u said
    if user_input.lower() == "read diary":
        print("\nMurdoc: let's take a peek at your tragic little thoughts.")
        for entry in memory["logs"]:
            print(f"[{entry['time']}] You said: {entry['text']}")       #diary format
            continue

with open(filename, "w") as file:
    json.dump(memory, file)

#try a bit of a decorator
user_input = input(print("hello, mate.\n how are you? ")

def murcock_is_asking(func):
    def hehemudz():
        if user_input == "good":
            print("nice one.")
        else:
            print("i can tell.")
            func()
            print("alright, get away now.")
    return hehemudz

@murcock.dont.care
def murdontcare():
    print("do i care or do i not?")
    
murdontcare()
