name = "Kamilla"
name = "Oona"

print(name)

number = 4
number += 10
print(number)

number **= 10
print(number)

number = 15
if number > 0:
    print(f"number {number} is positive")
else:
    print(f"number {number} is negative")

number = -5
if number > 0:
    print(f"number {number} is positive")
else:
    print(f"number {number} is negative")

number = 0
if number > 0:
    print(f"number {number} is positive")
elif number == 0:
    print(f"number {number} is Zero")
else:
    print(f"number {number} is negative")


number = 2
message = "positive" if number > 0 else "zero or negative"

print(message)

lista = [3,5,2,8,1]
loytyi = False
for x in lista:
    if x%2 == 0:
        print("löytyi parillinen", x)
        loytyi = True
        break
if not loytyi:
    print("ei löytynyt parillista")

 def testi(*lista):
    print("Annoit", len(lista), "parametria")
    print("Niiden summa on", sum(lista))

testi(1, 2, 3, 4, 5)
