import random

def game():
    print('Your are playing a game....')
    # fetch the highscore
    with open("c9/hiscore.txt") as f:
        hiscore=f.read()
    score=random.randint(1,62)
    print(f'Your score: {score}')
    return score

game()
