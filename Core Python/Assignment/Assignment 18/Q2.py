class Distance:
    def __init__(self, km, m, cm):
        self.km = km
        self.m = m
        self.cm = cm
    def __del__(self):
        print("Deleted..!")
    def __add__(self, other):
        cm = self.cm + other.cm
        m = cm // 100
        cm = cm % 100
        m = m + self.m + other.m
        km = m // 1000
        m = m % 1000
        km = km + self.km + other.km
        return f'{km}, {m}, {cm}'
    def __sub__(self, other):
        if (self.km < other.km or self.m < other.m or self.cm < other.cm):
            print("Can't minus distance")
        else:
            cm = self.cm - other.cm
            m = cm // 100
            cm = cm % 100
            m = m + self.m - other.m
            km = m // 1000
            m = m % 1000
            km = km + self.km - other.km
            return f'{km}, {m}, {cm}'

d1 = Distance(2, 1500, 350)
d2 = Distance(2, 2000, 100)

print(d1 - d2) 