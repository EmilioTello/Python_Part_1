class Pet:
    def __init__(self, name, type, tricks, health, energy, sound):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        self.sound = sound

    def sleep(self):
        self.energy += 25
        return self
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    def play(self):
        self.health += 5
        return self
    def noise(self):
        print(self.sound)
        return self


class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    
    def walk(self):
        self.pet.play()
        print(f"{self.first_name} took {self.pet.name} for a walk.")
        print(f"{self.pet.name}'s health is now {self.pet.health}.")
        return self
    def feed(self):
        self.pet.eat()
        print(f"{self.first_name} fed {self.pet.name} some {self.pet_food}.")
        print(f"{self.pet.name}'s energy is now {self.pet.energy}.")
        print(f"{self.pet.name}'s health is now {self.pet.health}.")
        return self
    def bathe(self):
        print(f"As {self.first_name} bathed {self.pet.name}, {self.pet.name} said {self.pet.sound}!")
        return self



Dog_1 = Pet("Spot","Dog","Jumping", 85, 60, "Arf")

Fighter_1 = Ninja("Daniel","Larusso","Biscuits","Kibble", Dog_1)

Fighter_1.walk()
Fighter_1.feed()
Fighter_1.bathe()
