
# How to write five properties of a book in oops

# BOOK  CLASS

class book():
    def __init__(self,Title,Author,Pages,Publication_details,location):
        self.Title = Title
        self.Author = Author
        self.Pages = Pages
        self.Publication_details = Publication_details
        self.location = location
        
# NEW  INSTANCE

book_1 = book('Harry Potter','Bloomsbury','760 pages',
              'pablished in 1997','In UK and States of America')
print(book_1)



class Author():
    def __init__(self,name,location,book_title,language,strong_vocabulary):
        self.name = name
        self.location = location
        self.book_title = book_title
        self.language = language
        self.strong_vocabulary = strong_vocabulary
        
#  NEW  INSTANCE

Author_1 = Author('J.K Rowling','United kingdom','Harry Potter',
                  'English','deathly_Hallows , Half_blood_prince',)
print(Author_1)
        






