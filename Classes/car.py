# class Car:
#     make = "Subaru"


class Car:
    def __init__(self,make,model,color):
        self.make = make
        self.model = model
        self.color = color
       

    def car_start(self):
        return f"The {self.make} is starting"
    def car_stop(self):
        return f"The {self.make} has stopped"
    def car_accelerate(self):
        return f"The {self.make} has accelerated"
