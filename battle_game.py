# Simple RPG Game
print("Welcome to the Simple RPG!")
print("=" * 30)

# Get player's name
player_name = input("Hello traveler! What's your name? ")
gold = 0
hp = 100
print(f"Nice to meet you, {player_name}!")
while(True):
    # Choose a location
    print("\nWhere would you like to go?")
    print("1. Dark Forest")
    print("2. Mystic Mountains")
    print("3. Haunted Castle")
    print("4. Deep Sea")
    location_choice = input("Enter your choice (1-4): ")
    
    # Process location choice
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
        location = "Deep Sea"
        enemy = "Bloop"
    else:
        location = "Mysterious Place"
        enemy = "Unknown Creature"
    
    print(f"\nYou've arrived at the {location}!")
    
    # Choose a weapon
    print("\nChoose your weapon:")
    print("1. Enchanted Bow")
    print("2. Sword")
    print("3. Trident")
    print("4. Magic Staff")
    weapon_choice = input("Enter your choice (1-4): ")
    
    # Process weapon choice
    if weapon_choice == "1":
        weapon = "Enchanted Bow"
    elif weapon_choice == "2":
        weapon = "Sword"
    elif weapon_choice == "3":
        weapon = "Trident"
    elif weapon_choice == "4":
        weapon = "Magic Staff"
    else:
        weapon = "Bare Hands"
    
    print(f"\nYou've chosen the {weapon} as your weapon!")
    
    # Encounter an enemy
    print(f"\nSuddenly, a {enemy} appears!")
    action = input("What will you do? (fight/run/set eyes): ").lower()
    
    # Process the encounter
    if action == "fight":
        print(f"You bravely attack the {enemy} with your {weapon}!")
        
        # Simple combat outcome
        if (weapon == "Sword" and enemy == "Goblin") or \
           (weapon == "Enchanted Bow" and enemy == "Dragon") or \
           (weapon == "Magic Staff" and enemy == "Ghost") or \
           (weapon == "Trident" and enemy == "Bloop") : 
            print(f"Your {weapon} is effective against the {enemy}! You win!")
            # javier = dapet gold di sini
            gold = gold+100
        else:
            print(f"The {enemy} is too strong for your {weapon}. You lose!")
            #javier kurangi HP
            hp = hp-30
            
    elif action == "run":
        print("You run away safely!")
    elif action == "set eyes":
        print("THE ENEMY HAS FOUND YOU, and he doesn't care about you,you are lucky, you Survived")
    else:
        print("You hesitate, and the enemy attacks! You lose!")
    # javier = sisa gold
    print(f"now you have {gold} gold")
    print(f"now your HP {hp}")
    if hp > 0 :
        # jika hp tidak habis, lanjut bermain
        print(f"Lanjut bermain Atau tidak")
        aksi = input("enter your choice lanjut / tidak")
        if aksi == "lanjut":
            print("okey lanjut")
        elif aksi == "tidak":
            print("okey stop")
            break
    else:
        print (f"your hp {hp} , you lose")
        print (f"Game Over")
        break
print("\nThanks for playing the Simple RPG!")