class Shirt:
    m_charge = 0.2
    l_charge = 0.3
    s_charge = 0.1
    def __init__(self, id, name, type, price, size):
        self.id = id 
        self.name = name
        self.type = type
        self.price = price
        self.size = size 
    
    def __del__(self):
        print('Destractor is called.')
    
    def showData(self):
        print('Id:', self.id)
        print('Name:', self.name)
        print('Type:', self.type)
        print('Size:', self.size)
        if (self.size == 's'):
            self.pri = (self.price * Shirt.s_charge)
            print('Price:',self.price + self.pri)
        elif(self.size == 'm'):
            self.pri = (self.price * Shirt.m_charge)
            print('Price:',self.price + self.pri)
        else:
            self.pri = (self.price * Shirt.l_charge)
            print('Price:',self.price + self.pri)

s1 = Shirt(1, 'Polo', 'Casual', 250, 's')
s1.showData()

s2 = Shirt(2, 'Tshirt', 'Casual', 150, 'm')
s2.showData()