

# Parent class
class Organism:
    name = "Unknown"
    species = "Unknown"
    legs = None
    arms = None
    dna = "Sequence A"
    origin = "Unknown"
    carbon_based = True

    def information(self):
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin: {}\nCarbon Based: {}".format(self.name,self.species,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        return msg

# Child Class Instance
class Human(Organism):
    name = "MacGyver"
    species = "Homosapien"
    legs = 2
    arms = 2
    origin = "Earth"

    def ingenuity(self):
        msg = "\nCreates a deadly weapon with only a paper clip, and chewing gum."
        return msg

# another child class instance
class Dog(Organism):
    name = "Spot"
    species = "Canine"
    legs = 4
    arms = 0
    dna = "Sequence B"
    Origin = "Earth"

    def bite(self):
        msg = "\nEmits a low growling and bites the target"
        return msg

#another child instance
class Bacteria(Organism):
    name = "X"
    species = "Bacteria"
    legs = 0
    arms = 0
    dna = "Sequence C"
    origin = "Mars"

    def replication(self):
        msg = "\nThe cells begin to divide and mulitply into two separate organisms"
        return msg




if __name__ == "__main__":
    human = Human()
    print(human.information())
    print(human.ingenuity())

    dog = Dog()
    print(dog.information())
    print(dog.bite())

    bacteria = Bacteria()
    print(bacteria.information())
    print(bacteria.replication())
    
    
