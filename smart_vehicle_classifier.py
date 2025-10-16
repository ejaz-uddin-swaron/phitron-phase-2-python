class Vehicle:
    def __init__(self, type, name, speed):
        self.type = type
        self.name = name
        self.__speed = speed

    def speed_getter(self):
        return self.__speed
    
    def classify(self):
        if self.__speed > 100:
            print("High-speed Vehicle")
        else:
            print("Normal Vehicle")

    def show_info(self):
        print(self.name)
        print(self.type)
        print(self.__speed)
        print(self.classify())

class Car(Vehicle):
    def __init__(self, type, name, speed):
        super().__init__(type, name, speed)
        print(f"Car Added: {self.name}")

    def show_info(self):
        super().show_info()

class Bike(Vehicle):
    def __init__(self, type, name, speed):
        super().__init__(type, name, speed)
        print(f"Bike Added: {self.name}")

    def show_info(self):
        super().show_info()

t = int(input())

while t != 0:
    s = input().split()

    if s[0] == "Car":
        car1 = Car(s[0], s[1], int(s[2]))
        car1.show_info()
    else:
        bike1 = Bike(s[0], s[1], int(s[2]))
        bike1.show_info()

    t -= 1

