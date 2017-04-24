

player_one = raw_input("Rock, Paper, or Scissors?").upper()
player_two = raw_input("Rock, Paper, or Scissors?").upper()

def gametime(p1, p2):
    if p1 == p2:
        return("It's a tie!")
    elif p1 == 'rock':
        if p2 == 'scissors':
        	return("Rock wins!")
        else:
            return("Paper wins!")
	elif p1 == 'paper':
        if p2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")

    elif p1 == 'scissors':
        if p2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")

    else:
        return("You typed the wrong thing you Doofus!")
        

print(gametime(player_one, player_two)

	

	