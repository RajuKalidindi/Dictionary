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

    elif len(get_close_matches(word, data.keys())) > 0:
        suggest = get_close_matches(word, data.keys())[0]
        print("Did you mean %s?" % suggest)
        y_n = input("Enter Y for yes and N for no: ")
        y_n = y_n.upper()

        if y_n == "Y":
            return data[suggest]

        elif y_n == "N":
            return "There is no such word! Please check."

        else:
            return "Please enter Y or N only"

    else:
        return "There is no such word! Please check."

word = input("Enter a word: ")
word = word.lower()

output = search(word)

if type(output) == list:
    n = 1
    for item in output:
        print(str(n) + ") " + str(item))
        n = n + 1

else:
    print(output)
