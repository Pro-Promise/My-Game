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
    print('''       _._._._    ^  _._._._       _._._._ ^
       | ___ |_._._._| ___ |_._._._| ___ |
       | |_| |  ___  | |_| |  ___  | |_| |
       |_III_|  |_|  |_III_|  |_|  |_III_| ^!^
 ^     | ___ |__III__| ___ |__III__| ___ |
    ^  | |_| |  ___  | |_| |  ___  | |_| |   ^!^
       |_III_|  |_|  |_III_|  |_|  |_III_|
       | ___ |__III__| ___ |__III__| ___ | _)o(_
       | |_| |  ___  | |_| |  ___  | |_| | /(|)\
   /)  |_III_|  |_|  |_III_|  |_|  |_III_|   H
 _/ )  | ___ |__III__|_____|__III__| ___ |   H
 ~^~^~ | |_| |"""""""||~|~||"""""""| |_| |   H
    ^~'|_III_|@@@@@@@||_|_||@@@@@@@|_III_|^~^H '
 @@@@@@@@@@@@@@     @/=====\@     @@@@@@@@@@@@@@''')
    print("""You are in front of Zhanyi's inn
             Would you like to move forwards or backwards? (f/b)""")
    direction = input().lower
    if direction == "f":
      print("""You walked into the inn, and there is an elf who looks worried. 
             You walk towards the elf.""")
      print("""The merchant elf named Gery seeks a company of adventurers to protect him from the assassins of the Devil of the Nightfall Jungle. - reward 1000g""")
        
      print("Would you like to do this quest? (y/n")
      quest = input().lower
      if quest == "y":
         weapons = ["A) stonehammer", "B) Giantspear"]
         print("He gives you the option of 2 weapons:")
      for weapon in weapons:
       print(weapon)

       print("Please choose an option: (A/B)")






















else:
    print('''
              _|_
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
~^^"  ^"  ~^^/   \^^~  "^  "^^~''')


