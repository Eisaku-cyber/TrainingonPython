import random # Making a random number regeration
secretNumber = random.randint(1,10)
print('I have a number between 1 and 10 .')

# Asking for a quess 6 times

for guesstaken in range(1,7):
    print('Take a quess')
    guess = int(input())

    if guess < secretNumber:
        print('Your quess is too low ')
    elif guess > secretNumber:
        print('Your quess is too high')
    else :
        break       #This is the correct quess !

    if guess == secretNumber:
        print ('Good job fag , you quessed number ' + str(guessTaken) )
    else : print ('You losed - WOMP WOMP ! , the number was ' + str(guesstaken))
