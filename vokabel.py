class Vokabel:
    def __init__(self, frage, antwort, kategorie, niveau):
        self.frage = frage
        self.antwort = antwort
        self.kategorie = kategorie
        self.niveau = niveau

    def pruefe_antwort(self, eingabe):
        return eingabe.lower() == self.antwort.lower()

    def in_dictionary_umwandeln(self):
        return {
            "frage": self.frage,
            "antwort": self.antwort,
            "kategorie": self.kategorie,
            "niveau": self.niveau
        }