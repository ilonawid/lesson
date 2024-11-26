class Figure:
    sides_count = 0


    def __init__(self, color, sides):
        self.__sides = sides
        self.__color = color
        self.filled = True

    def get_color(self):
        return self.__color

    def __is_valid_color(self, color):
        c = 0
        for i in color:
            if 0 < i < 255:
                c += 1
        if c == len(color):
            return True
        else:
            return False

    def set_color(self, color):
        res = self.__is_valid_color(color)
        if res is True:
            self.__color = list(color)
        else:
            self.__color = list(self.__color)
        return self.__color

    def __is_valid_sides(self, *sides):
        for side in sides:
            if side > 0 and len(sides) == self.__sides:
                return True
            else:
                return False

    def get_sides(self):
        res = []
        for i in range(0, self.sides_count):
            res.append(self.__sides)
        return res

    def __len__(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            for side in new_sides:
                self.__sides = side


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.radius = sides // (2 * 3.1415)

    def get_square(self):
        square = 3.1405 * self.radius ** 2
        return square


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, sides):
        super().__init__(color, sides)

    def get_square(self):
        perimetr = sum(self.__sides)
        square = (perimetr * (perimetr - self.__sides) * (perimetr - self.__sides) * (perimetr - self.__sides)) ** 0.5
        return square


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.sides = sides

    def get_volume(self):
        volume = self.sides ** 3
        return volume


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)

cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:

circle1.set_color((55, 66, 77))  # Изменится

print(circle1.get_color())

cube1.set_color((300, 70, 15))  # Не изменится
#
print(cube1.get_color())

# Проверка на изменение сторон:

cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится

print(cube1.get_sides())

circle1.set_sides(15)  # Изменится

print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:

print(len(circle1))

# Проверка объёма (куба):

print(cube1.get_volume())
