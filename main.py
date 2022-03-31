from genericpath import exists
from operator import indexOf
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
        board +=  ("|%s|\n") % ("          |".center(SPACING, ' '))
        board +=  ("|%s|\n") % ("          |".center(SPACING, ' '))
        board +=  ("|%s|\n") % ("-------------".center(SPACING, ' '))

    elif num_failed == 3:

        board +=  ("|%s|\n") % ("__________".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" |        |".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" O        |".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" |        |".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" |        |".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" /         |".center(SPACING, ' '))
        board +=  ("|%s|\n") % ("          |".center(SPACING, ' '))
        board +=  ("|%s|\n") % ("-------------".center(SPACING, ' '))

    elif num_failed == 4:

        board +=  ("|%s|\n") % ("__________".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" |        |".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" O        |".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" |        |".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" |        |".center(SPACING, ' '))
        board +=  ("|%s|\n") % (" /         |".center(SPACING, ' '))
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

    board += ("| USED LETTERS: ")
    guess = ""
    for letter in word.failed_guesses:
        guess += letter + " "
    board += ("%s|\n") % guess.center(SPACING - len("| USED LETTERS: ") + 1, ' ')
    board += ("+%s+\n") % ('-' * SPACING)

    print(board)

def print_menu(menu_items):

    menu = ("+%s+\n") % ('-' * SPACING)

    for i in range(len(menu_items)):
        print(i, menu_items[i])
        menu += ("|%s|\n") % ((str(i) + ". " + menu_items[i]).center(SPACING, ' '))
    
    menu += ("+%s+\n") % ('-' * SPACING)

    print(menu)

def main():
    menu = ['Play Game', 'Exit']
    print_menu(menu)
    dictionary = load_dict()
    word = Word(clean_word(dictionary[randint(0, len(dictionary) - 1)]))

    print_gameboard(word)
main()



