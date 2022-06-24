from book import Book
import booksSDK


book = Book('Are you my mother?', 1000)
print('Added book id: ', booksSDK.add_book(book))
print('Get book by title: ', booksSDK.get_book_by_title(book.title))
print('Not a valid book: ', booksSDK.get_book_by_title('yeet'))

booksSDK.add_book(Book('The Digging-est Dog', 76))
print ('Get books: ', booksSDK.get_books())

book = booksSDK.update_book(book, book.title, 76)
print('Updated book: ', book)
print('Deleted: ', booksSDK.delete_book(book))
print('After delete:', booksSDK.get_book_by_title('Are you my mother?'))

print("All books: ", booksSDK.get_books())






