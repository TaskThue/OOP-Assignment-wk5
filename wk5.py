# Base class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery
    
    def make_call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def charge(self, amount):
        self.battery += amount
        if self.battery > 100:
            self.battery = 100
        print(f"Battery charged to {self.battery}%")

    def __str__(self):
        return f"{self.brand} {self.model} - {self.storage}GB Storage, {self.battery}% Battery"


# Subclass (Inheritance + Polymorphism)
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery, cooling_system):
        super().__init__(brand, model, storage, battery)
        self.cooling_system = cooling_system

    def play_game(self, game):
        if self.battery > 10:
            self.battery -= 10
            print(f"Playing {game} 🎮 on {self.brand} {self.model}. Battery now {self.battery}%")
        else:
            print("Battery too low! Please charge the phone.")
    
    # Polymorphism: Override charge()
    def charge(self, amount):
        super().charge(amount)
        print(f"Cooling system '{self.cooling_system}' is active while charging.")

# Example Usage
phone1 = Smartphone("Samsung", "S23", 256, 80)
print(phone1)
phone1.make_call("0723456789")
phone1.charge(15)

gaming_phone = GamingSmartphone("Asus", "ROG 7", 512, 60, "Liquid Cooling")
print(gaming_phone)
gaming_phone.play_game("PUBG")
gaming_phone.charge(30)
