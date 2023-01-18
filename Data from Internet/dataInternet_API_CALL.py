from urllib import request
import json

url = "https://official-joke-api.appspot.com/random_ten"
r = request.urlopen(url)

print(r.getcode())
data = r.read()
jsonData = json.loads(data)
print(jsonData)


class Joke:

    def __init__(self, setup, punchline) -> None:
        self.setup = setup
        self.punchline = punchline

    def __str__(self) -> str:
        return f"setup {self.setup} punchline {self.punchline}"


jokes = []

for j in jsonData:
    setup = j["setup"]
    punchline = j["punchline"]
    joke = Joke(setup, punchline)
    jokes.append(joke)

print(len(jokes))

for joke in jokes:
    print(joke)
