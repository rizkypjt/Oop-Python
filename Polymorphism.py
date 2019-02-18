class Paroot:

    def fly(self):
        print ("parrot cab fly")

    def swim(self):
        print("parrot can't swim")

class Penguin:

    def fly(self):
        print("penguin telah ada")

    def swim(self):
        print("penguin cant swim")

# common interface
def flying_test(bird):
    bird.fly()
    bird.swim()

#instantiate objects
blu = Paroot()
peggy = Penguin()

#passing pada projeck
flying_test(blu)
flying_test(peggy)