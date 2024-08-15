import random
import hangman_diagram  

word_list = ["apple", "pineapple", "mango"]

lives = 6
chosen_word = random.choice(word_list)
display = ['_'] * len(chosen_word)  
game_over = False

print(f"Word to guess: {' '.join(display)}")  

while not game_over:
    guess_any_letter = input("Enter a letter to guess: ").lower()

    if guess_any_letter in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess_any_letter:
                display[position] = guess_any_letter
    else:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose the game!")
            break

    if '_' not in display:
        game_over = True
        print("Congratulations! You win!")
        break

    print(f"Current word: {' '.join(display)}")
    print(hangman_diagram.diagram[lives])

