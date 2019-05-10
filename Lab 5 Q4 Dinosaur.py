class Dinosaurs:
    def __init__(self, First_Name, Kingdom, Phylum, Last_Name='Dinosaurs', eyelids=False):
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.Kingdom = Kingdom
        self.Phylum = Phylum
        self.eyelids = eyelids


class Saurischian(Dinosaurs):
    Saurischian = "lizard-Type dinosaurs"


class Sauropoda(Saurischian):
    def Eat(self):
        print("They are Herbivoreous, So they eat Plants")

    def Size(self, Length, Height, Weight):
        self.Length = Length
        self.Height = Height
        self.Weight = Weight


class Theropoda(Saurischian):
    def Eat(self):
        print("They are Herbivoreous")

    def Size(self, Length, Height, Weight):
        self.Length = Length
        self.Height = Height
        self.Weight = Weight

class Ornithopoda(Dinosaurs):
        Saurischian = "Bird-Type dinosaurs"

class Thyreophora(Ornithopoda) :
    def Eat(self):
         print("They are Carnivoreous, So they est meat")

    def Size(self, Length, Height, Weight):
         self.Length = Length
         self.Height = Height
         self.Weight = Weight

class Cerapoda(Saurischian):
    def Eat(self):
         print("They are Carnivoreous, So they est meat ")

    def Size(self, Length, Height, Weight):
         self.Length = Length
         self.Height = Height
         self.Weight = Weight

# a = Dinosaurs("accc","c","d","e")
#
# print(a.First_Name + " " + a.Last_Name)


b = Saurischian('Saurischian','Animalia','Chordata')
print(b.First_Name + " " + b.Last_Name)
print(b.Kingdom)
print(b.Phylum)

c = Sauropoda("Sauropoda",'Animalia','Chordata')
print(c.First_Name + " " + b.Last_Name)
print("Their Kingdom is {}: ".format(c.Kingdom))
print("Their Phylum is {}: ".format(c.Phylum))
c.Eat()
c.Size("5 to 6","39–52","175 to 220 tonnes")
print("They are {} meter High".format(c.Height))
print("They have weight arround {} ".format(c.Weight))
print("Their Length is {} in meters :".format(c.Length))

