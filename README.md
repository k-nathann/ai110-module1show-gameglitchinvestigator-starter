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

**Game purpose:** This is a number guessing game where the player tries to guess a secret number within a limited number of attempts. After each guess, the game gives a hint telling you to go higher or lower. A score is tracked based on how many attempts it takes to win.

**Bugs found:**
- The hint direction was backwards — when your guess was too high the game told you to go higher, and when it was too low it told you to go lower, which made the game impossible to win by following the hints.
- On every even-numbered attempt, the secret number was secretly converted to a string before being compared to your guess. This caused the comparison to use alphabetical ordering instead of numeric ordering, so a guess of 9 would be considered greater than 42 because "9" comes after "4" alphabetically.

**Fixes applied:**
- In `logic_utils.py`, swapped the hint messages inside `check_guess` so that `guess > secret` returns "Go LOWER" and `guess < secret` returns "Go HIGHER".
- In `app.py`, removed the even/odd attempt branch that was casting the secret to a string. The secret is now always passed as an integer to `check_guess`.
- Moved `check_guess` from `app.py` into `logic_utils.py` and updated the import so the function lives with the other game logic.


## Demo Walkthrough

Difficulty: Normal | Range: 1–100 | Max attempts: 8 | Secret number: 63

1. **User enters 40** → `check_guess(40, 63)` returns `"Too Low"` → hint displays "📈 Go HIGHER!" → score: 0 − 5 = **−5**
2. **User enters 75** → `check_guess(75, 63)` returns `"Too High"` → hint displays "📉 Go LOWER!" → score: −5 − 5 = **−10**
3. **User enters 60** → `check_guess(60, 63)` returns `"Too Low"` → hint displays "📈 Go HIGHER!" → score: −10 − 5 = **−15**
4. **User enters 65** → `check_guess(65, 63)` returns `"Too High"` → hint displays "📉 Go LOWER!" → score: −15 − 5 = **−20**
5. **User enters 63** → `check_guess(63, 63)` returns `"Win"` → win bonus = 100 − 10×(6+1) = 30 → final score: −20 + 30 = **10** → 🎉 balloons

Session state after game: `attempts=6`, `status="won"`, `history=[40, 75, 60, 65, 63]`

---
## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
