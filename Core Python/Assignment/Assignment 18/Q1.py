class Complexn:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __del__(self):
        print("Number deleted...!")
        
    def __add__(self, other):
        return Complexn(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complexn(self.real - other.real, self.imag - other.imag)

    def __str__(self):
        return f"{self.real} + {abs(self.imag)}i"

c1 = Complexn(3, 4)
c2 = Complexn(2, 1)

c3 = c1 + c2
print(c3)

c4 = c1 - c2
print(c4)