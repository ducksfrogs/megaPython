import json

data = json.load(open('data.json'))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        return "the word does not exix. Please double chechk it`"

word = input("Enter word: ")

print(translate(word))