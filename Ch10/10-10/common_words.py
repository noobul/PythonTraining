franken = "Ch10/10-10/Frankenstein.txt"
pnp = "Ch10/10-10/Pride and Prejudice.txt"

def word_counter(word, book_name):
    try:
        result = 0    
        with open(book_name) as f:
            for line in f:
                counter = line.lower().count(word)
                result += counter
            print(result)
    except FileNotFoundError:
        print('File not found')

books = [franken, pnp]

for book in books:
    word_counter('the ', book)