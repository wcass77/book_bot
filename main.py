from stats import word_count

FRANK_PATH: str = "books/frankenstein.txt"


def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        text = f.read()
    return text


def main() -> None:
    text = get_book_text(FRANK_PATH)
    wc = word_count(text)
    print(f"{wc} words found in the document")


main()
