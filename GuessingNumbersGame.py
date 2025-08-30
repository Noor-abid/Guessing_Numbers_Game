import random

def guessing_game(guessLimit, number):
    random_number = random.randint(1, number)
    while guessLimit > 0:
        try:
            guess = int(input('What is your guess? '))
        except ValueError:
            print('Only integers are allowed!')
            continue 
        if guess < 1 or guess > number:
            print(f'Your guess is out of range! Enter a number between 1 and {number}.')
            continue

        guessLimit -= 1
        if random_number == guess:
            print('🎉 Congrats, You got it right!')
            break
        else:
            print('❌ Sorry, That was wrong!')
            print(f'You have {guessLimit} guess(es) left')

    else:  
        print('Game over!')
        print(f'The random number was {random_number}')


def easy():
    print("You are to guess a number between 1 and 10, and you have 6 guesses")
    guessing_game(6, 10)

def medium():
    print("You are to guess a number between 1 and 20, and you have 4 guesses")
    guessing_game(4, 20)

def hard():
    print("You are to guess a number between 1 and 50, and you have 3 guesses")
    guessing_game(3, 50)

def try_again():
    again = input('Do you want to play again? Yes/No: ')
    if again.upper() == 'YES':
        welcome()
    elif again.upper() == 'NO':
        print('Thanks for playing!')
        return
    else:
        print('Invalid input, please type Yes or No.')
        try_again()

def welcome():
    print('🎮 Welcome to the guessing game 🎮')
    difficulty = input("Choose your level between Easy, Medium and Hard: ")
    if difficulty.upper() == "EASY":
        easy()
        try_again()
    elif difficulty.upper() == "MEDIUM":
        medium()
        try_again()
    elif difficulty.upper() == "HARD":
        hard()
        try_again()
    else:
        print("⚠️ Wrong input, try again!")
        welcome()

welcome()
