def creerPileVide():
    return []

def estVide(pile:[])->bool:
    return taille(pile)==0

def empiler(pile:[],element):
    pile.append(element)
    
def depiler(pile):
    if(not estVide(pile)):
        element = pile[taille(pile)-1]
        del pile[taille(pile)-1]
        return element
        # Solution alternative:
        # return pile.pop(len(pile)-1)
        
def taille(pile):
    return len(pile)