# encapsulation
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.__speed = 0  # private attribute

    def accelerate(self, amount):
        self.__speed += amount
        print(f"Accelerating: {self.__speed} km/h")

    def brake(self, amount):
        self.__speed -= amount
        if self.__speed < 0:
            self.__speed = 0
        print(f"Braking: {self.__speed} km/h")

    def get_speed(self):
        return self.__speed

# Example usage
my_car = Car("Toyota", "Corolla", 2020)
my_car.accelerate(50)
my_car.brake(20)