from abc import ABC, abstractmethod     # Imported abstractmethod from the abc module.

class Phone(ABC):                       # Defined parent class
    def __init__(self,model: str):      # Initialized class
        self.model = model              # Defined property "model"

    @abstractmethod                     # Called on abstractmethod
    def power(self):                    # Without abstractmethod, Python would not allow
        pass                            # us to instantiate, and would return an error




class Pixel(Phone):                     # Created child class "Pixel"
    def __init__(self, model: str):     # Initialized class
        super().__init__(model)         # Gave all properties from parent class

    def power(self):                    # Defined to print out
        print("Fully charged.")         # "Fully Charged" when called




pixel = Pixel(Phone)                    # Created object named "pixel"
print(pixel.power())                    # print() calls on Pixel's property to print out
                                        # "Fully charged.









"""
from abc import ABC, abstractmethod
class car():
    def paySlip(self, amount):
        print("Your purchase amount: ",amount)
    @abstractmethod
    def payment(self,amount):
        pass
class DebitCardPayment(car):
    def payment(self,amount):
        print('Your purchase amount of {} exceeded your $100 limit '.format(amount))

obj = DebitCardPayment()
obj.paySlip("$400")
obj.payment("$400")
"""
