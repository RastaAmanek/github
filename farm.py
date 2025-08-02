
class Cow:

    def __init__(self, cow_name, cow_age = 0):
        self.name = cow_name
        self.age = cow_age

    def give_a_voice(self, suffix):
        print(f"Muuuuu... {suffix}")

    def run(self):
        print("zapierdalam")


class Cat:

    def give_a_voice(self):
        print("Miauuu...")

    def catch_mause(self):
        print("mhm")
        print("jedna mysz mniej")


cow_1 = Cow("Kurwka")
cow_1.give_a_voice("chuj Ci w dupe cwelu")
cow_1.run()
print(cow_1.name, cow_1.age)

cow_2 = Cow("Milka", 5)
cow_2.give_a_voice("chuj Ci w dupe cwelu")
cow_2.run()
print(cow_2.name, cow_2.age)

cat_1 = Cat()
cat_1.give_a_voice()
cat_1.catch_mause()
