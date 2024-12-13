import random
import hangman_stages   # create hangman stages in a separate file or refer from line 30..
import word_file        # create a file containing few words....

lives = 6
chosen_word = random.choice(word_file.words)
#print(chosen_word)
display = []
for i in range(len(chosen_word)):
    display += '_'
print(display)
game_over = False
while not game_over:
    guessed_letter = input("Guess a letter:\n").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter
    print(f"Correctly guessed letters are : {display}")
    if guessed_letter not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You Lose")

    if '_' not in display:
        game_over = True
        print("You Win")
    print(hangman_stages.stages[lives])
#here is the hangman stages file:
stages = ["""
       -----
       |    |
       O    |
      /|\   |
      / \   |
            |
    ""","""
       -----
       |   |
       O   |
      /|\  |
      /    |
           |
    ""","""
       -----
       |   |
       O   |
      /|\  |
           |
           |
    ""","""
       -----
      |   |
      O   |
     /|   |
          |
          |
    ""","""
       -----
       |   |
       O   |
       |   |
           |
           |
    ""","""
       -----
       |   |
       O   |
           |
           |
           |
    ""","""
       -----
       |   |
           |
           |
           |
           |
    """]
