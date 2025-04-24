import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]
from stats import get_num_words, get_character_count, get_sorted_list

def main():
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    character_count = get_character_count(text)
    sorted_list = get_sorted_list(character_count)
    for a in sorted_list:
        if a['char'].isalpha():
            print(f"{a['char']}: {a['num']}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()