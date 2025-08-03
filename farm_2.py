
class Animal:

    def say_hi(self):
        print("Hi")


class Cow(Animal):
    pass


class Horse(Animal):
    pass


class Turtle(Animal):
    def say_hi(self):
        print("Hello")


class Chicken(Animal):
    def say_hi(self):
        super().say_hi()
        print("No I hello!")


# cow_1 = Cow()
# cow_1.say_hi()
#
# horse_1 = Horse()
# horse_1.say_hi()
#
# turtle_1 = Turtle()
# turtle_1.say_hi()

chicken_1 = Chicken()
chicken_1.say_hi()
