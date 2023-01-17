names = ["Liisa", "Jyrki", "Heikki", "Tiina"]

for name in names:
    print(name)

print()

person = {
    "name": "Kalle",
    "age": 20,
    "address": "FIN"
}

for key in person:
    print(f"key: {key} value: {person[key]}")
print()
for key, value in person.items():
    print(f"key: {key} value: {value}")
