import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter if Yes, or No if No: " % get_close_matches(w, data.keys())[0])
        yn = yn.upper()
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word dosent exist. Please double check it"
        else:
            return "We didnt understand your entry"

    else:
        return "the word does not exix. Please double chechk it`"

word = input("Enter word: ")

output =translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
