import copy

def get_lines():
    with open("input.txt") as f:
        return [line.strip() for line in f.readlines() if line.strip()]
    
Lines = get_lines()

allergenDict = {}
ingredientCount = {}
for line in Lines:
    indexer = line.index('(')
    ingredients = set(line[:indexer].split())
    #hardcode 9 to skip the "contains," in the input string
    allergens = line[indexer+9:len(line)-1].replace(' ', '').split(',')

    for allerg in allergens:
        if allerg not in allergenDict:
            allergenDict[allerg] = []
        allergenDict[allerg].append(ingredients)

#Allergens to potential Ingredients
newDict = {}
for item in allergenDict:
    newDict[item] = list(set.intersection(*map(set,allergenDict[item])))

compare = {}
while (compare != newDict):
    compare = copy.deepcopy(newDict)
    for item in newDict:
        if len(newDict[item]) == 1:
            for x in newDict:
                if x != item and (newDict[item][0] in newDict[x]):
                    newDict[x].remove(newDict[item][0])

output = ''
for item in sorted(newDict.keys()):
    output = output+',' + newDict[item][0]
print(output[1:])