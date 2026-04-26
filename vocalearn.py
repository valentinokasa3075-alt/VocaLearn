# Hauptprogramm für den Vokabeltrainer VocaLearn
# Dieses Programm ermöglicht es, Vokabeln zu speichern und im Quiz zu lernen


# Funktion: Neue Vokabel hinzufügen
def neue_vokabel_hinzufuegen():
    # Benutzer gibt eine neue Frage (z.B. deutsches Wort) ein
    frage = input("Gib das Wort oder die Frage ein: ")
    
    # Benutzer gibt die passende Antwort ein (z.B. Übersetzung)
    antwort = input("Gib die richtige Antwort ein: ")
    
    # Benutzer wählt eine Kategorie (z.B. Englisch oder Französisch)
    kategorie = input("Gib eine Kategorie ein (z.B. Englisch, Französisch): ")

    # Vorhandene Vokabeln aus der JSON-Datei laden
    vokabeln = lade_vokabeln()

    # Neue Vokabel als Objekt der Klasse "Vokabel" erstellen
    neue_vokabel = Vokabel(frage, antwort, kategorie)

    # Objekt wird in ein Dictionary umgewandelt und zur Liste hinzugefügt
    vokabeln.append(neue_vokabel.in_dictionary_umwandeln())

    # Aktualisierte Vokabelliste wieder in die Datei speichern
    speichere_vokabeln(vokabeln)

    print("Vokabel wurde gespeichert.")

# Hauptprogramm für VocaLearn

# Funktion: Hauptmenü anzeigen und steuern
def hauptmenue():

    while True:

        # Menü wird angezeigt
        print("\n--- VocaLearn ---")
        print("1 - Neue Vokabel hinzufügen")
        print("2 - Lernen starten")
        print("3 - Programm beenden")

        auswahl = input("Bitte wählen: ")

        # Je nach Eingabe wird eine Funktion ausgeführt
        if auswahl == "1":
            neue_vokabel_hinzufuegen()

        elif auswahl == "2":
            lernen_starten()

        elif auswahl == "3":
            print("Programm beendet.")
            break

        else:
            print("Ungültige Eingabe.")


# Startpunkt des Programms
# Dieser Teil sorgt dafür, dass das Menü gestartet wird
if __name__ == "__main__":
    hauptmenue()