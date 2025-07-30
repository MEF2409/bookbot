from stats import get_num_words, letter_list, better_list
import sys

def main():
    if len(sys.argv) > 1:
        book = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(book)
    num_words = get_num_words(book_text)
    letters = letter_list(book_text)
    list_sorted = better_list(letters)
        
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for characters in list_sorted:
        character = characters["char"]
        counts = characters["num"]
        if str(character).isalpha():
            print(f"{character}: {counts}")
    print("============= END ===============")

def get_book_text(text_file):
    with open(text_file) as f:
        text = f.read()
    return text

main()