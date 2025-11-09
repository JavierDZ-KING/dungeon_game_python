"""
prompt:
create me simple rpg in python based on console
just like input then if else

game logic: we choose our weapon, we choose which dungeon to go to, enemies will show up in random pick based on dungeon, when battle start printout enemy and our health bar for each turn, enemy attacks randomly, we attack and inflict damage based on weapon type (or choose to idle), when win we get money

make it really simple, just to teach how to code

-----------------

PR: 
1. add "Bad Senior" to Forest dungeon
2. add weapon "Silat Kick"
"""

import random

# Simple RPG with Combat System
print("Welcome to the Dungeon Adventure RPG!")
print("=" * 40)

# Player stats
player_health = 100
player_money = 0
player_weapon = None
weapon_damage = 0

# Enemy types by dungeon
dungeon_enemies = {
    "Forest": ["Goblin", "Wolf", "Spider"],
    "Cave": ["Orc", "Bat", "Skeleton"],
    "Castle": ["Knight", "Wizard", "Dragon"],
    "Pesantren": ["Bad Senior"]
}

# Enemy stats [health, min damage, max damage]
enemy_stats = {
    "Goblin": [30, 5, 10],
    "Wolf": [25, 7, 12],
    "Spider": [20, 3, 8],
    "Orc": [40, 10, 15],
    "Bat": [15, 2, 6],
    "Skeleton": [35, 8, 13],
    "Knight": [50, 12, 18],
    "Wizard": [35, 15, 20],
    "Dragon": [70, 20, 25]
}

# Weapon choices
weapons = {
    "1": {"name": "Sword", "damage": (10, 15)},
    "2": {"name": "Bow", "damage": (8, 12, 16)},
    "3": {"name": "Axe", "damage": (12, 18)}
}

# ==============================

# Get player's name
player_name = input("Hello brave adventurer! What's your name? ")
print(f"Welcome, {player_name}!")

# Choose a weapon
print("\nChoose your weapon:")
for key, value in weapons.items():
    print(f"{key}. {value['name']} (Damage: {value['damage'][0]}-{value['damage'][1]})")
    
weapon_choice = input("Enter your choice (1-3): ")
if weapon_choice in weapons:
    player_weapon = weapons[weapon_choice]["name"]
    weapon_damage = weapons[weapon_choice]["damage"]
    print(f"You've chosen the {player_weapon}!")
else:
    player_weapon = "Fists"
    weapon_damage = (1, 3)
    print("Invalid choice! You'll have to use your bare fists.")

# Choose a dungeon
print("\nWhich dungeon would you like to explore?")
print("1. Forest (Easy)")
print("2. Cave (Medium)")
print("3. Castle (Hard)")
dungeon_choice = input("Enter your choice (1-3): ")

if dungeon_choice == "1":
    dungeon = "Forest"
elif dungeon_choice == "2":
    dungeon = "Cave"
elif dungeon_choice == "3":
    dungeon = "Castle"
else:
    dungeon = "Forest"
    print("Invalid choice! Defaulting to Forest.")

print(f"\nYou enter the {dungeon} dungeon...")

# Battle system
def battle(enemy):
    global player_health, player_money
    
    enemy_health = enemy_stats[enemy][0]
    enemy_min_dmg = enemy_stats[enemy][1]
    enemy_max_dmg = enemy_stats[enemy][2]
    
    print(f"\nA wild {enemy} appears!")
    
    while player_health > 0 and enemy_health > 0:
        # Display health bars
        print("\n" + "="*30)
        print(f"{player_name}: {player_health}/100 HP")
        print(f"{enemy}: {enemy_health}/{enemy_stats[enemy][0]} HP")
        print("="*30)
        
        # Player's turn
        print("\nWhat will you do?")
        print("1. Attack")
        print("2. Defend (take less damage next turn)")
        action = input("Enter your choice (1-2): ")
        
        # Player attack
        if action == "1":
            damage = random.randint(weapon_damage[0], weapon_damage[1])
            enemy_health -= damage
            print(f"You attack the {enemy} with your {player_weapon} for {damage} damage!")
        elif action == "2":
            print("You prepare to defend against the next attack!")
            defending = True
        else:
            print("You hesitate and lose your turn!")
            defending = False
        
        # Check if enemy is defeated
        if enemy_health <= 0:
            reward = random.randint(10, 30)
            player_money += reward
            print(f"\nYou defeated the {enemy} and found {reward} gold!")
            break
        
        # Enemy's turn
        enemy_damage = random.randint(enemy_min_dmg, enemy_max_dmg)
        
        if action == "2":  # Player defended
            enemy_damage = max(1, enemy_damage // 2)
            print(f"The {enemy} attacks, but you defend taking only {enemy_damage} damage!")
        else:
            print(f"The {enemy} attacks you for {enemy_damage} damage!")
        
        player_health -= enemy_damage
        
        # Check if player is defeated
        if player_health <= 0:
            print(f"\nYou have been defeated by the {enemy}!")
            break

# Random enemy encounter
enemy = random.choice(dungeon_enemies[dungeon])
battle(enemy)

# Game outcome
if player_health > 0:
    print(f"\nYou survived the {dungeon} dungeon!")
    print(f"Your health: {player_health}/100")
    print(f"Gold collected: {player_money}")
else:
    print("\nGame Over! You didn't make it out of the dungeon.")

print("\nThanks for playing!")