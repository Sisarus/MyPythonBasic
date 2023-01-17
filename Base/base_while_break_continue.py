number = 0

while number < 10:
    print(number)
    number += 1
else:
    print("while loop ended")

print()
number = 0
while number < 10:
    if number == 5:
        break
    number += 1
    print(number)

print()
number = 0
while number < 10:
    number += 1
    if number < 5:
        continue
    print(number)

print()
for n in [1, 2, 3, 4, 5]:
    if n < 5:
        continue
    print(n)

print()
for n in [1, 2, 3, 4, 5, 6, 7]:
    if n == 5:
        break
    print(n)
