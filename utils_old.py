class Book:

    favorites = []

    
    def __init__(self, title, pages):
        print('Creating a book...')
        self.title = title
        self.pages = pages
        

    def is_long(self):
        if self.pages > 300:
            return True
        return False
    
    def __str__(self):
        return f'{self.title} is {self.pages} pages long'

    def __eq__(self, other):
        if self.title == other.title and self.pages == other.pages:
            return True
        return False


    def __hash__(self):
        return hash(self.title) ^ hash (self.pages)



    

