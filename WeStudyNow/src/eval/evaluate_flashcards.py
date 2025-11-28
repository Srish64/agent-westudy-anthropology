def evaluate_flashcards(cards):
    score = 0
    if not cards:
        return {"score":0,"reason":"no cards"}
    n = len(cards)
    if n >= 5: score += 1
    if n >= 8: score += 1
    # check format
    good = sum(1 for c in cards[:min(5,n)] if isinstance(c, dict) and "Q" in c and "A" in c)
    if good >= 3: score += 1
    return {"score": score, "count": n, "good_pairs": good}