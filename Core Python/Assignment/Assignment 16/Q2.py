class Product:
    discount = 0.1
    def __init__(self, id=0, name=None, price=0, quantity=0):
        self.id = id 
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def __del__(self):
        print('Desrctactor is called.')
        
    def showProduct(self):
        print('ID:', self.id)
        print('Name:', self.name)
        print('Quantity:', self.quantity)
        self.dis = (self.price * self.quantity )* Product.discount
        print('Price:',(self.price * self.quantity ) - self.dis)
        
p1 = Product(1, 'Rice', 45, 2)
p1.showProduct()

p2 = Product(2, 'Sugar', 56, 1)