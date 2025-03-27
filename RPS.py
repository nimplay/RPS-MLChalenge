# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    if not prev_play:
        opponent_history.clear()
    else:
        opponent_history.append(prev_play)

    # Quincy
    if len(opponent_history) >= 6:
        last_six = "".join(opponent_history[-6:])
        if last_six in ["RRPPSS", "RPPSSR", "PPSSRR", "PSSRRP", "SSRRPP", "SRRPPS"]:
            quincy_cycle = ['R', 'R', 'P', 'P', 'S', 'S']
            next_move = quincy_cycle[len(opponent_history) % 6]
            return {'R': 'P', 'P': 'S', 'S': 'R'}[next_move]

    # Kris
    if len(opponent_history) >= 1:
        if len(opponent_history) >= 2 and opponent_history[-1] == {'R': 'P', 'P': 'S', 'S': 'R'}.get(opponent_history[-2], 'R'):
            return opponent_history[-2]

    #  Mrugesh
    if len(opponent_history) % 3 == 0:
        guess = 'R'
    elif len(opponent_history) % 3 == 1:
        guess = 'P'
    else:
        guess = 'S'

    #  Abbey
    if len(opponent_history) >= 4:
        last_plays = opponent_history[-4:]
        most_frequent = max(set(last_plays), key=last_plays.count)
        if most_frequent == 'R':
            guess = 'P'
        elif most_frequent == 'P':
            guess = 'S'
        else:
            guess = 'R'

    return guess
