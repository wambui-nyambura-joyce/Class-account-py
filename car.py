class Car:
    wheels = 4
    def __init__(self,make,model,color):
        self.make = make
        self.colour = color
        self.model = model
    def  start_car(self):
        return (f"My {self.make} produces a sound voomvoom when it's started.")
        # return (f"voomvoom")   
    def car_capacity(self):
        return (f"My {self.colour} {self.model} has a capacity of 4 people")
    def car_acceleration(self):
        return (f"Joy's {self.make} has an acceleration of 30 m/s squared.")