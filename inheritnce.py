# **INHERITANCE//CONSTRUCTOR ND METHOD OVERRIDING********

"""class BaseClass:
    def __init__(self):
        print("base init")

    def set_name(self, name):
        self.name = name
        print("base hiiiiiiiiiiiii")

    def display(self):
        print("name : " + self.name)


class SubClass(BaseClass):
    def fn(self):
        print("subclass")

    def __init__(self):
        super().__init__()
        print("sub init")

    def set_name(self, name):
        super().set_name(name)
        print("sub hiiiiiiiiiiiii")


y = SubClass()
y.fn()
y.set_name("lishi")
y.display()"""


# **************MULTILEVEL INHERITANCE*************
"""class First:
    def display_first(self):
        print("first")


class Second(First):
    def display_second(self):
        print("second")


class Third(Second):
    def display_third(self):
        print("third")

x = Third()
x.display_first()
x.display_second()
x.display_third()"""


#**************MULTIPLE INHERITANCE**************
"""class First:
    def display(self):
        print("first")


class Second:
    def display(self):
        print("second")


class Third(First,Second):
    def display_third(self):
        print("third")


x = Third()
x.display()
#x.display_second()
x.display_third()"""


#***************OPERATOR OVERLOADING******************
class sample:
    def set_name(self,n):
        self.name = n

    def __add__(self, other):
        name = self.name + other.name
        return name

s1 = sample()
s2 = sample()
s3 = sample()

s1.set_name("Deva")
s2.set_name("Durga")
s3.set_name("Vidhunraj")

full_name =s1 + s2 + s3
print(full_name)

