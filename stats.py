def word_count(text: str) -> int:
    return len(text.split())


def char_count(text: str) -> dict[str, int]:
    lower_text = text.lower()
    char_counts = {}
    for c in lower_text:
        if c in char_counts:
            char_counts[c] += 1
        else:
            char_counts[c] = 1
    return char_counts
