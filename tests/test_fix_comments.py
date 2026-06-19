from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]


def read_source(relative_path):
    return (ROOT_DIR / relative_path).read_text()


def test_attempt_placeholder_fix_has_collaboration_comment():
    source = read_source("app.py")

    assert (
        "#FIX: Used AI guidance to keep the layout while refreshing the attempts text after submit."
        in source
    )


def test_attempt_rerender_fix_has_collaboration_comment():
    source = read_source("app.py")

    assert (
        "#FIX: Re-rendered the existing placeholders with AI help so first submit shows the new attempt count."
        in source
    )


def test_attempt_display_tests_have_collaboration_comment():
    source = read_source("tests/test_attempt_display.py")

    assert (
        "#FIX: Added Streamlit regression tests with AI help for the first-submit attempt display bug."
        in source
    )
