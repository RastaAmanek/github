
class Cow:

    def __init__(self, cow_name, cow_age=0):
        self.name = cow_name
        self.age = cow_age
        self.alive = True

    def give_a_voice(self, suffix="Muuuu......"):
        if self.alive is True:
            print(f"Muuuuu... {suffix}")
        else:
            print("R.I.P")

    def run(self):
        print("zapierdalam")

    def kill_yourself(self):
        self.alive = False
        print("umieram")

    def turn_on_the_light(self, lamp):
        lamp.turn_on()


class Cat:

    def __init__(self, cat_name, cat_age=0):
        self.name = cat_name
        self.age = cat_age
        self.alive = True

    def give_a_voice(self):
        print("Miauuu...")

    def catch_mause(self):
        print("mhm")
        print("jedna mysz mniej")


class Lamp:

    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False


cow_1 = Cow("Kurwka")
cow_1.give_a_voice()
cow_1.run()
print(cow_1.name, cow_1.age)
cow_1.kill_yourself()
cow_1.give_a_voice()

cow_2 = Cow("Milka", 5)
cow_2.give_a_voice("chuj Ci w dupe cwelu")
cow_2.run()
print(cow_2.name, cow_2.age)

cat_1 = Cat("Cholera", 2)
cat_1.give_a_voice()
cat_1.catch_mause()
print(cat_1.name, cat_1.age)

lamp_1 = Lamp()
print(lamp_1.is_on)
cow_2.turn_on_the_light(lamp_1)
print(lamp_1.is_on)
