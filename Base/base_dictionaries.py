person = {
    "name": "Kalle",
    "age": 20,
    "address": "FIN"
}
print(person)
print(person["name"])
print(person["age"])
print(person["address"])
print(person.keys())
print(person.values())

print(person.get("age"))

person["age"] = 100

print(person["age"])

person.clear()
print(person)
