




class Car:
    color = "red"

    def setColor(self, color):
        print(self)
        self.color = color
        print(self.color)


myCar = Car()

myCar.setColor('blue')