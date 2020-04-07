class Dog:
    def __init__(self, name):
        self.name = name
        self.race = "cat"
        self.age = None
        self.owner = None
        self.favoriteToy = "ball"
        self.bestfriend = None

    def set_name(self, dogname):
        self.name = dogname

    def set_age(self, dogage):
        self.age = dogage

    def set_owner(self, dogowner):
        self.owner = dogowner


class Dog_daycare:
    def __init__(self, name):
        self.dagisNamn = name
        self.dogslist = []
        self.boss = "Simon"

    def add_dog(self, dog):
        self.dogslist.append(Dog(dog))

    def remove_dog(self, name):
        for i, dog in enumerate(self.dogslist):
            del self.dogslist[i]
            break
    def set_bossname(self, bossname):
        self.boss = bossname


def add_bestfriend(name, race):
    maxFriends = 1
    currentFriends = 0
    bestFriend = ""
    if bestFriend != "golden retriever" and currentFriends <= 1:
        newBestFriend = Dog(name)
        newBestFriend.race = race
        currentFriends += 1
    elif bestFriend == "golden retriever":
        newBestFriend = Dog(name)
        newBestFriend.race = race
        currentFriends += 1


def printAll():
    for x in range(0, len(dagis.dogslist)):
        print(dagis.dogslist[x].name + "\t" + str(dagis.dogslist[x].race)
              + "\t" + str(dagis.dogslist[x].owner) + "\t" + str(dagis.dogslist[x].age))


dagis = Dog_daycare("Vacker Tass")
print("Dogs in daycare:")
print(dagis.dogslist)


running = True
while running:
    print("Welcome to the " + dagis.dagisNamn + " daycare center")
    print("The owner of this facility is: " + dagis.boss)
    print("\nDogs currently in the facility are: ")
    printAll()
    print("\nWhat do you want to do? \n1. Add new dog \n2. Remove a dog \n3. Bossname \n4. Change dog name \n5. "
          "dogowner")

    choice = (input("Type the number of you choice"))
    if choice == str(1):
        dagis.add_dog("pan")
    elif choice == str(2):
        name = input("Insert name of dog you want to remove")
        dagis.remove_dog(name)
    elif choice == str(3):
        dagis.boss = input("insert bossname").capitalize()
    else:
        print("invalid")