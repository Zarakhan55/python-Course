class Library:
    def __init__(self, books):
        self.books = books

    def __len__(self):
        return len(self.books)
library = Library(["Python", "HTML", "CSS"])

print(len(library))












class Cart:
    def __init__(self, items):
        self.items = items
    def __len__(self):
     return len(self.items)
c1 = Cart(["Laptop", "Mouse", "Keyboard"])

print(len(c1))
