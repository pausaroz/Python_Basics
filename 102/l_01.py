#Miasteczko Świętego Mikołaja
class SantaLand:
    name_of_land = "Santa's Land"
    
#people, animal
class Human_and_Elf:
    def __init__(self, name, gender, who, pleace_to_live):
        self.name = name
        self.gender = gender
        self.who = who
        self.pleace_to_live = pleace_to_live

    def __str__(self):
        return self.name

    def work(self, place_of_work):
        return f"I'm working at {place_of_work}"

    def eat(self):
        return "I'm drining and eating something delicius"

    def sleep(self):
        return "I'm sleeping for 8 hours"
        
    def private_life(self):
        return "Now I have time for myself"

    def pleace_to_live(self):
        return str(self.pleace_to_live)

class Reindeers(Human_and_Elf):

    def work(self, place_of_work):
        return f"I'm pulling the sleigh"

    def private_life(self):
        return f"Rest after work"
    
    def place(self, pleace):
        return f"Now, I'm at the {pleace}"
    

#buldings
class Build(SantaLand):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Name: {self.name}, Adress: {SantaLand.name_of_land}"

class House(Build):
    def __init__(self, name, number_of_house):
        super().__init__(name)
        self.number_of_house = number_of_house
        
    def __str__(self):
        return super().__str__() + ", number: " + str(self.number_of_house)

def create_live(tuple_names, gender, human_or_elf_or_reinder, name_house):
    all_create_live = []
    for name in tuple_names:
        someone = Human_and_Elf(name, gender, human_or_elf_or_reinder, name_house)
        all_create_live.append(someone)
    return all_create_live

        
# creating buildings; tworzenie budynków

#for human
santa_house = Build("Santa's residence")

#for elfs
houses_of_elve_man, hauses_of_elve_woman = [], []
for i in range(3_000):
    house1 = House(f"Red House", i)
    houses_of_elve_man.append(house1)
    house2 = House(f"Green House", i)
    hauses_of_elve_woman.append(house2)

#for reinnders
stable = Build("Stable")
reindeer_paddock = Build("reindeer paddock")

#for elf to work
gift_factory= Build("Factory of gift")

#creating someone live

#human
santa_claus = Human_and_Elf("Santa Claus", "men", "human", santa_house)
mrs_santa = Human_and_Elf("Mrs. Santa", "woman", "human", santa_house)

#reinders
name_reindeer_man = ("Pyszalek", "Tancerz", "Kometek", "Amorek", "Blyskawiczny", "Fircyk", "Profesorek", "Zlosnik", "Czerwononosy" )
name_reindeer_woman = ("Prancer", "Dancer", "Comet", "Cupid", "Blitzen", "Dasher", "Donner", "Vixen", "Rudolph")

reinder_man = create_live(name_reindeer_man, "man", "reinder", stable)
reinder_woman = create_live(name_reindeer_woman, "man", "reinder", stable)

#elve
elve_name = ("Elmo", "Annae", "Galdor", "Legolas", "Nellas", "Miloth", "ArithmeticError", "Oropher")

elve_man, elve_woman = [], []
for i in range(3_000):
    elve_man.append(create_live(elve_name, "man", "elf", houses_of_elve_man[i]))
    elve_woman.append(create_live(elve_name, "woman", "elf", hauses_of_elve_woman[i].name))

