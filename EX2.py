class Vecteur2D:
    """defintion du class"""
    x = 0
    y = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    """defintion de la methode d'affichage"""
    def display(self):
        print("(", self.x, ", ", self.y, ")")

    """defintion de la methode d'ajouter"""
    def __add__(self, other):
        a = self.x + other.x
        b = self.y + other.y
        v = Vecteur2D(a, b)
        return v

"""initialiser les vecteur et faire la somme"""
vec = Vecteur2D()
vec2 = Vecteur2D(1, 1)
vec.x = 5
vec.y =10
vec.display()
vec2.display()
vec3 = vec + vec2
vec3.display()
