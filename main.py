import sys
from stats import get_word_count
from stats import get_book_text
from stats import get_letter_count
from stats import get_tally_text


def main():
    print("============ BOOKBOT ============") # matches file name!
    print(f"Analyzing book found at {sys.argv[1]}...")
    get_word_count(sys.argv[1])
    print("--------- Character Count -------")
    report = get_tally_text(sys.argv[1])
    for item in report:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
    main()