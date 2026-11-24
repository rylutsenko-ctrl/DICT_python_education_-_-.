import random

print("HANGMAN")
words = ["python", "java", "javascript", "php"]

while True:
    action = input('Type "play" to play the game, "exit" to quit: ')
    if action == "exit":
        break
    if action != "play":
        continue
    secret_word = random.choice(words)
    hint = ["-"] * len(secret_word)
    guessed_letters = set()
    lives = 8
    while lives > 0 and "-" in hint:
        print()
        print("".join(hint))
        letter = input("Input a letter: ")
        if len(letter) != 1:
            print("You should input a single letter")
            continue
        if not ("a" <= letter <= "z"):
            print("Please enter a lowercase English letter")
            continue
        if letter in guessed_letters:
            print("You've already guessed this letter")
            continue
        guessed_letters.add(letter)
        if letter in secret_word:
            for i in range(len(secret_word)):
                if secret_word[i] == letter:
                    hint[i] = letter
        else:
            print("That letter doesn't appear in the word")
            lives -= 1
    if "-" not in hint:
        print()
        print(f"You guessed the word {secret_word}!")
        print("You survived!")
    else:
        print("You lost!")
