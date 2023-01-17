numberList = [1,1]
numbersSet = {1,1}
letterSet = {"A", "A", "B", "C", "C"}
print(numberList)
print(numbersSet)
print(letterSet)

lettersA = {"A", "B", "C", "D"}
lettersB = {"A", "E", "F"}
union = lettersA | lettersB
intersection = lettersA & lettersB
difference = lettersA - lettersB
print(f"Union = {union}")
print(f"Intersection = {intersection}")

print(f"Difference = {difference}")
