class Product:
    def __init__(self, id=None, name=None, price=0, quantity=0):
        self.id = id 
        self.name = name 
        self.price = price
        self.quantity = quantity
    
    def showData(self):
        print("Product id:", self.id)
        print("Product name:", self.name)
        print("Product price:", self.price)
        print("Product Quantity:", self.quantity)
    
    def __del__(self):
        print("Destractor is called.")
        
p1 = Product(1, 'Rice', 45, 2)
p1.showData()

p2 = Product(2, 'Sugar', 56, 1)
del p2 