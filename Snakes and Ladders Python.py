import random
dice_images = [
    """
        ---
       |   |
       | o |
       |   |
        ---
    """,
    """
        ---
       |   |
       |o o|
       |   |
        ---
    """,
    """
        ---
       |   |
       |ooo|
       |   |
        ---
    """,
    """
        ---
       |o o|
       |   |
       |o o|
        ---
    """,
    """
        ---
       |o o|
       | o |
       |o o|
        ---
    """,
    """
        ---
       |ooo|
       |   |
       |ooo|
        ---
    """
    
]
ladders = {1: 38, 4: 14, 8: 10, 21: 42, 28: 76, 50: 57, 71: 92, 80: 99}
snakes = {97: 78, 95: 56, 88: 24, 62: 18, 48: 26, 36: 6, 32: 10}

print('Welcome To Snakes And Ladders!')
print('Player 1 will start the game')

Game = True

pos1 = 0
pos2 = 0

while Game == True:
    roll1 = input('Player 1 Press enter to roll dice: ')
    
    if roll1 == '': #if player 1 presses only the enter key
        num1 = random.randint(1,6) #roll the dice
        print('Rolling dice...')
        print('Its a ' + str(num1))
        print(dice_images[num1-1]) #picture index is 1 less than dice value

        if pos1+num1 > 100:
            pos1 = pos1 #if it will go goes over 100, do not increase the value
        else:
            pos1 += num1 

        for a in ladders:
            if pos1 == a:
                print('Player 1 climbed the ladder from ' + str(pos1) + ' to ' + str(ladders[a]))
                pos1 = ladders[a] 
        for b in snakes:
            if pos1 == b:
                print('Player 1 fell down a snake from ' + str(pos1) + ' to ' + str(snakes[b]))
                pos1 = snakes[b]
        print('Player1, your current position is : ' + str(pos1))

    roll2 = input('Player 2 Press enter to roll dice: ')
    
    if roll2 == '': #if player 1 presses only the enter key
        num2 = random.randint(1,6) #roll the dice
        print('Rolling dice...')
        print('Its a ' + str(num2))
        print(dice_images[num2-1]) #picture index is 1 less than dice value

        if pos2+num2 > 100:
            pos2 = pos2 #if it will go goes over 100, do not increase the value
        else:
            pos2 += num2 

        for i in ladders:
            if pos2 == i:
                print('Player 2 climbed the ladder from ' + str(pos2) + ' to ' + str(ladders[i]))
                pos2 = ladders[i]
        for x in snakes:
            if pos2 == x:
                print('Player 2 fell down a snake from ' + str(pos2) + ' to ' + str(snakes[x]))
                pos2 = snakes[x]
        print('Player2, your current position is : ' + str(pos2))
            
    if pos1 == 100:
        Game = False
        print('CONGRATULATIONS PLAYER1, YOU ARE THE WINNER!')
    if pos2 == 100:
        Game = False
        print('CONGRATULATIONS PLAYER2, YOU ARE THE WINNER!')














    
