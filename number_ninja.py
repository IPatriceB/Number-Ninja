import random

# --- COLOR PALETTE ---
RESET  = "\033[0m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"
ORANGE = "\033[38;5;208m"
RED    = "\033[31m"
CYAN   = "\033[36m"
GOLD   = "\033[33;1m"

x = ["1", "easy", "2", "medium", "3", "hard", "4", "impossible"]

player_coin = 0

player_left = False

#   === INTRO ===
    print(f"\n{CYAN}=====¤ NUMBER NINJA ¤=====\n\nThink of a number… lock it in… and let\'s see if I can guess it!{RESET}")
    print(f"Choose Your Level:")
    print(f"{GREEN}🟢 Level 1 — Easy{RESET}")
    print(f"{YELLOW}🟡 Level 2 — Medium{RESET}")
    print(f"{ORANGE}🟠 Level 3 — Hard{RESET}")
    print(f"{RED}🔴 Level 4 — 💀 Impossible 💀\n\n{RESET}")
    print("(Enter \"quit\" to leave the game.)")

    choosen_level = input(f"CHOOSE YOUR LEVEL: ").lower()

    while choosen_level not in x:
        if choosen_level == "quit":
            player_left = True
            print("\nPlayer has left...📴\n")
            quit()
        choosen_level = input("CHOOSE YOUR LEVEL: ").lower()
    
#   === SETTING OF EACH LEVEL ===
    if choosen_level in {"easy", "1"}:
        active_max_range    = 20
        active_max_lives    = 5
        mode_name           = "Easy"
        near_miss_threshold = 2
        active_color        = GREEN
        coin_reward         = 5

    elif choosen_level in {"medium", "2"}:
        active_max_range    = 100
        active_max_lives    = 8
        mode_name           = "Medium"
        near_miss_threshold = 5
        active_color        = YELLOW
        coin_reward         = 20

    elif choosen_level in {"hard", "3"}:
        active_max_range    = 500
        active_max_lives    = 9
        mode_name           = "Hard"
        near_miss_threshold = 10
        active_color        = ORANGE
        coin_reward         = 50

    elif choosen_level in {"impossible", "4"}:
        active_max_range    = 1000
        active_max_lives    = 5
        mode_name           = "Impossible"
        near_miss_threshold = 15
        active_color        = RED
        coin_reward         = 200

# === ITEMS THAT CAN BE BOUGHT IN THE SHOP
    shop = [
        {
            "name": ["Lucky Charm", "1", "lucky charm"],
            "cost": 20,
            "active": False,
        },
        {
            "name": ["Smoke Shield", "2", "smoke shield"],
            "cost": 25,
            "active": False,
        },        
        {
            "name": ["Heart Container", "3", "heart container"],
            "cost": 30,
            "active": False,
            "bonus": 2
        },
        {
            "name": ["Smoke Bomb", "4", "smoke bomb"],
            "cost": 40,
            "active": False,
        }        
    ]


# ===== SHOP SECTION =====
    
    if player_coin > 0:
        # SHOP MENU 
        print(f"\n{CYAN}🛒 ======== NINJA SHOP ======== 🛒{RESET}")
        print(f"{GOLD}Balance : {player_coin}{RESET}\n")
        print("🍀 1. The Lucky Charm (Revive on Death)     — 20 Coins")
        print("🛡️  2. Smoke Shield (Absorbs 1 Wrong Guess)  — 25 Coins")
        print("🧪 3. Heart Container (+2 Extra Lives)      — 30 Coins")
        print("🥷  4. Smoke Bomb (First 2 Misses are Free)  — 40 Coins")
        print("❌ 5. Skip Shop (Start Game)")

        # Player enters his purchase
        shop_decision = input("\t=> ").lower()

        for i in range (len(shop)):
            if shop_decision in shop[i]["name"]:
                if player_coin >= shop[i]["cost"]:
                    player_coin      -= shop[i]["cost"]
                    shop[i]["active"] = True
                    print(f"{shop[i]["name"][0]} purchased successfully!")
                    break
#   === IF PLAYER'S BALANCE ISN'T ENOUGH TO PURCHASE THE ITEM ===
                else:
                    print("❌ Insufficient coins!")

    # Variables out of the dictionary data for easier gameplay loop usage
    smoke_bomb_charges = 0
    has_lucky_charm = shop[0]["active"]
    has_shield      = shop[1]["active"]
    has_smoke_bomb  = shop[3]["active"]

    if has_smoke_bomb == True:
        smoke_bomb_charges = 2    
        has_smoke_bomb = False    

    # Adding the hearts if they purchased The Heart Container
    if shop[2]["active"] == True:
        active_max_lives += shop[2]["bonus"]

#   === GENERATING THE RANDOM NUMBER AND INITIALIZING THE ATTEMPT VARIABLE TO 1
    random_number = random.randint(1, active_max_range)
    attempts = 1

    print(f"\n{active_color}Mode: {mode_name} | Range: 1–{active_max_range}\nLives: {"❤️ " * active_max_lives}{RESET}\n")
            
    while attempts <= active_max_lives:
        try:
            entered_guess = int(input(f"🤔 [Attempt {attempts}/{active_max_lives}] Enter a number between 1 and {active_max_range} 🤔 \n\t=> "))

            numbers_difference = abs(entered_guess - random_number)      

            #IF THE NUMBER IS ABOVE THE LEVEL RANGE
            if entered_guess < 1 or entered_guess > active_max_range:
                print(f"❌ The entered number is not with the level range. Please type only digits between 1 and {active_max_range}.")
                print(f"Lives remaining: {"❤️ " * (active_max_lives - (attempts - 1))}\n")
            else:
                # IF THE NUMBER GUESSED IS CORRECT 
                if entered_guess == random_number:
                    print(f"{GOLD}CONGRATS! You found the secret number! 🏆{RESET}\n")
                    player_coin += coin_reward
                    current_profile["wins"] += 1
                    break
                else:
                    # IF THE NUMBER GUESSED IS CLOSE TO THE ANSWER 
                    if numbers_difference <= near_miss_threshold:
                        print(f"💥 {RED}CRITICAL NEAR MISS!{RESET} 💥")    

                    # IF THE NUMBER GUESSES IS TOO HIGH OR TOO LOW
                    if entered_guess < random_number:
                        print(f"{YELLOW}📉 Too low! 📉{RESET}")
                    elif entered_guess > random_number:
                        print(f"{CYAN}📈 Too high! 📈{RESET}")


            #   SHOW THE NUMBER OF REMAINING LIVES. 
                # If the player has the Smoke Bomb Charge
                if smoke_bomb_charges > 0:
                    smoke_bomb_charges -= 1
                    print(f"\n\t🥷 {CYAN}The Smoke Bomb cloud absorbed the blow! {smoke_bomb_charges} smoke charges remaining.{RESET}")
                    print(f"Remaining lives: {"❤️ " * active_max_lives}\n")
                # If the player has a shield 
                elif has_shield == True:
                    print(f"\n\t{GREEN}The shield broke, you don't lose a life in this round{RESET}.")
                    print(f"Remaining lives: {"❤️ "*(active_max_lives)}\n")
                    has_shield = False
                else:
                    print(f"Remaining lives: {"❤️ "*(active_max_lives - attempts)}\n")
                    attempts += 1

        #IF THE INPUT WAS NOT A VALID NUMBER
        except ValueError:
            print("❌ That is not a valid number. Please type digits only (like 5)!")
            print(f"Lives remaining: {"❤️ " * (active_max_lives - (attempts - 1))}\n")                

    # ===== GAME OVER =====
        if attempts > active_max_lives: 
            if has_lucky_charm == True:
                print(f"\n{ORANGE}🍀 Your Lucky Charm shatters! You are brought back to life for one final guess! 🍀{RESET}")
                has_lucky_charm = False
                attempts = active_max_lives
            else:
                print("💔 No more lives 💔... Game Over.🪦\n\n")

    current_profile["total attempts"] += 1
    # IF THE PLAYER WANTS TO QUIT THE GAME
    if input("Would you like to quit the game?\n\t=> ").lower() == "yes":
        player_left = True
        print("\nPlayer has left...📴\n")
        quit()

