from time import sleep
import random
lives = ""
reward = ""


print("""
         (o o)              (o o) 
        (  V  ) Welcome To (  V  )
        --m-m----------------m-m--""")

sleep(2)

print("""     █████ ██                                                                    
   ██████  ████ █                          █                                      
  ██   █  █  ███                          ██                                      
 █    █  █    █                           ██                                      
     █  █                               ████████             ████   ██   ████     
    ██ ██           ████   ███  ████   ████████    ████     █ ████ █ ██    ███  █ 
    ██ ██          █ ███  █ ████ ████ █   ██      █ ███  █ ██  ████  ██     ████  
    ██ ██████     █   ████   ██   ████    ██     █   ████ ████       ██      ██   
    ██ █████     ██    ██    ██    ██     ██    ██    ██    ███      ██      ██   
    ██ ██        ██    ██    ██    ██     ██    ██    ██      ███    ██      ██   
    █  ██        ██    ██    ██    ██     ██    ██    ██        ███  ██      ██   
       █         ██    ██    ██    ██     ██    ██    ██   ████  ██  ██      ██   
   █████         ██    ██    ██    ██     ██    ██    ██  █ ████ █    █████████   
  █  █████        █████ ██   ███   ███     ██    █████ ██    ████       ████ ███  
 █    ███          ███   ██   ███   ███           ███   ██                    ███ 
 █                                                                     █████   ███
  █                                                                  ████████  ██ 
   █                                                                █      ████   
    ██                                                                            
""")

Filename = "scores.txt"
myFile = open(Filename, "a")

print("Please enter a username")
username = input()
myFile.write(f"{username}\n")

print(f"Welcome {username} to Fantasy!")


creatures = ["Wolf", "Dragon", "Wizard", "Giant", "Vampire", "Human"]

print("Please choose your creature from the list:")
print("- " + "\n- ".join(creatures))


chosen_creature = input("Enter your creature: ").capitalize()
while chosen_creature not in creatures:
    print("Please input a creature from the given list.")
    chosen_creature = input("Enter your creature: ").capitalize()

if chosen_creature == "Wolf":
    lives = 5
elif chosen_creature == "Dragon":
    lives = 7
elif chosen_creature == "Wizard":
    lives = 6
elif chosen_creature == "Giant":
    lives = 5
elif chosen_creature == "Vampire":
    lives = 8
else:
    lives = 3

print(f"You have {lives} lives")


print(f"You have chosen to be a {chosen_creature}!")

print("You will spawn in...")
for i in range(3, 0, -1):
    print(i)
    sleep(1)
print("0")

print("Welcome to Zhanyi!")
print(f"~You have {lives} lives and {reward} gold~")
print("""                                     +              #####
                                   / \
 _____        _____     __________/ o \/\_________      _________
|o o o|_______|    |___|               | | # # #  |____|o o o o  | /\
|o o o|  * * *|: ::|. .|               |o| # # #  |. . |o o o o  |//\\
|o o o|* * *  |::  |. .| []  []  []  []|o| # # #  |. . |o o o o  |((|))
|o o o|**  ** |:  :|. .| []  []  []    |o| # # #  |. . |o o o o  |((|))
|_[]__|__[]___|_||_|__<|____________;;_|_|___/\___|_.|_|____[]___|  |""")

print("""                                       ▄▄           
▀████▀                               ▀███           
  ██                                   ██      ▄▄▄  
  ██       ▄▄█▀██▀██▀   ▀██▀  ▄▄█▀██   ██     ▀███  
  ██      ▄█▀   ██ ██   ▄█   ▄█▀   ██  ██       ██  
  ██     ▄██▀▀▀▀▀▀  ██ ▄█    ██▀▀▀▀▀▀  ██       ██  
  ██    ▄███▄    ▄   ███     ██▄    ▄  ██       ██  
██████████ ▀█████▀    █       ▀█████▀▄████▄   ▄████▄
                                                    
                                                    
""")
print("""                                     +              #####
                                   / \'
 _____        _____     __________/ o \/\_________      _________
|o o o|_______|    |___|               | | # # #  |____|o o o o  | /\'
|o o o|  * * *|: ::|. .|               |o| # # #  |. . |o o o o  |//\\
|o o o|* * *  |::  |. .| []  []  []  []|o| # # #  |. . |o o o o  |((|))
|o o o|**  ** |:  :|. .| []  []  []    |o| # # #  |. . |o o o o  |((|))
|_[]__|__[]___|_||_|__<|____________;;_|_|___/\___|_.|_|____[]___|  |""")

print('''You are in the village of Zhanyi
        Where would you like to go
        A. Zhanyi's Inn
        B. Zhanyi's Town Square''')
level_one = input()
if level_one == "A":
    print('''       _._._._    ^  _._._.__._._ ^
       | ___ |_._._._| ___ |_._._._| ___ |
       | |_| |  ___  | |_| |  ___  | |_| |
       |_III_|  |_|  |_III_|  |_|  |_III_| ^!^
 ^     | ___ |__III__| ___ |__III__| ___ |
    ^  | |_| |  ___  | |_| |  ___  | |_| |   ^!^
       |_III_|  |_|  |_III_|  |_|  |_III_|
       | ___ |__III__| ___ |__III__| ___ | _)o(_
       | |_| |  ___  | |_| |  ___  | |_| |//(|)\\
   /)  |_III_|  |_|  |_III_|  |_|  |_III_|   H
 _/ )  | ___ |__III__|_____|__III__| ___ |   H
 ~^~^~ | |_| |"""""""||~|~||"""""""| |_| |   H
    ^~'|_III_|@@@@@@@||_|_||@@@@@@@|_III_|^~^H '
 @@@@@@@@@@@@@@     @/=====\@     @@@@@@@@@@@@@@''')
    print("""You are in front of Zhanyi's inn""")
    print("Would you like to move forwards or backwards? (f/b)")
direction = input().lower()
if direction == "f":
    print("You walked into the inn, and there is an elf who looks worried. You walk towards the elf.")
    print("The merchant elf named Gery seeks a company of adventurers to protect him from the assassins of the Devil of the Nightfall Jungle. - reward 1000g")

    print("Would you like to do this quest? (y/n)")
    quest = input().lower()
    if quest == "y":
        weapons = ["A) stonehammer", "B) Giantspear"]
        print("He gives you the option of 2 weapons:")
        for weapon in weapons:
            print(weapon)

        print("Please choose an option: (A/B)")
        choice = input().upper()
        if choice in ["A", "B"]:
            if choice == "A": 
                print("You failed to protect Gery. He died and you lost a life and did not get paid.")   
                lives -= 1
                print(f"You have {lives} lives and {reward}g")
            elif choice == "B":
                print("You managed to defeat the assassins and Gery lived, he paid you!")
                reward += 1000
                print(f"You have {lives} lives and {reward}g")
lives = ""
direction = input().lower()
if direction == "b":
    print("You walked to back of Zhanyi's inn")
    print(f"Hello....{username}")
    print("You turned around and you see a strange wizard.""")
    print("He tells you that he needs your help to find the ancient treasure located in Jaga Temple")
print("Would you like to do this quest? (y/n)")
quest = input().lower()

if quest == "y":
    print("Would you like to do this quest? (y/n)")
    quest = input().lower()
    if quest == "y":
        weapons = ["A) Stone Ice Dust", "B) Seeds of Tricks"]
        print("He gives you the option of 2 weapons:")
        for weapon in weapons:
            print(weapon)



    print("""You embark on the adventure!
            You arrived at the Jaga Temple""")
    print("""     .          .            .        .
            UUUUUUUUUUUUUUUUUUUUUUU
       .    UUUUUUUUUUUUUUUUUUUUUUU   .
             |_|_|_|_|_|_|_|_|_|_|
     UUUUUUUU_|_|H|_|_|H|_|_|H|_|_UUUUUUUU ()
  () UUUUUUUU|_|_|_|_|_|_|_|_|_|_|UUUUUUUU(())
 ((() |_\I/_UUUUUUUUUUUUUUUUUUUUUUU_\I/_| ()()
 ())( |_|_|_||_\I/_||_\I/_||_\I/_||_|_|_| ))()
 ((())||H|H|||_|_|_||/_o_\||_|_|_|||H|H||((())
 (()))|_|_|_|||H|H|||=xxx=|||H|H|||_|_|_|(()))
 @@@@@@@@@@@||_|_|_||=xxx=||_|_|_||@@@@@@@@@@@
            @@@@@@@@@|   |@@@@@@@@@""")
    print("Would you like to enter the Temple?")
    enter = input()
    if input == "n":
        print("""You got scared and didn't want to enter the temple
               Then you were pushed into the Temple forced to complete the quest""")
    else: 
        print("You entered the Temple")

    print("""You are now inside the temple, There is 3 doors
            which door would you like to enter - 1,2 or 3""")
    door = input()
    if input == "1":
        print("You entered door 1, inside there is a goblin and he challenges you to a duel!")
        if weapon == "Stone Ice Dust":
            print("""You froze him into stone and won
















if level_one == "B":
    print("""              _|_
                            |
                           )H(
                           |_|
                         _+|_|+_
                     )H( |-|-|-| )H(
                     | |_||H|H||_| |
                     | |-|-|-|-|-| |
               )H(_+_| ||-|-|-|-|| |_+_)H(
               | |-|-| |-|-|-|-|-| |-|-| |
               | ||-|| ||-|-|-|-|| ||-|| |
               | |-|-| |-|-|-|-|-| |-|-| |
               |_||H||_||-|XXX|-||_||H||_|
              ~^^"  ^"  ~^^/   \^^~  "^  "^^~""")
    print("You are in front of Zhanyi's Town Square")

