from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_hint_direction_too_high():
    # Bug fix: when guess > secret the message must say Go LOWER, not Go HIGHER
    outcome, message = check_guess(75, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected 'LOWER' in hint when guess is too high, got: '{message}'"

def test_hint_direction_too_low():
    # Bug fix: when guess < secret the message must say Go HIGHER, not Go LOWER
    outcome, message = check_guess(25, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected 'HIGHER' in hint when guess is too low, got: '{message}'"

def test_secret_always_compared_as_int():
    # Bug fix: secret was cast to str on even attempts, causing lexicographic comparison.
    # e.g. str(9) > str(42) is True because "9" > "4", giving a wrong "Too High" outcome.
    # Both args must always be ints so numeric comparison is used.
    outcome, _ = check_guess(9, 42)
    assert outcome == "Too Low", "guess=9 < secret=42 must be 'Too Low', not 'Too High' (string comparison bug)"
