films = {
    "Star Wars":[12,5],
    "Braveheart":[9,3],
    "Frozen":[18,5]
    }

print("options are {}".format(", ".join(list(films.keys()))))

while True:
    choice = input("What film you want to know?").strip().title()
    if choice in films.keys():
        age = int(input("How old are you?").strip())
        if(age >= films[choice][0]):
            print("Price is {}".format(films[choice][1]))
            films[choice][1] = films[choice][1]-1
        else:
            print("TOO YOUNG")
    else:
        print("thats not an option")
