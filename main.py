import sys

from stats import char_count, char_dicts, word_count


def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        text = f.read()
    return text


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    wc = word_count(text)
    char_counts = char_count(text)
    sorted_dicts = char_dicts(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_dicts:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")
    print("============= END ===============")


main()
