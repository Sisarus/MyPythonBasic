def greet(name, age = -1):
    print(f"Hello {name} how are you?")
    if age >= 0:
        print(f"I know your age = {age}")

name = "Jaakko"
age = 2
greet(name, age)
greet("Pirpana", 52)
greet("Annali")
