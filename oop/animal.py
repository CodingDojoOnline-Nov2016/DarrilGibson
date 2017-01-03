class Animal(object):
    def __init__(self, name):
        self.health = 100
        self.name = name
        print self.name + " created."

    def walk(self):
        self.health = self.health - 1
        print self.name + " is walking. Health is now " + str(self.health) + "."
        # use return self to allow chaining
        return self

    def run(self):
        self.health = self.health - 5
        print self.name + " is running. Health is now " + str(self.health) + "."
        # use return self to allow chaining
        return self

    def displayHealth(self):
        print "Animal's name is " + str(self.name) + "."
        print self.name + "'s health is " + str(self.health) + "."
        # use return self to allow chaining
        return self

class Dog(Animal):
    def health(self):
        self.health = 150
        # use return self to allow chaining
        return self

    def pet(self):
        self.pet = self.health + 5
        print self.name + "'s health is " + str(self.health) + "."
        # use return self to allow chaining
        return self

class Dragon(Animal):
    def health(self):
        self.health = 170
        print self.name + "'s health is " + str(self.health) + "."
        # use return self to allow chaining
        return self

    def fly(self):
        self.health = self.health - 10
        print self.name + "'s health is " + str(self.health) + "."
        # use return self to allow chaining
        return self

Kitty = Animal('Kitty')
Kitty.walk().walk().walk().run().run().displayHealth()
#  Kitty.fly()  fails  AttributeError: 'Animal' object has no attribute 'fly'
# Kitty.pet() fails  AttributeError: 'Animal' object has no attribute 'fly'

Gray = Dog('Gray')
Gray.walk().walk().walk().run().run().pet().displayHealth()

Dragonheart = Dragon('Dragonheart')
Dragonheart.walk().walk().walk().run().run().fly().fly().displayHealth()
