from sys import exit

def snake_room():
    print("You look inside and the floor covered in snakes!")
    print(" Do you enter yes or no?")

    choice = input("> ")

    if choice == "yes":
        print("The snakes are not venomous and you find a trap door on the floor that leads to a basement.")
        basement()
    if choice == "no":
        print("A spider falls on your head and bites you and you die!")
        morgue()

def morgue():
    print("Your body is found and you recieve a proper burial.")
    exit(0)

def basement():
    print("You walk downstairs and see a room filled with diamonds! What do you do?")
    print("1. Take a few in your backpack")
    print("2. Return later to get them all")
    print("3. Go home and never mention it to anyone")

    choice = input("> ")

    if choice == "1":
        print("You are found by other robers and are killed")
        morgue()
    if choice == "2":
        print("You return later and retrieve all the diamonds")
        home()
    if choice == "3":
        print("You return home and never mention it to anyone ever agian!")
        life()

def home():
    print("You sell all the diamonds and make a fortune")
    print("unfortunately an enemy hears abnout your good fortune and invades your home")
    print("they kill you and stealing all your money.")
    morgue()

def life():
    print("You live happily ever after")
    print("You have a huge family and win the lottery and die of old age")
    morgue()

def start():
    print("You are walking in the woods and see an old abandonded house.  You walk up to the front door and open it.")
    snake_room()


start()
