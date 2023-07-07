# Parent Class
class vehicle:
    name = "vehicle"
    method = "moves"
    
    def move(self):
        print("A {} {}.".format(self.name,self.method))
              

class car(vehicle):
    name = "car"
    method = "drives"

    def move(self):
        print("A {} {}.".format(self.name,self.method))


class plane(vehicle):
    name = "plane"
    method = "flies"

    def move(self):
        print("A {} {}.".format(self.name,self.method))

vehicle = vehicle()
vehicle.move()

car = car()
car.move()

plane = plane()
plane.move()
