import sys,os,json
assert sys.version_info >= (3,8), "This script requires at least Python 3.8"

def load(l):
    f = open(os.path.join(sys.path[0], l))
    data = f.read()
    j = json.loads(data)
    return j

def find_passage(game_desc, pid):
    for p in game_desc["passages"]:
        if p["pid"] == pid:
            return p
    return {}



# ------------------------------------------------------

def update(current, game_desc, choice):
    if current == "":
        return current

    for l in current["links"]:
        if choice == l["name"].lower():
            current = find_passage(game_desc, l["pid"])
    return current

def render(current):
    #print("\nYou are at the " + current["name"])
    print(current["text"])

def get_input(current):
    choice = input("\nType the decision you would make, or type quit to stop: ")
    choice = choice.lower()
    os.system("printf '\033c'")
    if choice in ["quit","q","exit"]:
        return "quit"
    return choice

# ------------------------------------------------------

def main():
    game_desc = load("game.json")
    current = find_passage(game_desc, game_desc["startnode"])
    choice = ""

    while choice != "quit" and current != {}:
        current = update(current, game_desc, choice)
        render(current)
        choice = get_input(current)

    print("Thanks for playing!")

if __name__ == "__main__":
    main()