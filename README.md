# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
  - The game is a Streamlit number guessing game where the player tries to find a secret number within a limited number of attempts. It gives higher/lower hints, tracks attempts, and updates the score based on the result.
- [x] Detail which bugs you found.
  - The hints were backwards, the first submit did not show the updated attempt count correctly, and New Game did not fully reset the previous round. Difficulty settings also needed consistent ranges and attempt limits.
- [x] Explain what fixes you applied.
  - I moved the shared game logic into `logic_utils.py`, fixed the guess comparison and scoring logic, added a reset helper for new games, refreshed the attempt display after submits, and added pytest/Streamlit regression tests.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:
Secret: 35
1. User enters a guess of 36
2. Game returns "Go Lower!"
3. User enters a guess of 34
4. Game returns "Go Higher!"
5. Game Ends after correct guess or ends after given attempts and shows "Out of attempts! The secret was 27. Score: 0" 

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
tests/test_attempt_display.py ...                              [ 15%]
tests/test_fix_comments.py ...                                 [ 30%]
tests/test_game_logic.py ........                              [ 70%]
tests/test_new_game_reset.py .....                             [ 95%]
tests/test_reset_game_state.py .                               [100%]

========================= 20 passed in 0.31s =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
