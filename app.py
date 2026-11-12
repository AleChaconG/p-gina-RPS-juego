import random

import streamlit as st

from game import VALID_MOVES, determine_winner

st.set_page_config(page_title="Rock, Paper, Scissors")

st.session_state.setdefault("player_wins", 0)
st.session_state.setdefault("computer_wins", 0)
st.session_state.setdefault("ties", 0)
st.session_state.setdefault("last_player_move", None)
st.session_state.setdefault("last_computer_move", None)
st.session_state.setdefault("last_result", None)


def play_round(player_move: str) -> None:
    computer_move = random.choice(VALID_MOVES)
    result = determine_winner(player_move, computer_move)

    st.session_state.last_player_move = player_move
    st.session_state.last_computer_move = computer_move
    st.session_state.last_result = result

    if result == "player":
        st.session_state.player_wins += 1
    elif result == "computer":
        st.session_state.computer_wins += 1
    else:
        st.session_state.ties += 1


st.title("Rock, paper, scissors")
st.caption("Unlimited rounds. Scores reset when you reload the page.")

st.subheader("Scoreboard")
player_col, computer_col, ties_col = st.columns(3)
player_col.metric("Player wins", st.session_state.player_wins, border=True)
computer_col.metric("Computer wins", st.session_state.computer_wins, border=True)
ties_col.metric("Ties", st.session_state.ties, border=True)

st.subheader("Make your move")
rock_col, paper_col, scissors_col = st.columns(3)
rock_col.button(
    "Rock",
    icon=":material/landscape:",
    width="stretch",
    on_click=play_round,
    args=("rock",),
)
paper_col.button(
    "Paper",
    icon=":material/description:",
    width="stretch",
    on_click=play_round,
    args=("paper",),
)
scissors_col.button(
    "Scissors",
    icon=":material/content_cut:",
    width="stretch",
    on_click=play_round,
    args=("scissors",),
)

if st.session_state.last_result is None:
    st.info("Choose rock, paper, or scissors to start.")
else:
    st.write(
        f"You chose **{st.session_state.last_player_move}**. "
        f"The computer chose **{st.session_state.last_computer_move}**."
    )
    if st.session_state.last_result == "player":
        st.success("You win this round.")
    elif st.session_state.last_result == "computer":
        st.error("The computer wins this round.")
    else:
        st.info("This round is a tie.")
