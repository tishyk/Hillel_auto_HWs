
# Write Abstract class Figure
#
# Inherit Triangle and Round from it
#
# Create a collection of Figures, count perimeter and square of them


from abc import ABC, abstractmethod
class Figure(ABC):
    def __init__(self, mesure_of_length, figure_name):
        self.mesure_of_length = mesure_of_length
        self.figure_name = figure_name
    @abstractmethod
    def get_square(self):
        pass
    @abstractmethod
    def get_perimeter(self):
        pass


class Square(Figure):
    def __init__(self, side, mesure_of_length, figure_name):
        super().__init__(mesure_of_length, figure_name)
        self.side = side

    def get_square(self):
        print(f'Square of {self.figure_name} is {self.side ** 2} {self.mesure_of_length}')
    def get_perimeter(self):
         print(f'Perimeter of {self.figure_name} is {self.side * 4} {self.mesure_of_length}')
    def __str__(self):
         print(f"side - {self.side} {self.mesure_of_length}")
class Triangle(Figure):
    def __init__(self, side, mesure_of_length, figure_name):
        super().__init__(mesure_of_length, figure_name)
        self.side = side

    def get_square(self):
        print(f'Square of {self.figure_name} is {self.side ** 2} {self.mesure_of_length}')
    def get_perimeter(self):
        print(f'Perimeter of {self.figure_name} is {self.side * 4} {self.mesure_of_length}')
    def __str__(self):
        print(f"side - {self.side} {self.mesure_of_length}")
class Round(Figure):
    def __init__(self, side, mesure_of_length, figure_name):
        super().__init__(mesure_of_length, figure_name)
        self.side = side

    def get_square(self):
         print(f'Square of {self.figure_name} is {self.side ** 2} {self.mesure_of_length}')
    def get_perimeter(self):
        print(f'Perimeter of {self.figure_name} is {self.side * 4} {self.mesure_of_length}')
    def __str__(self):
         print(f"side - {self.side} {self.mesure_of_length}")


square = Square(5, "sm", "square")
circle = Round(8, "sm", "circle")
triangle = Triangle(10, "sm", "triangle")

list_of_figure: [Figure] = [square, circle, triangle]
for fug in list_of_figure:
    fug.get_perimeter()
    fug.get_square()


# square2 = Square(20, "km")
# print(f"{square1.side} {square1.mesure_of_length}")
# print(f"{square2.side} {square2.mesure_of_length}")

# from abc import ABC, abstractmethod
#
# class Animal(ABC):
#     def __init__(self, heads_count, paw_count):
#         self.heads_count = heads_count
#         self.paw_count = paw_count
#
#     def get_a_battle_roar(self):
#         pass
#     @abstractmethod
#     def bite(self):
#         pass
# class Cat(Animal):
#     def __init__(self, heads_count, paw_count, tail, claws_count, cat_name):
#         super().__init__(heads_count, paw_count)
#         self.tail = tail
#         self.claws = claws_count
#         self.cat_name = cat_name
#
#     def get_a_battle_roar(self):
#         return print("MEEEEEO")
#
#     def bite(self):
#         print(f"{self.cat_name} wish {self.tail} is doing a Kus")
#
# class Dog(Animal):
#     def __init__(self, heads_count, paw_count, tail, claws_count, dog_name):
#         super().__init__(heads_count, paw_count)
#         self.tail = tail
#         self.claws = claws_count
#         self.dog_name = dog_name
#
#     def get_a_battle_roar(self):
#         return print("ArGGG")
#
#     def bite(self):
#         print(f"{self.dog_name} wish {self.tail} have cut your leg")
#
# barsik = Cat(heads_count=1, paw_count=4, claws_count=18, tail="BIG PUSHISTY TAIL", cat_name="Barsik")
# bobik = Dog(heads_count=1, paw_count=4, claws_count=18, tail="BIG PUSHISTY TAIL", dog_name="Bobik")
#
#
#
# list_of_animals: [Animal] = [barsik, bobik]
# for animal in list_of_animals:
#     animal.bite()