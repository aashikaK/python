import random

# Initialize players
players = {
    "Player 1": {"health": 100},
    "Player 2": {"health": 100}
}

def shoot(shooter, target):
    # Random hit damage between 10-30
    damage = random.randint(10, 30)
    players[target]["health"] -= damage
    print(f"{shooter} hits {target} for {damage} damage!")
    if players[target]["health"] <= 0:
        players[target]["health"] = 0
        print(f"{target} is fully soaked! 💦")

def show_status():
    print("\n--- Current Status ---")
    for p, stats in players.items():
        print(f"{p}: {stats['health']}% dry")
    print("----------------------\n")

# Game loop
while True:
    show_status()
    
    # Check if someone won
    alive = [p for p, stats in players.items() if stats["health"] > 0]
    if len(alive) == 1:
        print(f"{alive[0]} wins the water fight! 🎉")
        break
    elif len(alive) == 0:
        print("Everyone got soaked! It's a tie! 😆")
        break
    
    # Player 1 turn
    if players["Player 1"]["health"] > 0:
        input("Player 1, press Enter to shoot at Player 2...")
        shoot("Player 1", "Player 2")
    
    # Player 2 turn
    if players["Player 2"]["health"] > 0:
        input("Player 2, press Enter to shoot at Player 1...")
        shoot("Player 2", "Player 1")