def evaluate_summary_text(text: str):
    score = 0
    reasons = []
    if not text or len(text.strip()) < 30:
        return {"score":0,"reasons":["too short"]}
    score += 1
    if len(text.splitlines()) >= 3:
        score += 1
        reasons.append("multiple bullets")
    keywords = ["anthropology","human","culture","evolution","archaeology"]
    found = [k for k in keywords if k in text.lower()]
    if found:
        score += 1
        reasons.append("keywords found")
    return {"score": score, "reasons": reasons, "keywords": found}