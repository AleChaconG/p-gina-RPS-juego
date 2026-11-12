VALID_MOVES = ("rock", "paper", "scissors")

BEATS = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}


def determine_winner(player_move: str, computer_move: str) -> str:
    """Return "player", "computer", or "tie" for one Rock, Paper, Scissors round.

    Raise ValueError if either move is not "rock", "paper", or "scissors".
    """
    if player_move not in VALID_MOVES:
        raise ValueError(f"Invalid player move: {player_move!r}")
    if computer_move not in VALID_MOVES:
        raise ValueError(f"Invalid computer move: {computer_move!r}")

    if player_move == computer_move:
        return "tie"
    if BEATS[player_move] == computer_move:
        return "player"
    return "computer"
