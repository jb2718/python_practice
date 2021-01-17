def print_roster(players):
    if len(players) == 1:
        print("There is 1 player on the team")
    else:
        print("There are {} players on the team".format(len(players)))
    
    for index, player in enumerate(players):
        print("Player #{}:".format(index + 1), player)
        
players = []
is_add = input('Would you like to add players to the team? Yes/No:  ')

while is_add.lower() == 'yes':
    player_name = input("What is the player's name?: ")
    players.append(player_name)
    is_add = input('Would you like to add players to the team? Yes/No:  ')

print_roster(players)

goalkeeper_num = int(input('Choose a player for the goalie. Enter their number: '))
print("The goalkeeper is {}".format(players[goalkeeper_num - 1]))

