"""
Make three classes:
Phone → has model and battery (default 100).


SmartPhone → inherits from Phone and adds operating system.


GamingPhone  → inherits from SmartPhone and adds cooling_system.
 Add a method start_game(name) that prints
 👉 "Playing <name> on <model>".



2. Make a class MobilePhone with:
model (public)


__battery (private, default 100)
 Add methods:


use() → reduce battery


charge() → increase battery (max 100)


get_battery() → show battery


Show that you can’t access __battery directly.


"""

class Phone:
    def __init__(self, model, battery = 100):
        self.model = model
        self.battery = battery

class SmartPhone(Phone):
    def __init__(self, model, battery, opeerating_system):
        super().__init__(model, battery)
        self.operating_system = opeerating_system

class GamingPhone(SmartPhone):
    def __init__(self, model, battery, opeerating_system, cooling_system):
        super().__init__(model, battery, opeerating_system)
        self.cooling_system = cooling_system

    def start_game(self, name):
        print(f"Playing {name} on {self.model}")

rog = GamingPhone("stripX",5000,"asus","liquid")
# print(rog.battery)
# print(rog.model)
# print(rog.cooling_system)
# print(rog.operating_system)
print(rog.start_game("fungame"))
