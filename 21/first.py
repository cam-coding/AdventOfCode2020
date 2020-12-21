import copy

def get_lines():
    with open("input.txt") as f:
        return [line.strip() for line in f.readlines() if line.strip()]
    

Lines = get_lines()

allergenDict = {}
allIngredients = set()
ingredientCount = {}
for line in Lines:
    indexer = line.index('(')
    ingredients = set(line[:indexer].split())

    for item in ingredients:
        ingredientCount[item] = ingredientCount.get(item, 0) + 1
    allIngredients = allIngredients.union(ingredients)
    allergens = line[indexer+9:len(line)-1].replace(' ', '').split(',')

    for allerg in allergens:
        if allerg not in allergenDict:
            allergenDict[allerg] = []
        allergenDict[allerg].append(ingredients)

newDict = {}
for item in allergenDict:
    newDict[item] = set.intersection(*map(set,allergenDict[item]))
    
badIngredients = set()
for item in newDict:
    badIngredients = badIngredients.union(newDict[item])
mySum = sum([ingredientCount[x] for x in allIngredients.difference(badIngredients)])
print(mySum)