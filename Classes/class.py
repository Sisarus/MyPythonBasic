class Phone:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def call(self, phoneNumber):
        print(f"{self.brand} is calling {phoneNumber}")

    def __str__(self) -> str:
        return f"Brand = {self.brand} \n Price = {self.price}"


iphone = Phone("Iphone 7+", 300)
samsung = Phone("Samsung S20", 1400)

print(iphone.brand)  # property
print(iphone.price)  # property

iphone.call("999")  # behavior

print(iphone)
print(samsung)