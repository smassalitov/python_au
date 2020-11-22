import sys


class Triangle:
    def __init__(self, a, b, c):
        self.l1 = Segment(a, b)
        self.l2 = Segment(b, c)
        self.l3 = Segment(a, c)

    def get_per(self):
        return self.l1.get_length() + self.l2.get_length() + self.l3.get_length()

    def get_square(self):
        half_per = self.get_per()
        return (half_per * (half_per - self.l1.get_length()) * (half_per - self.l1.get_length()) *
                (half_per - self.l1.get_length())) ** 0.5

    def is_triangle(self):
        return self.l1.get_length() + self.l2.get_length() > self.l3.get_length() and \
                self.l1.get_length() + self.l3.get_length() > self.l2.get_length() and \
                self.l2.get_length() + self.l3.get_length() > self.l1.get_length()

    def is_isosceles(self):
        return self.l1.get_length() == self.l2.get_length() \
                or self.l2.get_length() == self.l3.get_length() \
                or self.l1.get_length() == self.l3.get_length()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Segment:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_length(self):
        return ((self.a.x - self.b.x) ** 2 + (self.a.y - self.b.y) ** 2) ** 0.5


def len_check(line):
    if len(line) != 6:
        return False
    for i in line:
        try:
            int(i)
        except ValueError:
            return False
    return True


def set_squares(all_lines):
    index = 0
    all_squares = []
    for line in all_lines:
        if len_check(line.split()):
            x1 = int(line.split()[0])
            y1 = int(line.split()[1])
            x2 = int(line.split()[2])
            y2 = int(line.split()[3])
            x3 = int(line.split()[4])
            y3 = int(line.split()[5])
            point1 = Point(x1, y1)
            point2 = Point(x2, y2)
            point3 = Point(x3, y3)
            triangle = Triangle(point1, point2, point3)
            if triangle.is_triangle() and triangle.is_isosceles():
                all_squares.append((triangle.get_square(), index))
        index += 1
    return all_squares


def get_biggest_square(all_squares):
    max_square = -1
    max_line_number = -1
    for square in all_squares:
        if list(square)[0] > max_square:
            max_square = list(square)[0]
            max_line_number = list(square)[1]
    return max_line_number, max_square


def main():
    fin = open(sys.argv[1], 'r')
    fout = open(sys.argv[2], 'w')
    all_lines = fin.read().splitlines()
    max_line_number, max_square = get_biggest_square(set_squares(all_lines))
    if max_line_number != -1:
        print(all_lines[max_line_number], file=fout)


if __name__ == "__main__":
    main()
