# Importe für Vokabeltrainer (Klasse, Datenbank und Zufall)

import random
from vokabel import Vokabel
from datenbank import lade_vokabeln, speichere_vokabeln


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


    # Funktion: Lernmodus starten
def lernen_starten():

    # Alle gespeicherten Vokabeln laden
    vokabeln = lade_vokabeln()

    # Wenn keine Vokabeln vorhanden sind, wird das Programm abgebrochen
    if len(vokabeln) == 0:
        print("Keine Vokabeln vorhanden.")
        return
    
    print("\nVerfügbare Kategorien:")

    kategorien = []

    # Alle vorhandenen Kategorien aus den Vokabeln sammeln (ohne Duplikate)
    for vokabel in vokabeln:
        if vokabel["kategorie"] not in kategorien:
            kategorien.append(vokabel["kategorie"])

    # Kategorien nummeriert anzeigen
    for i, kategorie in enumerate(kategorien):
        print(f"{i+1} - {kategorie}")

    # Zusätzliche Option: alle Kategorien gleichzeitig lernen
    print(f"{len(kategorien)+1} - ALLE")

    # Benutzer wählt eine Kategorie aus
    auswahl = input("Wähle eine Kategorie (Nummer): ")

    try:
        auswahl = int(auswahl)

        # Wenn letzte Option gewählt wurde → alle Kategorien
        if auswahl == len(kategorien) + 1:
            gewaehlte_kategorie = "ALLE"
        else:
            # sonst gewählte Kategorie aus Liste nehmen
            gewaehlte_kategorie = kategorien[auswahl - 1]

    except:
        print("Ungültige Auswahl.")
        return

    gefilterte_vokabeln = []

    # Vokabeln nach gewählter Kategorie filtern
    for vokabel in vokabeln:
        if gewaehlte_kategorie == "ALLE" or vokabel["kategorie"] == gewaehlte_kategorie:
            gefilterte_vokabeln.append(vokabel)

    # Nur die gefilterten Vokabeln werden verwendet
    vokabeln = gefilterte_vokabeln

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