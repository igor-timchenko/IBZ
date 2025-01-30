import re
import math
class Line:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
    def length(self):
        return math.sqrt((self.x1 - self.x0) ** 2 + (self.y1 - self.y0) ** 2)
    def __str__(self):
        return f"Line: ({self.x0}, {self.y0}) to ({self.x1}, {self.y1}), Length: {self.length()}"
class Circle:
    def __init__(self, centerX, centerY, radius):
        self.centerX = centerX
        self.centerY = centerY
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
    def __str__(self):
        return f"Circle: Center ({self.centerX}, {self.centerY}), Radius: {self.radius}, Area: {self.area()}"
def parse_line(line_str):
    match = re.match(r"Line:s*(-?d*.?d*);(-?d*.?d*);(-?d*.?d*);(-?d*.?d*)", line_str)
    if match:
        x0, y0, x1, y1 = map(float, match.groups())
        return Line(x0, y0, x1, y1)
    return None
def parse_circle(circle_str):
    match = re.match(r"Circle:s*(-?d*.?d*);(-?d*.?d*);(-?d*.?d*)", circle_str)
    if match:
        centerX, centerY, radius = map(float, match.groups())
        return Circle(centerX, centerY, radius)
    return None
def main():
    shapes = []
    try:
        with open('shapes.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith("Line:"):
                    shape = parse_line(line)
                    if shape:
                        shapes.append(shape)
                elif line.startswith("Circle:"):
                    shape = parse_circle(line)
                    if shape:
                        shapes.append(shape)
    except FileNotFoundError:
        print("Файл не найден.")
        return
    # Сортировка по длине для линий и площади для окружностей
    shapes.sort(key=lambda shape: shape.length() if isinstance(shape, Line) else shape.area())
    # Вывод результата
    for shape in shapes:
        print(shape)
if __name__ == "__main__":
    main()
