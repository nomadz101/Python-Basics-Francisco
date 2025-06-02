import random
import time

def create_character(name):
    return {
        "name": name,
        "hp": 100,
        "attack": random.randint(15, 25),
        "defense": random.randint(5, 15),
        "magic": random.randint(10, 20),
        "skill": random.randint(12, 22)
    }

# Define moves for each category with name and damage range multiplier
attack_moves = {
    "Slash": (0.8, 1.2),
    "Heavy Strike": (1.0, 1.5),
    "Quick Jab": (0.5, 1.0)
}

magic_spells = {
    "Fireball": (1.0, 1.4),
    "Ice Spike": (0.8, 1.3),
    "Lightning Bolt": (1.1, 1.6)
}

skills = {
    "Power Shot": (1.0, 1.3),
    "Poison Strike": (0.7, 1.1),
    "Earthquake": (1.2, 1.7)
}

def choose_move(moves):
    print("Choose a move:")
    for i, move in enumerate(moves, 1):
        print(f"{i}. {move}")
    while True:
        choice = input("Enter the number of your move: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(moves):
            return list(moves.keys())[int(choice) - 1]
        print("Invalid choice, try again.")

def perform_attack(attacker, defender):
    print(f"\n{attacker['name']}, choose your attack type:")
    print("1. Attack")
    print("2. Magic")
    print("3. Skill")

    while True:
        choice = input("Select (1-3): ").strip()
        if choice == "1":
            move = choose_move(attack_moves)
            base_stat = attacker["attack"]
            move_type = "Attack"
            break
        elif choice == "2":
            move = choose_move(magic_spells)
            base_stat = attacker["magic"]
            move_type = "Magic"
            break
        elif choice == "3":
            move = choose_move(skills)
            base_stat = attacker["skill"]
            move_type = "Skill"
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

    min_mul, max_mul = None, None
    if move_type == "Attack":
        min_mul, max_mul = attack_moves[move]
    elif move_type == "Magic":
        min_mul, max_mul = magic_spells[move]
    else:
        min_mul, max_mul = skills[move]

    # Calculate damage
    damage = int(base_stat * random.uniform(min_mul, max_mul) - defender["defense"] * 0.5)
    damage = max(damage, 0)

    defender["hp"] -= damage
    defender["hp"] = max(defender["hp"], 0)

    print(f"{attacker['name']} used {move} ({move_type}) and dealt {damage} damage! ({defender['name']} HP: {defender['hp']})")

def battle(char1, char2):
    print(f"\nBattle Start! {char1['name']} VS {char2['name']}\n")
    turn = 0
    while char1["hp"] > 0 and char2["hp"] > 0:
        attacker = char1 if turn % 2 == 0 else char2
        defender = char2 if turn % 2 == 0 else char1
        perform_attack(attacker, defender)
        if defender["hp"] == 0:
            print(f"\n💥 {defender['name']} has been defeated! {attacker['name']} wins!")
            break
        turn += 1
        time.sleep(1)

def main():
    print("=== Turn-Based Battle Simulator ===")
    name1 = input("Enter name for Character 1: ").strip()
    name2 = input("Enter name for Character 2: ").strip()

    char1 = create_character(name1)
    char2 = create_character(name2)

    print(f"\n{name1}'s stats: HP={char1['hp']}, Attack={char1['attack']}, Defense={char1['defense']}, Magic={char1['magic']}, Skill={char1['skill']}")
    print(f"{name2}'s stats: HP={char2['hp']}, Attack={char2['attack']}, Defense={char2['defense']}, Magic={char2['magic']}, Skill={char2['skill']}")

    input("\nPress Enter to start the battle...")
    battle(char1, char2)

if __name__ == "__main__":
    main()
