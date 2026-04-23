class Vokabel:
    def __init__(self, frage, antwort, kategorie):
        self.frage = frage
        self.antwort = antwort
        self.kategorie = kategorie

    def pruefe_antwort(self, eingabe):
        return eingabe.lower() == self.antwort.lower()

    def in_dictionary_umwandeln(self):
        return {
            "frage": self.frage,
            "antwort": self.antwort,
            "kategorie": self.kategorie
        }