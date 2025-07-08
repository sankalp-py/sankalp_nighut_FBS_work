class Book:
    count = 0
    def __init__(self, id=None, name=None, price=0, author=None):
        Book.count += 1
        self.id = id 
        self.name = name 
        self.price = price
        self.author = author
    
    def showData(self):
        print("Book Id:", self.id)
        print("Book name:", self.name)
        print("Book price:", self.price)
        print("Book author:", self.author)
    
    def __del__(self):
        print("Destractor is called.")
    
    @staticmethod
    def totalCount():
        print("Total Streagth of student is",Book.count) 
    

book1 = Book(1, 'Python', 250, 'Giudo Van Rossum')
book1.showData()
book2 = Book(2, 'Java', 400, 'Reo star')
print('Total books:', Book.count)