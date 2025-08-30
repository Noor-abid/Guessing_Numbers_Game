import random
def guessing_game(guessLimit, number):
    random_number=random.randint(1, number)
    try:
     while guessLimit > 0:
        guess=int(input('What is your guess?'))
        guessLimit-=1
        if random_number==guess:
            print('Congrats, You got it right!')
            break
        elif guess > number:
            print('Your guess is out of range!')
            print(f'You have {guessLimit} guess(es) left')
        else:
            print('Sorry, That was wrong!')
            print(f'You have {guessLimit} guess(es) left')
            print('Game over!')
            print(f'The randon number was {random_number}')
    except ValueError:
     print('Only integeres are allowed')
def easy():
   print("You are to guess a number between 1 and 10, and you have 6 guesses")
   guessing_game(6, 10)
def medium():
   print("You are to guess a number between 1 and 20, and you have 4 guesses")
   guessing_game(4, 20)
def hard():
   print("You are to guess a number between 1 and 50, and you have 3 guesses")
   guessing_game(3, 50)