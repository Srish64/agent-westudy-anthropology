def clean_text(text: str) -> str:
    if not text:
        return ""
    t = text.replace("\r", " ").strip()
    # collapse whitespace
    t = " ".join(t.split())
    # remove weird control chars
    t = "".join(ch for ch in t if ord(ch) >= 32 or ch in ("\n","\t"))
    return t