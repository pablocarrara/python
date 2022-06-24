class Book():

    favs = []

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def log(self):
        print(f'{self.title} is {self.pages} pages long')
        with open('log.txt', 'a+') as file:
            file.write(f'{self.title} is {self.pages} pages long\n')

    def is_short(self):
        if self.pages < 100:
            return True
        return False

    def __str__(self):
        return f'{self.title} is {self.pages} pages long'

    def __eq__(self, o):
        if self.title == o.title and self.pages == o.pages:
            return True
        return False

    def __hash__(self):
        return hash(self.title) ^ hash(self.pages)


book1 = Book('mi libro3', 77)
book1.log()
book2 = Book('mi libro4', 77)
book2.log()
