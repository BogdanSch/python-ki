import sys, string

Index = dict[str, list[int]]

def read_stopwords() -> set[str]:
    """
    Read all the stopwords from the file "stopwords.txt". Returns the
    collection of stopwords as a set; each stopword should be stripped
    of whitespace.
    """
    stopwords = set()
    
    with open('stopwords.txt') as file:
        for word in file:
            stopwords.add(word)

    return stopwords

def convert_word(word: str) -> str:
    """
    Strips a word from all puncuation, whitespace, and digits. 
    Then converts the word into all lower case.
    Don't worry about any other strange characters that are left
    in the text.
    >>> convert_word('')
    ''
    >>> convert_word('cAt.')
    'cat'
    >>> convert_word('E-text!')
    'e-text'
    """
    return word.strip(string.punctuation +
                      string.whitespace +
                      string.digits).lower()

def create_index(filename: str, stopwords: set[str]) -> Index:
    """
    Reads `filename` and returns an index.
    * For each word in the file, the index contains a record of all line
      numbers where this word occurs.
    * Words are converted to lowercase and stripped of punctuation,
      whitespace and digits before adding to the index.
    * Empty strings and stopwords are ignored and not indexed.
    """
    words_index: Index = dict()
    with open(filename, "r") as file:
        for line_number, line in enumerate(file, 1):
            for word in line.split():
                processed_word = convert_word(word)
                if processed_word in stopwords or processed_word in string.whitespace:
                    continue

                words_index.setdefault(processed_word, []).append(line_number)

    return words_index

def search_index(word: str, book_index: Index) -> list[int]:
    """
    Find the word in book_index. Returns a list of the line numbers where
    word occurs. If the word does not occur, returns an empty list.
    >>> book_index: Index = { 
    >>> 'book': [10, 25, 120], 'llm': [1, 56, 128]
    >>> }
    >>> search_index('book', book_index)
    [10, 25, 120]
    >>> search_index('llm', book_index)
    [1, 56, 128]
    >>> search_index('chat', book_index)
    [3, 5, 25, 136]
    >>> search_index('apple', book_index)
    []
    """
    return book_index.get(word, [])

def show_search_results(searched_word: str, line_numbers: list[int]) -> None:
    """
    Displays the search results (line_numbers) nicely, 
    like in the examples.
    >>> show_search_results('book', [100, 200, 1121])
    The word "book" can be found on lines: 100, 200, 1121.
    >>> show_search_results('pattern', [20, 120, 133, 456])
    The word "pattern" can be found on lines: 20, 120, 133, 456.
    """
    lines = ", ".join(str(line_number) for line_number in line_numbers)
    print(f'The word "{searched_word}" can be found on lines: {lines}.')

def user_input_search(book_index: Index) -> None:
    """
    User input loop. For every line provided as input, convert it,
    find the line numbers, and show results.
    """
    line = input("\nEnter search term: ")
    while line not in ["q", "Q", "quit", ""]:
        searched_word = convert_word(line)
        line_numbers = search_index(searched_word, book_index)
        show_search_results(searched_word, line_numbers)
        line = input("\nEnter search term: ")

if __name__ == "__main__":
    stopwords = read_stopwords()

    if len(sys.argv) < 2:
        print("No arguments provided.",
              "Please specifiy the file you want to search.")
        sys.exit()

    book_index = create_index(sys.argv[1], stopwords)
    print("Index built for", sys.argv[1]+".",
            "Type the word you want to look up.")

    user_input_search(book_index)