import random

def roll():
    min_value= 1
    max_value= 6
    roll=random.randint(min_value, max_value)
    
    return roll 


while True:
    players = input("enter the number of player(2- 4): ")
    if players.isdigit():
        players=int(players)
        #isdigit is to check if the input is with limits only of 1-4 
        #int(player) is to convert the string of the player to int
        #its done to check if the limits are being followed 
        if 2 <= players <= 4:
            break
        else:
            print("player number between 2- 4")

    else:
        print("invalid try again :)")

#print(players)     #to display the results 

#to stimulate dice rolls 
max_score=50
player_scores=[0 for _ in range(players)]

while max(player_scores)< max_score:
      for player_idx in range(players):
        print("\nPlayer number",player_idx +1, "turn has started!")
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score=0
        while True:
            should_roll=input("would you like to roll (y)?")
            if should_roll.lower() != "y":
                break
            value=roll()
            if value==1:
                print("you rolled a 1! turn done")
                current_score=0
                break
            else:
                current_score += value
                print("you rolled a:",value)
                #debuggin done ,while loop to be placed inside 
                print("your score is:",current_score)
                player_scores[player_idx] += current_score
                print("yout total score is :", player_scores[player_idx])

max_score=max(player_scores)
winning_idx=player_scores.index(max_score)
print("player number",winning_idx+1,
      "is the winner with a score of :",max_score)




