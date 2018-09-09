import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def search(word):
    if word in data:
        return data[word]

    elif word.title() in data:
        return data[word.title()]

    elif word.upper() in data:
        return data[word.upper()]

    else:
        return "There is no such word! Please check."

word = input("Enter a word: ")
word = word.lower()

output = search(word)

if type(output) == list:
    for item in output:
        print(str(item))

else:
    print(output)
