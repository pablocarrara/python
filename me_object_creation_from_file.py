import utils


def add_book(title, pages):
    with open('input.txt', 'a') as file:
        file.write(f'\n{title}\t{pages}')


with open('input.txt', 'w') as file:
    file.write('Are You My Mother?\t72\nthe Digging-est Dog\t72\n')
    file.write(
        'La Argentina devorada\t400\nHow to avoid a climate disaster\t500\n')
    file.write('Crear o morir\t600\nEl hombre mediocre\t95')


all_books = []

with open('input.txt', 'r') as file:
    data = file.read().split('\n')
    for i in range(len(data)):
        book = utils.Book(data[i].split('\t')[0], data[i].split('\t')[1])
        all_books.append(book)

    for book in all_books:
        print(book)
