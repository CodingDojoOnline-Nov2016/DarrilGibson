class Bike(object):
    # def __init__(self):
    def __init__(self, price, max_speed):
      print "New bike created"
      self.price = price
      self.max_speed = max_speed
      self.miles = 0

    def displayinfo(self):
        print "Price is $" + str(self.price)
        print "Max speed is " + str(self.max_speed) + ' MPH'
        print "Current mileage is " + str(self.miles) + ' miles'
        return self

    def ride(self):
        print "Riding"
        self.miles = self.miles + 10
        print "Current mileage is " + str(self.miles) + ' miles'
        return self

    def reverse(self):
        print "Reversing"
        self.miles = self.miles - 5
        print "Current mileage is " + str(self.miles) + ' miles'
        return self

Racer = Bike(119.99, 25)
Mountain = Bike(399.99, 20)
Racer.ride().ride().reverse().displayinfo()
Mountain.ride().displayinfo().ride().displayinfo().reverse().displayinfo()
# Racer = Bike(119.99, 25)
# Racer.ride()
# Racer.ride()
# Racer.ride()
# Racer.reverse()
# Racer.displayinfo()
#
# mountain = Bike(399.99, 20)
# mountain.ride()
# mountain.ride()
# mountain.reverse()
# mountain.reverse()
# mountain.displayinfo()
