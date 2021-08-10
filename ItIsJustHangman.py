# It's just Hangman ... in Python ... forget which book I was reading when I did this lesson while learning Python
# EVI

import random

HANGMANPICS = ['''

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
 =========''', '''

 +---+
 |   | 
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

words = "ant baboon badger bat bear beaver camel cat cheetah clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama lynx mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra "

word_bank = {index: word for index, word in enumerate(words.split())}

def get_custom_word() -> str:
    print('Please enter a word for your friend to guess: \n')
    return input().lower()

def get_random_word(word_bank: dict) -> str:
    r_index = random.randint(0, len(word_bank.values()) - 1)
    return word_bank[r_index]

def display_board(HANGMANPICS, missedLetters,correctLetters, secret_word):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secret_word)

    for i in range(len(secret_word)):
        if secret_word[i] in correctLetters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
    print()

def get_player_guess(already_guessed: set) -> str:
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        print('\n' * 2)
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in already_guessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def word_check(word: str) -> bool:
    if word.isalpha() and len(word) > 2:
        return True
    else:
        print('Word must only contain letters and be 3 or more characters. Re-enter')
        return False

def word_options():
    while True:
        print('Play from word bank (enter: wb) or use a custom word (enter: cw)?')
        word = input()

        if word == "cw":
            word = get_custom_word()
            if word_check(word):
                print('\n' * 50)
                return word
        elif word == "wb":
            word = get_random_word(word_bank)
            return word
        else:
            print('Invalid Entry, Try again')

def have_another_go_at_it() -> bool:
    print('Do you want to have another go at it (play again)? (Yes or No)')
    return input().lower().startswith('y')


# Main body of game - Game Loop
if __name__=='__main__':            
    print('H-A-N-G-M-A-N PY EDITION')

    missed_letters = ''
    correct_letters = ''
    secret_word = word_options()
    game_over = False

    while True:
        
        display_board(HANGMANPICS, missed_letters, correct_letters, secret_word)

        guess = get_player_guess(missed_letters + correct_letters)

        if guess in secret_word:
            correct_letters = correct_letters + guess

        found_all_letters = True    
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                found_all_letters = False
                break
            
        if found_all_letters:
            print('Yes! The secret word is "' + secret_word + '"! You have won!')
            game_over = True
        else:
            if guess not in secret_word:
                missed_letters = missed_letters + guess

            if len(missed_letters) == len(HANGMANPICS) - 1:
                display_board(HANGMANPICS, missed_letters,correct_letters, secret_word)
                print('You have run out of guesses!\nAfter ' + str(len(missed_letters)) + ' missed guesses and ' + str(len(correct_letters)) + ' correct guesses, the word was "' + secret_word + '"')
                game_over = True

        if game_over:
            if have_another_go_at_it():
                missed_letters = ''
                correct_letters = ''
                game_over = False
                secret_word = word_options()
            else:
                break
