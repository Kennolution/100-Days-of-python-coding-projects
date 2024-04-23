print('Welcome to Wilderness Survival: A journey into the unknown.')

bravery = input('Do you have what it takes to survive in the wild? ')
if bravery == 'yes':
    biome = input('Choose one biome between "caves", "forest", "lake"- ')
    if biome == 'lake':
        swim = input('Can you swim? ')
        if swim == 'yes':
            speed = float(input('How fast are you moving? '))
            if speed >= 5:
                print('You Win!!!. You got to the finish line before the sharks. Grab your Gols treasure reward.')
            else:
                print("Game Over. The sharks are already starting to block the finish line. You won't survive when you get there")
        else:
            print("Game Over.\nYou won't survive")
    elif biome == 'forest':
        x = input('Are you turning left or right on the T_Junction? ')
        if x == 'right':
            print('Congratulations!. You have survived the wilderness.')
        elif x == 'left':
            print('Craft some weopons. You have put yourself in danger. Good luck')
        else:
            print(f'Game Over. You chose {x} instead of left/right')
    elif biome == 'caves':
        cave = input('salt/dark? ')
        if cave == 'salt':
            print('Congratulations!.\nYou have won milk, honey and diamonds.')
        elif cave == 'dark':
            print('Game Over. You have entered the wolfs territory.')
        else:
            print(f'Game Over. You chose {y} instead of salt/dark.')
    else:
        print('Incorrect option. Exiting the game.')
else:
    print('''Go Home. You won't be allowed to play with this option.''')