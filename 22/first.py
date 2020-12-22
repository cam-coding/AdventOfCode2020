from collections import deque
import math
import pprint
import copy

def get_lines():
    with open("input.txt") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

Lines = get_lines()
Width = len(Lines[0])
Height = len(Lines)

global p1Deck
p1Deck = []
global p2Deck
p2Deck = []

def get_decks():
    i = 1
    while Lines[i] != 'Player 2:' and i < len(Lines):
        p1Deck.append(int(Lines[i]))
        i += 1
    
    i +=1
    while i < Height:
        p2Deck.append(int(Lines[i]))
        i += 1

def play_war():
    while len(p1Deck) > 0 and len(p2Deck) > 0:
        card1 = p1Deck.pop(0)
        card2 = p2Deck.pop(0)

        if card1 > card2:
            p1Deck.append(card1)
            p1Deck.append(card2)
        else:
            p2Deck.append(card2)
            p2Deck.append(card1)
    print(p1Deck)
    print("hi")
    print(p2Deck)

def calc_score(deck):
    total = 0
    multiplier = 1
    for i in range(len(deck)-1, -1, -1):
        total += deck[i] * multiplier
        #print(deck[i] * multiplier)
        multiplier += 1
    print(total)

get_decks()
print(p1Deck)
print(p2Deck)
play_war()
if len(p1Deck) == 0:
    calc_score(p2Deck)
else:
    calc_score(p1Deck)