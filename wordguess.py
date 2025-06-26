print("Guess the word\n The hint is:'It is a machine'")
secret_word="computer"
secret_list= list(secret_word)
guessed_word=["_"]*len(secret_list)
guessed_letters=[] #keeps trackof words that user has already guessed

while "_" in guessed_word:
    print("Current word: ", " ".join(guessed_word))
    guess=input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("Youu have already guessed that!")
        continue

    guessed_letters.append(guess)

    if guess in secret_list:
        for i in range(len(secret_list)):
            if secret_list[i]== guess:
                guessed_word[i]= guess
        print("Good job!")
    else:
        print("Wrong guess!")

print("\nYou guessed the word!", secret_word)
