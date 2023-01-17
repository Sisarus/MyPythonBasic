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
