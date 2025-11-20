
#Run this code to start your shift. You don't need run the code again if you want to keep playing.
import random
import time
import os

game_running = True

def clear_screen():
    """Clears the terminal screen."""
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux (os.name is 'posix')
    else:
        _ = os.system('clear')

password_check = True

while password_check == True:
  password = input("Enter your password: ")
  print("Processing...")
  if password == "EPDMAN290":
    time.sleep(5.0)
    print("Welcome Manager")
    epd_num = 0 #counts the number of expedition
    password_check = False
  else:
    time.sleep(3.0)
    print("wrong password try again")

time.sleep(4.0)
clear_screen()

while game_running == True:

    hp = 0
    atk = 0
    defense = 0
    statsToken = 20.0
    selection_state = True
    nam_stats_list = ['Health', 'Attack', 'Defense']

    enemy_defeated = 0
    dungeons_cleared = 0
    ene_stats = [100.0, 5.0, 2.0]
    game_state = True


    retry_quit_choice = True

    print("Please distribute your ", statsToken," stat points into the following: DEX, STR and AGI")
    def stats(Dexterity = 0,Strength = 0,Agility = 0):
        return [20*( 2*Dexterity + 0.5*Strength ), 2*( 2*Strength + 0.5*Agility ),  (2*Agility + 0.5*Dexterity)]

    while selection_state == True:

        DEX = 0
        STR = 0
        AGI = 0

        try:
            DEX += float(input("DEX: "))
            STR += float(input("STR: "))
            AGI += float(input("AGI: "))

            if DEX + STR + AGI == statsToken:
                player_stats = stats(float(DEX),float(STR),float(AGI))

                statsToken = 0

                hp += player_stats[0]
                atk += player_stats[1]
                defense += player_stats[2]

                stats_list = [hp, atk, defense]

                print("Health: ",hp," Attack Power: ", atk," Defense:", defense)
                selection_state = False

            else:
                print("Number does not add up to 20, try again.")
        except ValueError:
            print("Invalid response. Please try again.")
    
    time.sleep(5.0)
    clear_screen()

    while game_state == True:

        copy_ene_stats = ene_stats.copy() #Stat inflation
        player_action = input("Choose your strategy: Aggressive, Passive or Flexible? ") #Reset
        play_def_count = 0
        ene_def_count = 0
        play_atk_count = 0
        ene_atk_count = 0

        play_staggercheck = False #Checking for stagger
        ene_staggercheck = False

        while copy_ene_stats[0] > 0: #Player's Turn
            auto_choice = ['attack', 'defend']
            if player_action.lower() == 'aggressive':
                probability = [2, 1]
            elif player_action.lower() == 'passive':
                probability = [1, 2]
            else:
                probability = [1, 1]
            automated_player_action = random.choices(auto_choice,probability,k=1)[0]
            time.sleep(3.0)


            if play_staggercheck == True: #Stagger mechanics
                print("You are staggered")
                play_def_count = 0
                play_staggercheck = False
            else:
                print("The player", automated_player_action)
                if automated_player_action == 'attack': #If Def then Atk, then counter (deals 2x atk)
                    if play_atk_count >= 2: #Exhaustion mechanics. Repeated below same for enemy.
                        print("You have been exhausted")
                        play_atk_count = 0
                    else:
                        if play_def_count == 0:
                            pla_atk = copy_ene_stats[0] - stats_list[1]
                            copy_ene_stats[0] = pla_atk
                            if ene_def_count == 2:
                                ene_staggercheck = True
                                print("Enemy is staggered")
                            print("Enemy's HP remaining: ",copy_ene_stats[0])
                            play_atk_count += 1
                        elif play_def_count == 1:
                            print("How you like that?")
                            pl_counter_atk = stats_list[1]*2
                            pl_counter_results = copy_ene_stats[0] - pl_counter_atk
                            copy_ene_stats[0] = pl_counter_results
                            play_def_count = 0
                            if ene_def_count == 2:
                                ene_staggercheck = True
                                print("Enemy is staggered")
                            print("Enemy's HP remaining: ",copy_ene_stats[0])
                            play_atk_count += 1
                        elif play_def_count == 2:
                            print("TAKE THIS!!")
                            pl_cha_atk = stats_list[1]*3
                            pl_charge_results = copy_ene_stats[0] - pl_cha_atk
                            copy_ene_stats[0] = pl_charge_results
                            play_def_count = 0
                            if ene_def_count == 2:
                                ene_staggercheck = True
                                print("Enemy is staggered")
                            print("Enemy's HP remaining: ",copy_ene_stats[0])
                            play_atk_count += 1


                elif automated_player_action == 'defend': #Heal ---> Charge ---> Charged Attack (deals 3x atk) for consecutive defend commands
                    play_atk_count = 0
                    if play_def_count == 0:
                        pla_def = stats_list[0] + stats_list[2]
                        stats_list[0] = pla_def
                        print("Player's HP: ",stats_list[0])
                        play_def_count += 1
                    elif play_def_count == 1:
                        print("Charging a big one")
                        play_def_count += 1
                    elif play_def_count == 2:
                        print("TAKE THIS!!")
                        pl_cha_atk = stats_list[1]*3
                        pl_charge_results = copy_ene_stats[0] - pl_cha_atk
                        copy_ene_stats[0] = pl_charge_results
                        play_def_count = 0
                        if ene_def_count == 2:
                            ene_staggercheck = True
                            print("Enemy is staggered")
                    print("Enemy's HP remaining: ",copy_ene_stats[0])
            if copy_ene_stats[0] <= 0:
                break


            if ene_staggercheck == True:
                print("Enemy has been knocked, now is your chance!!")
                ene_def_count = 0
                ene_staggercheck = False
            else:
                print("The enemy is making their decision...") #Suspension (scary)
                enemy_action = random.choice(['attack','defend'])
                time.sleep(3.0)
                print("The enemy", enemy_action)
                if enemy_action == 'attack': #Enemy's Turn #Same here
                    if ene_atk_count >= 2:
                        print("Enemy is exhausted, now is our chance.")
                        ene_atk_count = 0
                    else:
                        if ene_def_count == 0:
                            ene_atk = stats_list[0] - copy_ene_stats[1]
                            stats_list[0] = ene_atk
                            if play_def_count == 2:
                                play_staggercheck = True
                                print("You have been staggered")
                            print("Player's Remaining HP: ",stats_list[0])
                            ene_atk_count += 1
                        elif ene_def_count == 1:
                            print("You have been countered")
                            ene_counter = copy_ene_stats[1]*2
                            ene_counter_results = stats_list[0] - ene_counter
                            stats_list[0] = ene_counter_results
                            ene_def_count = 0
                            if play_def_count == 2:
                                play_staggercheck = True
                                print("You have been staggered")
                            print("Player's Remaining HP: ",stats_list[0])
                            ene_atk_count += 1
                        elif ene_def_count == 2:
                            print("Enemy released a charged attack")
                            ene_charge_atk = copy_ene_stats[1]*3
                            ene_charge_results = stats_list[0] - ene_charge_atk
                            stats_list[0] = ene_charge_results
                            ene_def_count = 0
                            if play_def_count == 2:
                                play_staggercheck = True
                                print("You have been staggered")
                            print("Player's Remaining HP: ",stats_list[0])
                            ene_atk_count += 1

                elif enemy_action == 'defend':
                    ene_atk_count = 0
                    if ene_def_count == 0:
                        ene_def = copy_ene_stats[0] + copy_ene_stats[2]
                        copy_ene_stats[0] = ene_def
                        print("Enemy's HP: ",copy_ene_stats[0])
                        ene_def_count += 1
                    elif ene_def_count == 1:
                        print("Enemy is charging")
                        ene_def_count += 1
                    elif ene_def_count == 2:
                        ene_charge_atk = copy_ene_stats[1]*3
                        ene_charge_results = stats_list[0] - ene_charge_atk
                        stats_list[0] = ene_charge_results
                        ene_def_count = 0
                        print("Enemy released a charged attack")
                        if play_def_count == 2:
                            play_staggercheck = True
                            print("You have been staggered")
                        print("Player's Remaining HP: ",stats_list[0])
            if stats_list[0] <= 0:
                break


        if stats_list[0] <= 0:
            print("Game Over") #well done
            game_state = False
        else:
            enemy_defeated += 1
            print("you won the fight! Time to upgrade...")
            print("Type 0 for Hp, type 1 for Atk, type 2 for Def")
            time.sleep(3.0)
            up_st_lts = int(input("Choose which stat to upgrade: ")) #Player stat Upgrade
            num_st_up = random.choice(range(21))
            stats_list[up_st_lts] += num_st_up
            print(nam_stats_list[up_st_lts], "has been upgraded by",num_st_up,"to",stats_list[up_st_lts])
            print("Player's HP: ",stats_list[0],"ATK: ",stats_list[1],"DEF: ",stats_list[2])

            time.sleep(3.0)
            ene_up_st_lts = random.choice(range(3)) #Enemy stat inflation
            ene_num_st_up = random.choice(range(46))

            ene_stats[ene_up_st_lts] += ene_num_st_up
            print(nam_stats_list[ene_up_st_lts], "has been upgraded by",ene_num_st_up,"to",ene_stats[ene_up_st_lts])
            print("Next enemy's HP:",ene_stats[0]," ATK:",ene_stats[1]," DEF:",ene_stats[2])

        input("Press Enter to continue...") #Ready when you are :)

        clear_screen()

    dungeons_cleared += enemy_defeated/10
    epd_num += 1
    print("Loading results...") # Loading.... loading... loading...
    time.sleep(5.0)
    print("You have defeated ",enemy_defeated," and cleared ",dungeons_cleared," levels") # Nice stats bro.

    name_Player = input("Player's Name: ") #Congrats on your expedition
    time_now = time.ctime()
    print("Expedition #", epd_num, time_now) #Real time basis. Imagine exploring at night. :O
    print("----------------------------------------------------------------------------------")
    time.sleep(4.0)
    print("DEX:",DEX," STR:",STR," AGI:",AGI)
    print("----------------------------------------------------------------------------------")
    time.sleep(6.0)
    print(name_Player,"has defeated ",enemy_defeated," and cleared ",dungeons_cleared," levels of the infinite dungeon. May they find peace.")
    time.sleep(3.0)
    print("----------------------------------------------------------------------------------")
    print("Sending to database...")
    time.sleep(10.0)
    print("----------------------------------------------------------------------------------")
    print("SENT. GOOD JOB MANAGER.") # :D
    print("----------------------------------------------------------------------------------")
    time.sleep(2.0)

    while retry_quit_choice == True:
        retry_quit = input("To continue the shift, please type Y or N: ")
        if retry_quit.capitalize()== "Y":
            print("Here we go again")
            retry_quit_choice = False
            time.sleep(3.0)
            clear_screen()
        elif retry_quit.capitalize() == "N":
            print("Closing EXPLORMAN.exe now...")
            game_running = False
            retry_quit_choice = False
            time.sleep(3.0)
        else:
            print("Invalid choice, try again")
            
input("Press Enter to close the game.")
print("Thanks for playing!")
time.sleep(6.0)