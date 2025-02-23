import random

def getAnswear(answearNumber):
    if answearNumber == 1:
        return 'It is certain'
    elif answearNumber == 2:
        return 'It is decided so '
    elif answearNumber == 3:
        return 'Yes'
r = random.randint(1,3)
fortune = getAnswear(r)
print(fortune)
