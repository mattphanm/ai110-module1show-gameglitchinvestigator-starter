from types import SimpleNamespace

from logic_utils import reset_game_state


def build_state():
    return SimpleNamespace(
        attempts=4,
        history=[12, 18, 22],
        score=75,
        status="lost",
        secret=99,
    )


def test_new_game_resets_attempts_to_zero():
    state = build_state()

    reset_game_state(state, 1, 20, secret_factory=lambda low, high: 7)

    assert state.attempts == 0


def test_new_game_clears_history():
    state = build_state()

    reset_game_state(state, 1, 20, secret_factory=lambda low, high: 7)

    assert state.history == []


def test_new_game_resets_score():
    state = build_state()

    reset_game_state(state, 1, 20, secret_factory=lambda low, high: 7)

    assert state.score == 0


def test_new_game_restores_playing_status():
    state = build_state()

    reset_game_state(state, 1, 20, secret_factory=lambda low, high: 7)

    assert state.status == "playing"


def test_new_game_rolls_secret_within_active_range():
    state = build_state()

    reset_game_state(state, 1, 20, secret_factory=lambda low, high: high)

    assert 1 <= state.secret <= 20
