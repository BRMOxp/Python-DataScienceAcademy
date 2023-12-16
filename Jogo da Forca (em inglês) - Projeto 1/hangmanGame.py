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

#display the hangman
def display_hangman(remaining_attempts):

    # list of stages
    stages = [  # stage 6 (final)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # stage 5
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # stage 4
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # stage 3
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # stage 2
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # stage 1
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # stage 0
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[remaining_attempts]
#function
def game():
    
    #word list of the game
    words = ['banana','avocado','grape','orange','strawberry','pineapple','apple']

    #randomly choose a word
    word = random.choice(words)

    #list comprehension
    discovered_letters = ['_' for letter in word]

    #attempts
    remaining_attempts = 6

    #wrong letters list
    wrong_letters = []

    while remaining_attempts > 0:
        
        #cleans the screen
        clean_screen()
        #prints
        print(display_hangman(remaining_attempts))
        print("Guess the word below:\n")
        print(" ".join(discovered_letters))
        print("\nRemaining attempts: ",remaining_attempts)
        print("Discovered letters:", " ".join(wrong_letters))

        #attempt
        attempt = input("\nEnter a letter: ").lower()

        #conditional
        if attempt in word:
            index = 0
            for letter in word:
                if attempt == letter:
                    discovered_letters[index] = letter
                index += 1
        else:
            remaining_attempts -=1
            wrong_letters.append(attempt)
        
        if "_" not in discovered_letters:
            print("\nYou win!, the word was:",word)
            break

    if "_" in discovered_letters:
        print("\nYou lose!, the word was:",word)

if __name__ == "__main__":
    game()