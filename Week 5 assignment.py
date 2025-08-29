# Base class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery = battery  # in mAh

    def make_call(self, number):
        print(f"{self.brand} {self.model} is calling {number} 📞")

    def charge(self, amount):
        self.battery += amount
        print(f"{self.brand} {self.model} charged to {self.battery}mAh 🔋")

# Derived class - Inheritance
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, cooling_system):
        super().__init__(brand, model, storage, battery)
        self.cooling_system = cooling_system

    # Polymorphism: Overriding a method
    def charge(self, amount):
        super().charge(amount)
        print(f"{self.brand} {self.model} is optimized for gaming while charging 🎮")

# Creating objects
phone1 = Smartphone("Samsung", "Galaxy S23", 256, 4000)
phone2 = GamingPhone("Asus", "ROG Phone 7", 512, 6000, "Advanced Liquid Cooling")

# Using methods
phone1.make_call("08012345678")
phone2.charge(500)
               
