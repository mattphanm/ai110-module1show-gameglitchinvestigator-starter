from types import SimpleNamespace

from logic_utils import reset_game_state


def test_reset_game_state_clears_round_progress():
    state = SimpleNamespace(
        attempts=4,
        history=[12, 18, 22],
        score=75,
        status="lost",
        secret=99,
    )

    reset_game_state(state, 1, 20, secret_factory=lambda low, high: 7)

    assert state.attempts == 0
    assert state.history == []
    assert state.score == 0
    assert state.status == "playing"
    assert state.secret == 7
