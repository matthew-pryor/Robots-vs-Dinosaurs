from dinosaur import Dinosaur


class Herd:
    
    def __init__(self): # list of the dinosaurs
        
        self.herd = []
        self.create_herd()

    def create_herd(self): # void it needs to add dinosaurs to the overall list (team) of dinosaurs
        
        dino_1 = Dinosaur('Toby', 15)
        dino_2 = Dinosaur('Moo', 20)
        dino_3 = Dinosaur('Jaxson', 25)

        self.herd.append(dino_1)
        self.herd.append(dino_2)
        self.herd.append(dino_3)