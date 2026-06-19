import random


class GuessResult(str):
    """String outcome that can still unpack into (outcome, message)."""

    def __new__(cls, outcome: str, message: str):
        obj = super().__new__(cls, outcome)
        obj.message = message
        return obj

    def __iter__(self):
        yield str(self)
        yield self.message


def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    #FIX: Refactored difficulty settings with AI help so range and attempts scale together.
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 200
    return 1, 100


def get_attempt_limit_for_difficulty(difficulty: str):
    """Return the number of guesses allowed for a given difficulty."""
    if difficulty == "Easy":
        return 10
    if difficulty == "Normal":
        return 8
    if difficulty == "Hard":
        return 5
    return 8


def format_attempts_status(low: int, high: int, attempts_left: int):
    """Return the status message shown above the guess input."""
    return f"Guess a number between {low} and {high}. Attempts left: {attempts_left}"


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


# Core guess-comparison logic used by the app and tests.
def check_guess(guess, secret):
    """
    Compare guess to secret and return a result that behaves like a string.
    """
    # I matched the hint text to the shared comparison logic after the AI pointed out the branch was inverted.
    if guess == secret:
        return GuessResult("Win", "🎉 Correct!")

    if guess > secret:
        return GuessResult("Too High", "📈 Go HIGHER!")
    return GuessResult("Too Low", "📉 Go LOWER!")


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number - 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score


def reset_game_state(session_state, low: int, high: int, secret_factory=None):
    """
    Reset a game round in place.

    `session_state` can be Streamlit session state or a simple test double.
    """
    if secret_factory is None:
        secret_factory = random.randint

    # I kept the AI's reset-helper idea and used it to clear every round field together so stale state cannot linger.
    session_state.attempts = 0
    session_state.history = []
    session_state.score = 0
    session_state.status = "playing"
    session_state.secret = secret_factory(low, high)
