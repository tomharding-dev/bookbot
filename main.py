from stats import count_words, count_chars, gen_report
import sys

def get_book_text(book_path):
    with open(book_path) as book_file: # Open the book file in read mode 
        book_text = book_file.read() # Read the book text
    return book_text # Return the book text

def main():
    if len(sys.argv) != 2: # Check if the correct number of arguments is provided
        print("Usage: python3 main.py <path_to_book>") 
        sys.exit(1)
    
    book_path = sys.argv[1] # Get the book path from command line argument
    book_text = get_book_text(book_path) # Read the book text
    word_count = count_words(book_text) # Count the words in the book
    sorted_count = gen_report(count_chars(book_text)) # Sort the character counts 
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}") # Print the book path
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words") # Print the total word count
    print("--------- Character Count -------")
    for x in sorted_count: # Iterate through the sorted character counts
        if x['character'].isalpha() == True:  # Check if character is alphabetic
            print(f"{x['character']}: {x['count']}") # Print the character and its count
    print("============= END ===============")
    
main()