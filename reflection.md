# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
the hint logic was incorrect, the hint would say go lower when the number was higher at the end of the game.

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|50     |go higher          | go lower.       | None.                  |
|90     |go lower           | go higher       | None.                  |

---

## 2. How did you use AI as a teammate?
- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude as my AI tool. 

Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Claude correctly identified the incorrect "Go HIGHER/LOWER" jand suggested that we swapped the "Go HIGHER/LOWER" messages in check_guess.

Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
When Claude added the two new pytest cases, it ran them and reported them as passing, but it didn't point out that the 3 pre-existing tests were already broken. I had to ask why does it say some tests failing? before Claude explained that those tests were comparing result == "Win" when check_guess actually returns a tuple ('Win', '🎉 Correct!')
- 
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
i ran pytest-v after each fix and checked that the new tests passed.

- Describe at least one test you ran (manual or using pytest)  
for this test: test_secret_always_compared_as_int used check_guess(9, 42) and asserted the outcome was "Too Low". Under the old bug, str(9) > str(42) is True because "9" > "4" lexicographically, so it would have returned "Too High" which completely wrong. that test exposed the failure case.

- Did AI help you design or understand any tests? How?
yes, claude suggested the specific input values (9, 42) to expose the string comparison bug, explaining why that pair breaks lexicographic ordering but not numeric ordering
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
everytime a user interatcs with a streamlit application(clicks a button), the entire python script reruns from top to bottom. without st.session_state, every rerun would reset the variables, its like a notebook that streamlit holds onto between page refreshes, while everything else gets wiped.

---

## Demo Walkthrough

Difficulty: Normal | Range: 1–100 | Max attempts: 8 | Secret number: 63

1. **User enters 40** → `check_guess(40, 63)` returns `"Too Low"` → hint displays "📈 Go HIGHER!" → score: 0 − 5 = **−5**
2. **User enters 75** → `check_guess(75, 63)` returns `"Too High"` → hint displays "📉 Go LOWER!" → score: −5 − 5 = **−10**
3. **User enters 60** → `check_guess(60, 63)` returns `"Too Low"` → hint displays "📈 Go HIGHER!" → score: −10 − 5 = **−15**
4. **User enters 65** → `check_guess(65, 63)` returns `"Too High"` → hint displays "📉 Go LOWER!" → score: −15 − 5 = **−20**
5. **User enters 63** → `check_guess(63, 63)` returns `"Win"` → win bonus = 100 − 10×(6+1) = 30 → final score: −20 + 30 = **10** → 🎉 balloons

Session state after game: `attempts=6`, `status="won"`, `history=[40, 75, 60, 65, 63]`

---

## 5. Looking ahead: your developer habits
Writing tests that use specific edge-case inputs (like check_guess(9, 42)) rather than just normal values

id ask my AI to check existing tests before adding new ones

AI-generated code can look correct and even run without errors while still having subtle logic bugs 
- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
