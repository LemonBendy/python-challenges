class shapes:
    def __init__(self, fill_colour, outline_colour, outline_thickness):
        self.fill_colour = fill_colour
        self.outline_colour = outline_colour
        self.outline_thickness = outline_thickness

    def rotate(self, angle):
        print("Rotating by " + str(angle) + " degrees")

    def copy(self):
        print("Copying")

    def enlarge(self, percentage):
        print("Enlarging by a factor of " + str(percentage))

class circle(shapes):
    def __init__(self, fill_colour, outline_colour, outline_thickness, radius, centre):
        self.radius = radius
        self.centre = centre
        super().__init__(fill_colour, outline_colour, outline_thickness)

    def change_outline_colour(self, outline_colour):
        self.outline_colour = outline_colour

    def describe(self):
        print(f"This circle is {self.radius} and is {self.fill_colour} with a {self.outline_colour} outline")

class rectangle(shapes):
    def __init__(self, fill_colour, outline_colour, outline_thickness, length, width):
        self.length = length
        self.width = width
        super().__init__(fill_colour, outline_colour, outline_thickness)

    def add_text(self, text):
        print("Adding text: " + text)

    def describe(self):
        print(
            f'This rectangle is {self.length} by {self.width} and is {self.fill_colour} with a {self.outline_colour} outline')

circle_1 = circle("green", "red", 10, 3, (0, 0))
circle_2 = circle("blue", "pink", 4, 5, (0,5))
rectangle_1 = rectangle("green", "yellow", 6, 5, 3)
rectangle_2 = rectangle("brown", "blue", 3, 10, 5)

circle_1.enlarge(self, 50)
rectangle_1.rotate(self, 30)
rectangle_1.add_text(self, "I am using OOP")
circle_2.change_outline_colour(self, "purple")

print(circle_1.describe())
print(circle_2.describe())
print(rectangle_1.describe())
print(rectangle_2.describe())
