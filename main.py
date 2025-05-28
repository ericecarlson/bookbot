
from stats import count_words, count_characters, sort_characters 
import sys

def get_book_text(file_path):
    """
    Reads the content of a book file and returns it as a string.
    
    Args:
        file_path (str): The path to the book file.
        
    Returns:
        str: The content of the book.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    """
    Main function to demonstrate reading a book file. We set the file path and call the function to read the book.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    elif file_path := sys.argv[1]:
        if not file_path.endswith('.txt'):
            print("Please provide a valid text file.")
            sys.exit(1)
    book_text = get_book_text(file_path)
    word_count = count_words(book_text)
    character_count = count_characters(book_text)
    ## printing the results
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words ")
    print(f"--------- Character Count -------")
    sorted_character_count = sort_characters(character_count)
    ## loop through the sorted character count dictionary and print each character and its count
    for char, count in sorted_character_count.items():
        if char.isalpha():
            print(f"{char}: {count}")
if __name__ == "__main__":
    main()