class Library:
    def __init__(self,book_name,author,price):
       self.book_name=book_name
       self.author=author
       self.price=price
    def show_book(self):
        print("Book Name:",self.book_name)
        print("Author name:",self.author)
        print("price:",self.price)
    def return_book(self):
        print("Book returned successfully!")
book1=Library("OOP","zara",499)
book2=Library("js","Ali",879)
book1.show_book()
book1.return_book()
print("============================")
book2.show_book()
book2.return_book()


    
    