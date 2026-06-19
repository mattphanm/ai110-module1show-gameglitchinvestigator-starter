import streamlit as st

from logic_utils import (
    check_guess,
    format_attempts_status,
    get_attempt_limit_for_difficulty,
    get_range_for_difficulty,
    parse_guess,
    reset_game_state,
    update_score,
)

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

#FIX: Shared the difficulty setup with logic_utils using AI help so each mode gets the right range and attempts.
low, high = get_range_for_difficulty(difficulty)
attempt_limit = get_attempt_limit_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

# AI helped identify that reruns were preserving stale state, so I initialize the first round once here.
if "secret" not in st.session_state:
    # I followed the AI's Streamlit-state guidance here so the first round survives reruns.
    reset_game_state(st.session_state, low, high)

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

st.subheader("Make a guess")

#FIX: Used AI guidance to keep the layout while refreshing the attempts text after submit.
attempts_status = st.empty()
attempts_status.info(
    format_attempts_status(low, high, attempt_limit - st.session_state.attempts)
)

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    debug_attempts = st.empty()
    debug_attempts.write(f"Attempts: {st.session_state.attempts}")
    debug_score = st.empty()
    debug_score.write(f"Score: {st.session_state.score}")
    st.write("Difficulty:", difficulty)
    debug_history = st.empty()
    debug_history.write(f"History: {st.session_state.history}")

raw_guess = st.text_input(
    "Enter your guess:",
    key=f"guess_input_{difficulty}"
)

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

if new_game:
    # I applied the AI's reset-state suggestion here so New Game clears the entire round cleanly.
    reset_game_state(st.session_state, low, high)
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

if submit:
    st.session_state.attempts += 1

    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        st.session_state.history.append(raw_guess)
        st.error(err)
    else:
        st.session_state.history.append(guess_int)

        # I kept the AI-aligned shared helper path so the app and tests use the same comparison logic.
        outcome, message = check_guess(guess_int, st.session_state.secret)

        if show_hint:
            st.warning(message)

        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )

        if outcome == "Win":
            st.balloons()
            st.session_state.status = "won"
            st.success(
                f"You won! The secret was {st.session_state.secret}. "
                f"Final score: {st.session_state.score}"
            )
        else:
            if st.session_state.attempts >= attempt_limit:
                st.session_state.status = "lost"
                st.error(
                    f"Out of attempts! "
                    f"The secret was {st.session_state.secret}. "
                    f"Score: {st.session_state.score}"
                )

    #FIX: Re-rendered the existing placeholders with AI help so first submit shows the new attempt count.
    attempts_status.info(
        format_attempts_status(low, high, attempt_limit - st.session_state.attempts)
    )
    debug_attempts.write(f"Attempts: {st.session_state.attempts}")
    debug_score.write(f"Score: {st.session_state.score}")
    debug_history.write(f"History: {st.session_state.history}")

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")
