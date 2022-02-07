from dinosaur import Dinosaur


class Herd:
    
    def __init__(self): # list of the dinosaurs
        
        self.herd = []
        self.create_herd()

    def create_herd(self): # void it needs to add dinosaurs to the overall list (team) of dinosaurs
        
        self.dino_1 = Dinosaur('Toby the T-Rex', 25)
        self.dino_2 = Dinosaur('Moo the Meme-o-saurus', 50)
        self.dino_3 = Dinosaur('Triceratops Troy', 75)

        self.herd.append(self.dino_1)
        self.herd.append(self.dino_2)
        self.herd.append(self.dino_3)