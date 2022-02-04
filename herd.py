from dinosaur import Dinosaur


class Herd:
    
    def __init__(self): # list of the dinosaurs
        
        self.herd = []
        self.herd_names = []
        self.create_herd()

    def create_herd(self): # void it needs to add dinosaurs to the overall list (team) of dinosaurs
        
        self.dino_1 = Dinosaur('Toby', 15)
        self.dino_2 = Dinosaur('Moo', 20)
        self.dino_3 = Dinosaur('Jaxson', 25)

        self.herd.append(self.dino_1)
        self.herd.append(self.dino_2)
        self.herd.append(self.dino_3)

        self.herd_names.append(self.dino_1.name)
        self.herd_names.append(self.dino_2.name)
        self.herd_names.append(self.dino_3.name)