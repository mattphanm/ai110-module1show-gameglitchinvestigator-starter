from streamlit.testing.v1 import AppTest

from logic_utils import format_attempts_status


#FIX: Added Streamlit regression tests with AI help for the first-submit attempt display bug.
def run_app():
    app = AppTest.from_file("app.py")
    app.run(timeout=5)
    return app


def assert_attempts_left(app, expected_attempts_left):
    #FIX: Updated the display check with AI help so the prompt follows the active difficulty range.
    assert app.info[0].value == format_attempts_status(1, 100, expected_attempts_left)


def test_attempts_left_starts_at_attempt_limit():
    app = run_app()

    assert app.session_state.attempts == 0
    assert_attempts_left(app, 8)


def test_first_valid_submit_updates_attempts_left_immediately():
    app = run_app()
    app.session_state.secret = 50

    app.text_input[0].set_value("25")
    app.button[0].click().run(timeout=5)

    assert app.session_state.attempts == 1
    assert_attempts_left(app, 7)


def test_first_invalid_submit_updates_attempts_left_immediately():
    app = run_app()

    app.text_input[0].set_value("not a number")
    app.button[0].click().run(timeout=5)

    assert app.session_state.attempts == 1
    assert_attempts_left(app, 7)
