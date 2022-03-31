from genericpath import exists
from operator import contains, indexOf
import os
from random import randint, randrange

DICTIONARY = '/usr/share/dict/words'
SPACING = 100

class Word:
    def __init__(self, word):
        self.word = word
        self.answers = []
        self.failed_guesses = []

        for i in self.word:
            self.answers.append('_')


def load_dict():
    if exists(DICTIONARY):
        with open(DICTIONARY, 'r') as f:
            dictionary = f.readlines()

    return dictionary

def clean_word(word):
    return word[0:len(word)-1]

def print_hangman(board, word):

    num_failed = len(word.failed_guesses)

    if num_failed == 0:

        board +=  ("|%s|\n") % (" _________".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" |        |".center(SPACING, ' '))
        board +=  ("|%s|\n") % ("          |".center(SPACING, ' '))
        board +=  ("|%s|\n") % ("          |".center(SPACING, ' '))
        board +=  ("|%s|\n") % ("          |".center(SPACING, ' '))
        board +=  ("|%s|\n") % ("          |".center(SPACING, ' '))
        board +=  ("|%s|\n") % ("          |".center(SPACING, ' '))
        board +=  ("|%s|\n") % ("-------------".center(SPACING, ' '))

    elif num_failed == 1:

        board +=  ("|%s|\n") % (" _________".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" |        |".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" O        |".center(SPACING, ' '))
        board +=  ("|%s|\n") % ("          |".center(SPACING, ' '))
        board +=  ("|%s|\n") % ("          |".center(SPACING, ' '))
        board +=  ("|%s|\n") % ("          |".center(SPACING, ' '))
        board +=  ("|%s|\n") % ("          |".center(SPACING, ' '))
        board +=  ("|%s|\n") % ("-------------".center(SPACING, ' '))

    elif num_failed == 2:
        
        board +=  ("|%s|\n") % (" _________".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" |         |".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" O         |".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" |         |".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" |         |".center(SPACING, ' '))
        board +=  ("|%s|\n") % ("           |".center(SPACING, ' '))
        board +=  ("|%s|\n") % ("           |".center(SPACING, ' '))
        board +=  ("|%s|\n") % ("-------------".center(SPACING, ' '))

    elif num_failed == 3:

        board +=  ("|%s|\n") % ("__________".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" |        |".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" O        |".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" |        |".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" |        |".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" /        |".center(SPACING, ' '))
        board +=  ("|%s|\n") % ("          |".center(SPACING, ' '))
        board +=  ("|%s|\n") % ("-------------".center(SPACING, ' '))

    elif num_failed == 4:

        board +=  ("|%s|\n") % ("__________".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" |        |".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" O        |".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" |        |".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" |        |".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" /        |".center(SPACING, ' '))
        board +=  ("|%s|\n") % ("          |".center(SPACING, ' '))
        board +=  ("|%s|\n") % ("-------------".center(SPACING, ' '))

    elif num_failed == 5:

        board +=  ("|%s|\n") % ("__________".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" |        |".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" O        |".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" |        |".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" |        |".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" /\       |".center(SPACING, ' '))
        board +=  ("|%s|\n") % ("          |".center(SPACING, ' '))
        board +=  ("|%s|\n") % ("-------------".center(SPACING, ' '))

    elif num_failed == 6:

        board +=  ("|%s|\n") % ("__________".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" |        |".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" O        |".center(SPACING, ' '))
        board +=  ("|%s|\n") % ("\|        |".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" |        |".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" /\       |".center(SPACING, ' '))
        board +=  ("|%s|\n") % ("          |".center(SPACING, ' '))
        board +=  ("|%s|\n") % ("-------------".center(SPACING, ' '))

    elif num_failed == 7:

        board +=  ("|%s|\n") % ("__________".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" |        |".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" O        |".center(SPACING, ' '))
        board +=  ("|%s|\n") % ("\|/       |".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" |        |".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" /\       |".center(SPACING, ' '))
        board +=  ("|%s|\n") % ("          |".center(SPACING, ' '))
        board +=  ("|%s|\n") % ("-------------".center(SPACING, ' '))

    return board


def print_gameboard(word):

    board =     ("+%s+\n") % ('-' * SPACING)
    board +=    ("|%s|\n") % ('HANGMAN'.center(SPACING, ' '))
    board +=    ("+%s+\n") % ('-' * SPACING)

    board = print_hangman(board, word)

    board += ("|")
    answer = ""
    for letter in word.answers:
        answer += letter + " "
    board += ("%s|\n") % (answer.center(SPACING, ' '))

    board += ("+%s+\n") % ('-' * SPACING)

    guess = "USED LETTERS: "
    for letter in word.failed_guesses:
        guess += letter + " "
    board += ("|%s|\n") % guess.center(SPACING, ' ')
    board += ("+%s+\n") % ('-' * SPACING)

    print(board)

def print_menu(menu_items):

    max = 0
    for i in menu_items:
        if len(i) > max:
            max = len(i)

    for i in range(len(menu_items)):
        if len(menu_items[i]) < max:
            tmp = menu_items[i].ljust(max, ' ')
            menu_items[i] = tmp

    menu =     ("+%s+\n") % ('-' * SPACING)
    menu +=    ("|%s|\n") % ('HANGMAN'.center(SPACING, ' '))
    menu +=    ("+%s+\n") % ('-' * SPACING)

    for i in range(len(menu_items)):
        menu += ("|%s|\n") % ((str(i) + ". " + menu_items[i]).center(SPACING, ' '))
    
    menu += ("+%s+\n") % ('-' * SPACING)

    print(menu)

def str_answers(word):
    answer = ""
    for letter in word.answers:
        answer += letter
    
    return answer

def main():
    menu = ['Play Game', 'Exit']
    dictionary = load_dict()

    play_game = False

    while True:
        print_menu(menu)

        player_choice = int(input("\nPlease select a menu option: "))

        if player_choice == 0:
            play_game = True
        elif player_choice == 1:
            exit()

        while play_game == True:
            word = Word(clean_word(dictionary[randint(0, len(dictionary) - 1)].lower()))



            while str_answers(word) != word.word:
                print_gameboard(word)

                if len(word.failed_guesses) != 7:
                    guess = input("Guess a letter: ").lower()

                    while contains(word.answers, guess) | contains(word.failed_guesses, guess):
                        guess = input("You already guessed that letter. Pick another one: ").lower()

                    if contains(word.word, guess):
                        indices = [i for i, x in enumerate(word.word) if x == guess]

                        for i in indices:
                            word.answers[i] = guess

                    if not contains(word.word, guess):
                        word.failed_guesses.append(guess)
                        word.failed_guesses.sort()

                else:
                    print("You failed.")
                    print("The word is: " + word.word + "\n")
                    
                    play_game = False
                    break

            if word.word == str_answers(word):
                print_gameboard(word)
                print("Congratulations! You won!")
                play_game = False

main()



