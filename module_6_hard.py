import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides, filled=True):
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(r, g, b):
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                return True
            else:
                return False
        else:
            return False

    def set_color(self, r, g, b):
        if Figure.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *sides):
        if len(self.__sides) == len(sides):
            for side in sides:
                if not (isinstance(side, int) and side >= 0):
                    return False
            return True
        return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        p = 0
        for side in self.__sides:
            p += side
        return p

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count and self.__is_valid_sides(*new_sides):
            self.__sides = new_sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides, filled=True):
        if len(sides) == Circle.sides_count:
            self.__radius = sides[0] / (2 * 3.14)
            super().__init__(color, *sides, filled=filled)
        else:
            self.__radius = 1 / (2 * 3.14)
            super().__init__(color, 1, filled=filled)

    def get_square(self):
        return 3.14 * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides, filled=True):
        if len(sides) == Circle.sides_count:
            super().__init__(color, *sides, filled=filled)
        else:
            super().__init__(color, 1, 1, 1, filled=filled)

    def get_square(self):
        p = len(self) / 2
        sides = self.get_sides()
        return math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side, filled=True):
        sides = []
        if isinstance(side, int) and side >= 0:
            for i in range(Cube.sides_count):
                sides.append(side)
        else:
            for i in range(Cube.sides_count):
                sides.append(1)
        super().__init__(color, *sides, filled=filled)

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)# Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
