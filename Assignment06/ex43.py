class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
            You do a dive roll into the Weapon Armory, crouch and scan
            the room for more Gothons that might be hiding. It's dead
            quiet, too quiet. You stand up and run to the far side of
            the room and find the neutron bomb in its container.
            here's a keypad lock on the box and you need the code to
            get the bomb out. If you get the code wrong 10 times then
            the lock closes forever and you can't get the bomb. The
            code is 3 digits.
            """))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
                The container clicks open and the seal breaks, letting
                gas out. You grab the neutron bomb and run as fast as
                you can to the bridge where you must place it in the
                right spot.
                """))
            return 'the_bridge'
        else:
            print(dedent("""
                The lock buzzes one last time and then you hear a
                sickening melting sound as the mechanism is fused
                together. You decide to sit there, and finally the
                Gothons blow up the ship from their ship and you die.
                """))
            return 'death'



class TheBridge(Scene):

    def enter(self):
        print(dedent("""
            You burst onto the Bridge with the netron destruct bomb
            under your arm and surprise 5 Gothons who are trying to
            take control of the ship. Each of them has an even uglier
            clown costume than the last. They haven't pulled their
            weapons out yet, as they see the active bomb under your
            arm and don't want to set it off.
            """))

        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
                In a panic you throw the bomb at the group of Gothons
                and make a leap for the door. Right as you drop it a
                Gothon shoots you right in the back killing you. As
                you die you see another Gothon frantically try to
                disarm the bomb. You die knowing they will probably
                blow up when it goes off.
                """))
            return 'death'

        elif action == "slowly place the bomb":
            print(dedent("""
                You point your blaster at the bomb under your arm and
                the Gothons put their hands up and start to sweat.
                You inch backward to the door, open it, and then
                carefully place the bomb on the floor, pointing your
                blaster at it. You then jump back through the door,
                punch the close button and blast the lock so the
                Gothons can't get out. Now that the bomb is placed
                you run to the escape pod to get off this tin can.
                """))

            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"


class EscapePod(Scene):

    def enter(self):
        print(dedent("""
            You rush through the ship desperately trying to make it to
            the escape pod before the whole ship explodes. It seems
            like hardly any Gothons are on the ship, so your run is
            clear of interference. You get to the chamber with the
            escape pods, and now need to pick one to take. Some of
            them could be damaged but you don't have time to look.
            There's 5 pods, which one do you take?
            """))

        good_pod = randint(1,5)
        guess = input("[pod #]> ")


        if int(guess) != good_pod:
            print(dedent(f"""
                You jump into pod {guess} and hit the eject button.
                The pod escapes out into the void of space, then
                implodes as the hull ruptures, crushing your body into
                jam jelly.
                """))
            return 'death'
        else:
            print(dedent(f"""
                You jump into pod {guess} and hit the eject button.
                The pod easily slides out into space heading to the
                planet below. As it flies to the planet, you look
                back and see your ship implode then explode like a
                bright star, taking out the Gothon ship at the same
                time. You won!
                """))

            return 'finished'

class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return 'finished'
