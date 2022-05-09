#Hope Crisafi
#Lab 4
#4/20/21
#Grace Parker

#NJW 8.5/10

import random

#Task 1

integer = int(input('enter an integer greater than 10: '))
#NJW Didn't you just have a try? (-0.5)
numTries = 0

while integer <=10:
    integer = int(input('please, enter an integer greater than 10: '))
    numTries = numTries + 1

#NJW We don't need this test inside the loop
#NJW Remove the IF and unindent everything below.    
    if integer > 10:
        print('Success')
        numTries = numTries + 1
        print('Number of tries:',numTries)


# #Task 2

inty = int(input('enter an integer: '))

while inty != -1:
    if inty % 2 == 0:
        print('You entered an even number')
        inty = int(input('enter an integer: '))
#NJW This can be an else. If it's NOT -1, it can
#NJW ONLY be even or odd
    if inty % 2 != 0:
        print('You entered an odd number')
        inty = int(input('enter an integer: '))

#NJW This shouldn't be in the loop
#NJW NOR is the if required
    if inty == -1:
        print('Done')


#Task 3

print('Your starting budget is $100')

budget = 100
purchaseAmount = float(input('enter a purchase amount: '))
#NJW Why do we need to make a purchase BEFORE the loop?

while budget > 0:
    budget = budget - purchaseAmount
    print('Budget remaining:','{:.2f}'.format(budget))

#NJW ALL of this should be OUTSIDE the loop.
#NJW The last thing in the loop is getting the next purchase    
    if budget < 0:
        print('You are','{:.2f}'.format(abs(budget)),'over budget')

    if budget == 0:
        print('You have no budget money remaining, nice') 

    if budget > 0:
        purchaseAmount = float(input('enter another purchase amount: '))

 

#Task 4

# Part A
# secret = 7
# guess = int(input('enter your guess here: '))

# while guess != secret: 
#     guess = int(input('WRONG. Guess again: '))
#     if guess == secret:
#         print('You guessed correctly')


#Part B-E
secret = int(random.randint(1,100))
guess = int(input('enter your guess here: '))
numGuesses = 1


#NJW I went through the 'and' code Monday.
#NJW If there are TWO reasons for the loop to run
#NJW (we haven't guessed yet AND it's less than 5 guesses)
#NJW We should make that explicit in the while loop
#NJW boolean condition (-0.5). There ONLY needs to be ONE loop (-0.5) 

while guess != secret:
    if numGuesses == 5:
        print('Your last guess was:',guess)
        print('You did not guess it, the correct answer was:',secret,)
        print('it took you',numGuesses,'tries.')
        numGuesses = 6
    while numGuesses != 5 and numGuesses !=6:
        if guess > secret:
            guess = int(input('Your guess is too high. Guess again: '))
            numGuesses = numGuesses +1 
        if guess < secret:
            guess = int(input('Your guess is too low. Guess again: '))
            numGuesses = numGuesses +1 
        if guess == secret:
            print('You guessed correctly')
            print('Number of attempts:',numGuesses + 1)

