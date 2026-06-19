from types import SimpleNamespace

from logic_utils import (
    check_guess,
    format_attempts_status,
    get_attempt_limit_for_difficulty,
    get_range_for_difficulty,
    reset_game_state,
)

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result, message = check_guess(50, 50)
    assert result == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    # I used the AI's suggestion to assert the message text here, not just the outcome label.
    result, message = check_guess(60, 50)
    assert result == "Too High"
    assert message == "📈 Go Lower!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    # I kept the AI-driven regression check so the lower-hint text stays covered too.
    result, message = check_guess(40, 50)
    assert result == "Too Low"
    assert message == "📉 Go Higher!"


def test_check_guess_behaves_like_a_string():
    # I added this with the AI so the shared helper keeps working for both direct string checks and tuple unpacking.
    result = check_guess(60, 50)
    assert result == "Too High"
    assert str(result) == "Too High"


def test_difficulty_settings_scale_range_and_attempts():
    #FIX: Added this coverage with AI help so Easy stays smaller and Hard stays larger with fewer attempts.
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_attempt_limit_for_difficulty("Easy") == 10
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_attempt_limit_for_difficulty("Normal") == 8
    assert get_range_for_difficulty("Hard") == (1, 200)
    assert get_attempt_limit_for_difficulty("Hard") == 5


def test_unknown_difficulty_uses_normal_defaults():
    assert get_range_for_difficulty("Unknown") == (1, 100)
    assert get_attempt_limit_for_difficulty("Unknown") == 8


def test_attempts_status_uses_active_range():
    assert format_attempts_status(1, 200, 5) == (
        "Guess a number between 1 and 200. Attempts left: 5"
    )


def test_reset_game_state_clears_round_fields():
    # I added this with the AI to pin down the shared reset behavior used by New Game.
    state = SimpleNamespace(
        attempts=4,
        history=[1, 2, 3],
        score=25,
        status="lost",
        secret=99,
    )

    reset_game_state(state, 1, 100, secret_factory=lambda low, high: 42)

    assert state.attempts == 0
    assert state.history == []
    assert state.score == 0
    assert state.status == "playing"
    assert state.secret == 42
