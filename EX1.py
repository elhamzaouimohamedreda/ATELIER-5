class Vecteur2D():
    """defintion du class"""
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y



v1 = Vecteur2D()
v2 = Vecteur2D(1,6)

# affichage des deux vecteurs
print("coordinates of v2: ","(",v2.x,",",v2.y,")")
print("coordinates of v1: ","(",v1.x,",",v1.y,")")