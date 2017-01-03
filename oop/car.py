
class Car(object):
    def __init__(self, price, speed, fuel, mileage):
      self.price = price
      self.speed = speed
      self.fuel = fuel
      self.mileage = mileage
      if self.price > 10000:
        tax = .15
      else:
        tax = .12
      self.tax = tax
      print "New car created"

    def display_all(self):
        print "Price: $" + str(self.price)
        print "Speed: " + str(self.speed) + ' mph'
        print "Fuel " + str(self.fuel)
        print "Mileage: " + str(self.mileage) + ' mph'
        print "Tax rate " + str(self.tax)

Car1 = Car(23456, 75, 'Full', 15)
Car1.display_all()

Car2 = Car(12345, 25, 'Half', 25)
Car2.display_all()

Car3 = Car(3456, 65, 'Quarter', 35)
Car3.display_all()

Car4 = Car(4567, 55, 'Almost full', 45)
Car4.display_all()

Car5 = Car(11223, 85, 'Half', 15)
Car5.display_all()

Car6 = Car(23456, 75, 'Quarter', 15)
Car6.display_all()
