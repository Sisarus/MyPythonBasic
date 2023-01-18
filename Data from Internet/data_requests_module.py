import requests  # https://requests.readthedocs.io/en/latest/

url = "https://official-joke-api.appspot.com/random_ten"
r = requests.get(url)

print(r.status_code)
data = r.text

jsonData = r.json()


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
