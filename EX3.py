class Rectangle:
    """defintion du class"""
    def __init__(self, longueur=10, largeur=6):
        self.lon = longueur
        self.lar = largeur
        self.nom = "rectangle"

    """La methode qui calcule la surface"""
    def surface(self):
        return self.lon * self.lar

    def __str__(self):
        # Affichage des caracteristiques d'un rectangle
        return ("\nLe {0} de côtes {1} et {2} a une surface de {3}"
                .format(self.nom, self.lon, self.lar, self.surface()))


class Carre(Rectangle):
    def __init__(self, cote=6):
        # Constructeur
        Rectangle.__init__(self, cote, cote)
        self.nom = "carre"


if __name__ == '__main__':
    r = Rectangle(3, 5)
    print(r)
    c = Carre()
    print(c)