class Student:
    def __init__(self, id=0, name=None, age=0, prec=0):
        self.id = id
        self.name = name
        self.age = age
        self.prec = prec
    
    def Display(self):
        print("Id :", self.id)
        print("Name :", self.name)
        print("Age :", self.age)
        print("Precentage :", self.prec)
    def Accept(self):
        self.id = int(input("Enter a id:"))
        self.name = input("Enter a name:")
        self.age = int(input("Enter a age:"))
        self.prec = int(input("Enter a percentage:"))
        
    def Rank(self):
        if self.prec > 90:
            print("Rank A")
        elif self.prec >60:
            print("Rank B")
        elif self.prec >30:
            print("Rank C")
        else:
            print("Rank D")
    def __str__(self):
        return f'Id:{self.id}\nName:{self.name}\nAge:{self.age}\nPercentage:{self.prec}'

class EnggStudent(Student):
    def __init__(self, id=0, name=None, age=0, prec=0, branch = None, internal_m = 0):
        super().__init__(id, name, age, prec)
        self.branch = branch
        self.im = internal_m
    def Display(self):
        super().Display()
        print('Branch :', self.branch)
        print('Internal Mraks:', self.im)
    def Accept(self):
        super().Accept()
        self.branch = input('Enter a branch:')
        self.im = int(input('Enter a internal marks:'))
    def Rank(self):
        if self.im > 20:
            print("Rank A")
        elif self.im > 15:
            print("Rank B")
        else:
            print("Rank C")
    def __str__(self):
        return f'Id:{self.id}\nName:{self.name}\nAge:{self.age}\nPercentage:{self.prec}'


s1 = EnggStudent()
s1.Accept()
s1.Display()
s1.Rank()
print(s1)
