"""
class Thing():
    pass
example = Thing()
print(Thing)
print(example)

class Thing2():
    letters = "abc"
print(Thing2.letters)


class Thing3():
    def __init__(self, letters):
        self.letters = letters
t = Thing3("xyz")
print(t.letters)
"""

class Element():
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    def __str__(self):
        return self.__symbol

    def get_name(self):
        return self.__name
    def get_symbol(self):
        return self.__symbol
    def get_number(self):
        return self.__number


    def set_name(self, input_name):
        self.__name = input_name

    def set_symbol(self, input_symbol):
        self.__symbol = input_symbol

    def set_number(self, input_number):
        self.__number = input_number
    name = property(get_name, set_name)
    symbol = property(get_symbol, set_symbol)
    number = property(get_number, set_number)



#element1 = Element("Hydrogen", "H", 1)
#print(element1.name, element1.symbol, element1.number)
#element1_dict = {'name' : 'Hydrogen', 'symbol' : 'H', 'number' : 1}
#print(element1_dict)
#hydrogen = Element(**element1_dict)
#print('hydrogen.name ',hydrogen.name)
#hydrogen1 = Element("Hydrogen", "H", 1)
#print('dump ',hydrogen.dump)
#print(hydrogen1)
element_of_table = Element("Hydrogen", "H", 1)

#element_of_table.name = "Oxigen"
element_of_table.symbol = "O"
#element_of_table.number = 16

#print('element_of_table: ', element_of_table)


class Animal():
    def __init__(self, name, food):
        self.name = name
        self.eats = food
    def name(self):
        return self.name
    def eats(self):
        return f"{self.eats}"


animal = Animal('Marty', 'fruit')

class Bear(Animal):
    def __str__(self):
        return f"{self.eats}"

bear = Bear('Bear', 'berries')
print(bear.name, ' eats: ', bear.eats)


class Rabbit(Animal):
    pass
rabbit = Rabbit('Rabbit', 'clover')
#print(rabbit.name, ' eats: ', rabbit.eats)


class Octothorpe(Animal):
    pass
octothorpe = Octothorpe('Octothorpe', 'campers')
#print(octothorpe.name, ' eats: ', octothorpe.eats)


class BabblingBrook():
    def __init__(self, name):
        self.name = name
    def name(self):
        return 'Brook'
    def eats(self):
        return 'Hamburger'
brook = BabblingBrook()


def who_eats(obj):
    print( obj.name, ' is eating: ', obj.eats )

who_eats(brook)
who_eats(bear)
who_eats(animal)
who_eats(rabbit)
who_eats(octothorpe)



