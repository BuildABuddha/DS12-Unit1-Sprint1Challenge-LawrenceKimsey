import random


class Product(object):
    """
    A product of ACME.
    Warrenty void when package is opened.
    """

    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        if (self.price / self.weight) < 0.5:
            return "Not so stealable..."
        elif (self.price / self.weight) >= 1:
            return "Very stealable!"
        else:
            return "Kinda stealable."

    def explode(self):
        if (self.flammability * self.weight) < 10:
            return "...fizzle."
        elif (self.flammability * self.weight) >= 50:
            return "...BABOOM!!"
        else:
            return "...boom!"


class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif self.weight >= 15:
            return "OUCH!"
        else:
            return "Hey that hurt!"
