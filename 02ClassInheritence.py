


class Bird:
    name = "bird"

    def __init__(self):
        print("Bird is ready")

    def run(self, name, mode):
        self.name = name
        return "{} run {}".format(self.name, mode)


class AnimalSing:
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

class AnimalSwim:
    def swim(self, mode):
        return "{} swim {}".format(self.name, mode)

class AnimalDance:
    def swim(self):
        return "{} is now davcing".format(self.name)

class AnimalFly:
    def fly(self, mode):
        return "{} flies {}".format(self.name, mode)

class Parrot(Bird,AnimalDance,AnimalSing,AnimalFly):
    def speak(self):
        return "{} speaks like human".format(self.name)


myBird = Parrot()

print(myBird.run('parrot', 'fast'))