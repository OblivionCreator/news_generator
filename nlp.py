import language_processing
import random

def generate(username, text, useverb=True):
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

    return headlineGenerator(username, randPhrase, rand_un_adj, rand_un_verb, useverb)

def headlineGenerator(name, phrase, adjective, verb='', useverb=True):

    if useverb == True:
        v_ = verb
    else:
        v_ = 'IS'

    c_list = ["thinks that", "said that", "stated that", "strongly believes that", "does not believe that", "made it public that they think that", "determined that", "believes that", "did not understand that"]

    c_ = c_list[random.randint(0, len(c_list))]

    headline = f"BREAKING NEWS: {name.upper()} {c_} {phrase.upper()} {v_.upper()} {adjective.upper()}!"

    return headline