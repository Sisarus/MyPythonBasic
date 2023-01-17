numbers = [1,2,3,4, -1, 0, ["A", "B"]]
print(numbers)
print(numbers[6])
print(numbers[6][1])

print(" ")

numbers = [1, 2, 3, 4, -1, 0]

numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(" ")
numbers.append(1000)
print(len(numbers))
print(numbers)

numbers.clear()
print(numbers)

print(" ")

numbers = [1, 1, 2, 3, 4, -1, 0]
print(3 in numbers)
print(numbers)
numbers.remove(1)
print(numbers)

numbers = [ 1, 2, 3, 4, -1, 0]
del numbers[0]
print(numbers)

numbers = [1, 2, 3, 4, -1, 0]
del numbers[0:3]
print(numbers)

