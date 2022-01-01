class etudiant:
    def _init_(self, nom, prenom, age, cne, moyenne):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.cne = cne
        self.moyenne = moyenne

# list de type etudiant
etudiant = [
    {'nom': 'ELHAMZAOUI', 'prenom': 'MOHAMED', 'age': 20, 'cne': 234567, 'moyenne':15},
    {'nom': 'ELHAMZAOUI', 'prenom': 'AHMED', 'age': 38, 'cne': 345667, 'moyenne': 16},
]

# trie par age
print("\tListe triee par age :")
etudiant.sort(key=lambda x: x.get('age'))
print(etudiant)
# trie par moyenne
print("\n\tListe triee par moyenne :")
etudiant.sort(key=lambda x: x.get('moyenne'))
print(etudiant)