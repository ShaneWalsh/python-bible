known_users = ["Adam", "Frank", "Joe", "Billy", "Bobby"]


print(len(known_users))

while True:
    print("Warning, I am alert")
    name = input("name Yo?:").strip().capitalize()
    if name in known_users:
        print("I Know you. Welcome {}".format(name))
        remove= input("Would you like to be removed? y/n").lower()
        if remove == "y":
            known_users.remove(name)
    else:
        print("I dont know you {}".format(name))
        add = input("Would you like to be registered {}?".format(name).lower())
        if add == "y":
            known_users.append(name)
        elif add == "n":
            print("Fine. Suit Yourself")
    print(known_users)

    
            
