from collections import deque

def playMarbleGame(n_players, last_marble):
    n_marbles = last_marble + 1

    circle = deque([0]) # current marble is always at left end
    player_scores = [0 for i in range(0, n_players)] # player with index 0 is player No. 464

    current_player = 0

    for marble in range(1, n_marbles):
        current_player = (current_player + 1) % n_players
        
        if marble % 23 == 0:
            player_scores[current_player] += marble
            circle.rotate(7)
            player_scores[current_player] += circle.popleft()
            
        else:
            circle.rotate(-2)    
            circle.appendleft(marble)        

    return circle, player_scores

# TASK 1: 464 players, keep going until marble 70918
circle, player_scores = playMarbleGame(464, 70918)
print(max(player_scores))

# TASK 2: 464 players, keep going until marble 7091800
circle, player_scores = playMarbleGame(464, 7091800)
print(max(player_scores))
