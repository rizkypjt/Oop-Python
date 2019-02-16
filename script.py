class Parrot:

    #class attribute
    species = "bird"

    #instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

#inisiasi class Parrot
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

#access the class attribute

print("blu is a{}".format(blu.__class__.species))
print("woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))