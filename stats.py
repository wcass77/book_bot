from typing import Union


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


def char_dicts(char_counts: dict[str, int]) -> list[dict[str, Union[str, int]]]:
    list_dicts = []
    for key in char_counts:
        char_dict = {"char": key, "num": char_counts[key]}
        list_dicts.append(char_dict)
    list_dicts.sort(reverse=True, key=lambda x: x["num"])
    return list_dicts
