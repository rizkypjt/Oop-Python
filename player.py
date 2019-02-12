class Player:
    name = 'Mbappe'

    def getName(self):
        return self.name

#di luar class

pemain = Player()

#cara pertama
print(pemain.name)

#cara kedua
print (pemain.getName())