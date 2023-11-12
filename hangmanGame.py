import random
from os import system, name

#cleans the screen after every execution
def clean_screen():

    #Windows 
    if name == 'nt':
        _= system('cls')

    #Mac or Linux
    else:
        _=system('clear')

#list of stages
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

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

#class
class Hangman:
    #constructor
    def __init__(self,word):
        self.word = word
        self.wrong_letters = []
        self.discovered_letters = []

    #method to discover the letter
    def guess(self, letter):
        if letter in self.word and letter not in self.discovered_letters:
            self.discovered_letters.append(letter)
        elif letter not in self.word and letter not in self.wrong_letters:
            self.wrong_letters.append(letter)
        else:
            return False
        return True
    #method to verify if the game is finished
    def hangman_over(self):
        return self.hangman_won() or (len(self.wrong_letters) == 6)

    #method to verify if player has won
    def hangman_won(self):
        if '_'  not in self.hide_letter():
            return True
        return False
    #method to not show the letter in board
    def hide_letter(self):
        rtn = ''
        for letter in self.word:
            if letter not in self.discovered_letters:
                rtn += '_'
            else:
                rtn += letter
        return rtn
    #method to check game status and print the board in the screen
    def print_game_status(self):
            
            print (board[len(self.wrong_letters)])
            
            print ('\nWord: ' + self.hide_letter())
            
            print ('\nWrong Letters: ',) 
            
            for letter in self.wrong_letters:
                print (letter,) 
            
            print ()
            
            print ('Correct letters: ',)
            
            for letter in self.discovered_letters:
                print (letter,)
            
            print ()
def rand_word():

	#word list of the game
    words = ['banana','avocado','grape','orange','strawberry','pineapple','apple','pear']

    #randomly choose a word
    word = random.choice(words)
        
    return word

def main():

    clean_screen()

    #create the object and select a word randomly
    game = Hangman(rand_word())

    #while game not finished, print the status, ask for a letter and read it
    while not game.hangman_over():
        
        #game status
        game.print_game_status()
        
        #receives a input from terminal
        user_input = input('\nType a letter: ')
        
        #verify if typed letter is part of a word
        game.guess(user_input)

    #verify game status
    game.print_game_status()	

    #prints a message in the screen
    if game.hangman_won():
        print ('\nCongratulations:! You win!!')
    
    else:
        print ('\nGame over! You lose.')
        print ('The word was ' + game.palavra)
#execute the program		
if __name__ == "__main__":
	main()
