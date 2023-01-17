import keyword
name, age = "Camilla", 20
PI = 3.14
number = 2
numnbers = [1, 2, 3, 4]
isAdult = True
isAdults: bool = True
nameFin: str = "Kaisa"

"""
Loot!
A comment!
"""


def hello() -> str:
    return "Hi!"

# I am a comment
# a second comment
# third comment


def hello2():
    return 1


print(name)
print(age)
print(numnbers)
fullName = "J James"

print(type(name))
print(type(age))
print(type(numnbers))
print(type(PI))
print(type(isAdult))
print(hello)
print(hello2)

print(name.upper())
print(name.replace('C', 'c'))
print(len(name))
print(name == "Camilla")
print('code' in name)
print('code' not in name)

email = """
Hello {},
How are you?
It was nice talking to you
Yeah
"""
print(email.format(name))

emailTwo = f"""
Hello {name},
How are you?
It was nice talking to you
Yeah age {4+4}
"""
print(emailTwo)

# identation


def myFunction():
    name = "Timo"
    surname = "Dance"


# Reserved Keywords


print(keyword.kwlist)
