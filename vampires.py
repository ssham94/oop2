class Vampire:
    coven = []

    def __init__(self, vampire_name, vampire_age, coffin, drank_blood):
        self.name = vampire_name
        self.age = vampire_age
        self.in_coffin = coffin
        self.drank_blood_today = drank_blood

    def drink_blood(self):
        self.drank_blood_today = True

    def go_home(self):
        self.in_coffin = True

    @classmethod
    def create(cls, vampire_name, vampire_age, coffin, drank_blood):
        new_vamp = Vampire(vampire_name, vampire_age, coffin, drank_blood)
        cls.coven.append(new_vamp)
        return new_vamp

    @classmethod
    def sunrise(cls):
        alive = []
        for vampire in cls.coven:
            if vampire.drank_blood_today and vampire.in_coffin:
                alive.append(vampire)
        cls.coven = alive
    
    @classmethod
    def sunset(cls):
        for vampire in cls.coven:
            vampire.drank_blood_today = False
            vampire.in_coffin = False


stan = Vampire.create('Stan', 25, True, True)
ian = Vampire.create('Ian', 24, True, True)
aj = Vampire.create('Aj', 23, True, True)
victoria = Vampire.create('Victoria', 25, True, True)
simon = Vampire.create('Simon', 28, True, True)
edi = Vampire.create('Edi', 49, True, True)
carol = Vampire.create('Carol', 28, True, True)

for vampire in Vampire.coven:
    print(vampire.name) # Should print out names of all the vampires

# Testing the cases for the vampires
Vampire.sunset()
stan.drink_blood()
stan.go_home()
ian.drink_blood()
aj.drink_blood()
aj.go_home()
victoria.go_home()
Vampire.sunrise() # Should remove all vampires except "Stan" and "Aj"
print('')
for vampire in Vampire.coven:
    print(vampire.name) # Should print "Stan", "Aj"