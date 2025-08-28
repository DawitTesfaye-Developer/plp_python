# Base class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery = battery  # in mAh

    def make_call(self, number):
        print(f"{self.brand} {self.model} is calling {number}... 📞")

    def take_photo(self):
        print(f"{self.brand} {self.model} takes a photo! 📸")

# Inheritance - subclass
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, cooling_system):
        super().__init__(brand, model, storage, battery)
        self.cooling_system = cooling_system

    def play_game(self, game):
        print(f"Playing {game} on {self.brand} {self.model} 🔥")
        print(f"Cooling system status: {self.cooling_system}")

# Create objects
phone1 = Smartphone("Samsung", "Galaxy S23", 256, 4000)
phone2 = GamingPhone("ASUS", "ROG Phone 7", 512, 6000, "Active Cooling")

phone1.make_call("0912345678")
phone1.take_photo()

phone2.make_call("0987654321")
phone2.play_game("Genshin Impact")
