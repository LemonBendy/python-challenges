class pet(): # Class, defines the attributes and methods of an object
    def __init__(self, givenName, givenAge, givenNumber_of_legs): # Constructor, called when an object is created
        # initialise the attributes
        self.name = givenName
        self.age = givenAge
        self.number_of_legs = givenNumber_of_legs

    def get_name(self): # Method, defines the behaviour of an object
        return self.name

    def get_age(self):
        return self.age

    def get_number_of_legs(self):
        return self.number_of_legs

    def set_name(self, givenName):
        self.name = givenName

    def set_age(self, givenAge):
        self.age = givenAge

    def set_number_of_legs(self, givenNumber_of_legs):
        self.number_of_legs = givenNumber_of_legs


class cat(pet):
    def __init__(self, givenName, givenAge, givenNumber_of_legs, givenColour):
        self.colour = givenColour
        super().__init__(givenName, givenAge, givenNumber_of_legs)

    def get_colour(self):
        return self.colour

    def set_colour(self, givenColour):
        self.colour = givenColour


kato = cat("Kato", 3, 4, "Black")
kato.set_colour("Orange")
print(kato.get_colour())
