with open("books.txt") as books_file:
    books = []

    for line in books_file:
        clean_line = line.strip()
        books.append(clean_line)

    for line in books:
        print(line)

numbers = [23, -7, 8.5, 16, 30]

number = numbers.index(5)