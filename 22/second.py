import copy

def get_lines():
    with open("input.txt") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

Lines = get_lines()

def get_decks():
    decks = [ [], []]
    i = 1
    while Lines[i] != 'Player 2:':
        decks[0].append(int(Lines[i]))
        i += 1
    
    i +=1
    while i < len(Lines):
        decks[1].append(int(Lines[i]))
        i += 1
    return decks

def play_war_recursion(p1, p2, top):
    # Reddit showed me the speed
    if not top:
        if max(p1) > max(p2):
            return 0
    roundStorage = []
    cards = [0, 0]
    decks = [p1, p2]
    while len(decks[0]) > 0 and len(decks[1]) > 0:
        for round in roundStorage:
            if decks[0] == round[0] and decks[1] == round[1]:
                return 0
        roundStorage.append(copy.deepcopy(decks))
        for i in range(2): cards[i] = decks[i].pop(0)

        winner = 0
        if len(decks[0]) >= cards[0] and len(decks[1]) >= cards[1]:
            winner = play_war_recursion(decks[0][:cards[0]], decks[1][:cards[1]], False)
        elif cards[1] > cards[0]:
            winner = 1
        decks[winner].append(cards[winner])
        decks[winner].append(cards[1 - winner])
    if top:
        return decks[int(len(decks[0]) == 0)]
    return int(len(decks[0]) == 0)

def calc_score(deck):
    print(len(deck))
    print(deck[0])
    print(sum([count * card for count, card in enumerate(reversed(deck), 1)]))

decks = get_decks()
calc_score(play_war_recursion(copy.deepcopy(decks[0]), copy.deepcopy(decks[1]), True))