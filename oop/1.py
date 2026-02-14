class Person:
    name = None
    surname = None
    age = None
    price = None

    def __init__(self, name, surname, age, price):
        self.name = name
        self.surname = surname
        self.age = age
        self.price = price

    def __repr__(self):
        return f"\n{self.__class__.__name__}\nName: {self.name}\nSurname: {self.surname}\nAge: {self.age}\nPrice {self.price}"

    class Builder:

        def name(self, _name):
            self.name = _name
            return self
        def surname(self, _surname):
            self.surname = _surname
            return self
        def age(self, _age):
            self.age = _age
            return self
        def price(self, _price):
            self.price = _price
            return self
        
        def build(self):
            return Person(self.name, self.surname, self.age, self.price)

    def canDrink(self):
        if (self.age < 21):
            return f"{self.name} can't drink at age {self.age} which is less than the legal minimum 21"

person = Person.Builder().age(18).surname("Thomas").name("George").price(123.123).build()
print(str(person))

