from Animal import Animal
from Canivore import Carnivore
from CarnivoreSauvage import CarnivoreSauvage

if __name__=='__main__':
    animal=Animal("lion","brun","masculin","marche")
    animal.manger()
    print(animal.genre)