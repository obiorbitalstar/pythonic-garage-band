class Band:
    band_list = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        self.band_list.append(self)

    def play_solos(self, name):
        return [play_solos for member in self.members]

    def __str__(self):
        return f"band(name:{self.name},member:{self.members})"

    def __repr__(self):
        return f"'name':{self.name},'members' :{self.members}"


class Muscians:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Hi am {self.name}"


class Guitarest(Muscians):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Am {self.name}, i play Guitar"

    def __repr__(self):
        return f"Guitariest:{self.name} "

    def get_instrument(self):
        return f"Guitar"

    def play_solo(self):
        return f"Drrrrrrrrrrrrrrrn"
class Singer(Muscians):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f"Am {self.name},Am the singer"
    def __repr__(self):
        return f"Singer:{self.name}"
    def get_instrument(self):
        return "Larynx"
    def play_solo(self):
        return "AAAAAAAAAAAHHHHHHHHHHHHH"

class Bassist(Muscians):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f"Am {self.name} , i play the bass"
    def __repr__(self):
        return f"Bassist:{self.name}"
    def get_instrument(self):
        return "Bass"
    def play_solo(self):
        return f"breezy sounds"

class Drummer(Muscians):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f"Am {self.name}, i play the drums"
    def __repr__(self):
        return f"Drummer:{self.name}"
    def get_instrument(self):
        return "Drums"
    def play_solo(self):
       return f"Ba Dom Tss"

if __name__ == "__main__":
    bashar =Guitarest("Bashar")
    print(bashar.name)
    print(bashar.play_solo())
    print(bashar.get_instrument())
    samer = Bassist("Samer")
    print(samer.name)
    print(samer.play_solo())
    print(samer.get_instrument())
    saed = Drummer("Saed")
    print(saed.name)
    print(saed.play_solo())
    ahmad = Singer("Ahmad")
    print(ahmad.name)
    print(ahmad.play_solo())
    print(ahmad.get_instrument())
    band1 = (Band("Pandora Box", [ahmad,bashar, samer, saed]))
    for member in band1.members:
        print("Name: ", member.name)
        print("Member: ", member)
    print(band1.band_list)

