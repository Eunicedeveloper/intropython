class Base:
    def __init__(self):
        self.a = "i have rights"
        self.e = "and privileges"
        self.__f = "more rights"
        self.g = "and power"


class derived(Base):
    def __init__(self):
        print(self.a) #accessible
        print(self.e) #accessible
        print(self.__f) #not accessible
        print(self.g) #accessible


# create an intance of the parent class

obj1 = Base()
print(obj1.a)
print(obj1.e)
#print(obj1.f) #-"you don't have rights and permission
print(obj1.g)
