import copy

def get_lines():
    with open("input.txt") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

Lines = get_lines()

global decks
decks = [ [], [] ]

def get_decks():
    i = 1
    while Lines[i] != 'Player 2:' and i < len(Lines):
        decks[0].append(int(Lines[i]))
        i += 1
    
    i +=1
    while i < len(Lines):
        decks[1].append(int(Lines[i]))
        i += 1

def play_war():
    while len(decks[0]) > 0 and len(decks[1]) > 0:
        cards = [ decks[0].pop(0), decks[1].pop(0) ]
        winner = int(cards[1] > cards[0])
        decks[winner].append(cards[winner])
        decks[winner].append(cards[1 - winner])

def calc_score(deck):
    print(sum([count * card for count, card in enumerate(reversed(deck), 1)]))

get_decks()
play_war()
calc_score(decks[int(len(decks[0]) == 0)])