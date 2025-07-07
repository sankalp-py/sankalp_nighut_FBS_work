class Shirt:
    def __init__(self, id=None, name=None, type=None, price=0, size=None):
        self.id = id 
        self.name = name
        self.type = type
        self.price = price
        self.size = size 
        
    def showData(self):
        print('Shirt id:', self.id)
        print('Shirt name:', self.name)
        print('Shirt type:',self.type)
        print('Shirt Price:', self.price)
        print('Shirt Size:', self.size)
    
    def __del__(self):
        print("Destractor is called.")
    
s1 = Shirt(1, 'Polo', 'Casual', 250, 'S')
s1.showData()

s2 = Shirt(2, 'Tshirt', 'Casual', 150, 'M')
del s2