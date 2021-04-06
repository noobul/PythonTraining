import book

runner = True

while runner:
    prompt = ("Why do you like programming?(type 'q' to quit): ")
    answer = input(prompt)

    if answer == 'q':
        runner = False
    else:
        answers = book.Book(answer)
        answers.append_in_book('answers.txt', answer)