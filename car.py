class Car:
    def __init__(self,color,make,model,milleage):
        self.color=color
        self.make=make
        self.model=model
        self.milleage=milleage
    def description(self):
        return f"{self.make}-{self.model} is {self.color} in color"   
    def annualMilleage(self):
        return self.milleage*12
            