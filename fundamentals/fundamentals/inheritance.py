class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.normal_citizen = True

    def greeting(self):
        print(f"Hi my name is {self.name}")
        return self

# person_one= Person("Bob Ross", 60)
# person_two= Person("Lucille Ball", 50)

person_one = Person("Dave Fleming", 30)

# child class
class Superstar(Person):
    def __init__(self, real_name, age, stage_name, catchphrase):
        super().__init__(real_name, age)
        self.stage_name = stage_name
        self.catchphrase = catchphrase
        self.normal_citizen = False

    def greeting(self):
        print(f"Hi my name is {self.stage_name})


superstar_one = Superstar("Paul David Hewsom", 61, "Bono", "It's a beautiful day")
superstar_two = Superstar("Stefani Joanne Angelina Germanotta", 35, "Lady Gaga", "I was born this way")
superstar_three = Superstar("Marshall Bruce Mathers III", 49, "Eminem", "Mom's Spaghetti")


superstar_one.greeting()
