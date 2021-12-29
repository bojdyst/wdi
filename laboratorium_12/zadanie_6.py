class Ground:
    def __init__(self, points):
        self.points = points  # self.zmienna daje dostęp całej klasie do tej zmiennej

    def print(self):
        print(self.points)

    def get_candidates(self, main_point):
        x = []
        y = []
        z = []  # potencjalny czwarty punkt
        for point in self.points:  # przechodzi przez punkty z tablicy punktów
            if point[0] == main_point[0] and point[1] != main_point[1]:
                y.append(point)
            elif point[1] == main_point[1]:
                x.append(point)
            else:
                z.append(point)
        return x, y, z

    def combination_of_arrays(self, horizontalX, verticalY):
        candidates = []
        for hx in horizontalX:
            for vy in verticalY:
                candidates.append((hx[0], vy[1]))
        return candidates

    def sorted_by_y(self, e):
        return e[1]

    def can_exist_rectangle(self, main_point, symetric_point):
        a = abs(main_point[0] - symetric_point[0])
        b = abs(main_point[1] - symetric_point[1])
        if a == b:
            return False

        for point in self.points:
            if max(main_point[0], symetric_point[0]) > point[0] > min(main_point[0], symetric_point[0]) and \
                    max(main_point[1], symetric_point[1]) > point[1] > min(main_point[1], symetric_point[1]):
                return False
        return True

    def is_rectangle_from_point(self, point):
        horizontalX, verticalY, others = self.get_candidates(point)  # horizontalX = x, verticalY = y, others = z
        potential_point = self.combination_of_arrays(horizontalX, verticalY)
        for potential in potential_point:
            if others.__contains__(potential) and self.can_exist_rectangle(point, potential):
                return True
        return False

    def is_rectangle(self):
        for point in self.points:
            if self.is_rectangle_from_point(point):
                return True
        return False


x1 = Ground([(-2, 2), (1, 1), (1, 6), (7, 1), (7, 6), (3, 3)])
x2 = Ground([(1, 6), (7, 7), (7, 18), (6, 31)])
x3 = Ground([(-52, 2), (-7, 1), (0, 1), (0, 10), (-7, 10), (-33, 3)])

print(x1.is_rectangle())
print(x2.is_rectangle())
print(x3.is_rectangle())