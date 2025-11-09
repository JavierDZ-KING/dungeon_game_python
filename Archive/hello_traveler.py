"""
prompt:
create me simple rpg in python based on console
just like input then if else

game logic: it starts with hello traveler whats ur name, choose where to go from 3 places, choose weapon

make it really simple, just to teach how to code
"""

player_name = input("Hello traveler! What's your name? ")
print(f"Nice to meet you, {player_name}!")

# Choose a location
print("\nWhere would you like to go?")
print("1. Dark Forest")
print("2. Mystic Mountains")
print("3. Haunted Castle")
print("4. Pesantren")
location_choice = input("Enter your choice (1-4): ")

# Process location choice
while(location_choice < "1" or location_choice > "4"):
    location_choice = input("Bad input, please enter proper choice (1-4): ")

if location_choice == "1":
    location = "Dark Forest"
    enemy = "Goblin"
elif location_choice == "2":
    location = "Mystic Mountains"
    enemy = "Dragon"
elif location_choice == "3":
    location = "Haunted Castle"
    enemy = "Ghost"
elif location_choice == "4":
    location = "Pesantren"
    enemy = "Bad Senior"
else:
    location = "Mysterious Place"
    enemy = "Unknown Creature"

print(f"\nYou've arrived at the {location}!")

# Choose a weapon
print("\nChoose your weapon:")
print("1. Sword")
print("2. Bow")
print("3. Magic Staff")
weapon_choice = input("Enter your choice (1-3): ")

# Process weapon choice
if weapon_choice == "1":
    weapon = "Sword"
elif weapon_choice == "2":
    weapon = "Bow"
elif weapon_choice == "3":
    weapon = "Magic Staff"
else:
    weapon = "Bare Hands"

print(f"\nYou've chosen the {weapon} as your weapon!")

# Encounter an enemy
print(f"\nSuddenly, a {enemy} appears!")
action = input("What will you do? (fight/run): ").lower()

# Process the encounter
if action == "fight":
    print(f"You bravely attack the {enemy} with your {weapon}!")
    
    # Simple combat outcome
    if (weapon == "Sword" and enemy == "Goblin") or (weapon == "Bow" and enemy == "Dragon") or (weapon == "Magic Staff" and enemy == "Ghost") or (weapon == "Bow" and enemy == "Bad Senior"):
        print(f"Your {weapon} is effective against the {enemy}! You win!")
    else:
        print(f"The {enemy} is too strong for your {weapon}. You lose!")
        
elif action == "run":
    print("You run away safely!")
else:
    print("You hesitate, and the enemy attacks! You lose!")

print("\nThanks for playing the Simple RPG!")