import random

def game():
    print('Your are playing a game....')
    score=random.randint(1,62)
    # fetch the highscore
    with open("c9/hiscore.txt") as f:
        hiscore=f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0
    print(f'Your score: {score}')
    if(score>hiscore):
        with open("c9/hiscore.txt","w") as f:
            f.write(str(score))
    return score

game()
