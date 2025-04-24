FRANK_PATH = "books/frankenstein.txt"


def get_book_text(file_path):
    with open(file_path) as f:
        text = f.read()
    return text


def main():
    print(get_book_text(FRANK_PATH))


main()
