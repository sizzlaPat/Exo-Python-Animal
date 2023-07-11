from abc import ABC,abstractmethod
class Animal:
    
    def __init__(self,nom,couleur,genre,deplacement) :
        self.genre = genre
        self.couleur = couleur
        self.nom = nom
        self.deplacement=deplacement
    @abstractmethod
    def manger(self): 
       pass

    def deplacer(self):
        print(" je marche")

  #  def display(self):