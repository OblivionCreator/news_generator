import language_processing
import random

def generate(text):
    noun_phr, verb, adj = language_processing.tokenize(text) # Converts input text into tokens.
    print(noun_phr, verb, adj)



    randPhrase = random.choice(noun_phr)
    print(randPhrase)

    un_adj = []
    un_verb = []

    for x in adj:
        if x not in randPhrase and x not in un_adj:
            un_adj.append(x)

    for x in verb:
        if x not in randPhrase and x not in un_verb:
            un_verb.append(x)

    print(un_adj)

    if len(un_adj) == 0:
        return False
    if len(un_verb) == 0:
        un_verb = ["IS"]

    rand_un_adj = random.choice(un_adj)
    rand_un_verb = random.choice(un_verb)

    return headlineGenerator("OBLIVION", randPhrase, rand_un_adj, rand_un_verb)

def headlineGenerator(name, phrase, adjective, verb):

    headline = f"BREAKING NEWS: {name.upper()} thinks that {phrase.upper()} {verb.upper()} {adjective.upper()}!"
    print(headline)

while True:
    text = input()
    generate(text)

