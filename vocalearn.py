# Importe für Vokabeltrainer (Klasse, Datenbank und Zufall)

import random
import os

from vokabel import Vokabel
from datenbank import lade_vokabeln, speichere_vokabeln


# Hauptprogramm für den Vokabeltrainer VocaLearn
# Dieses Programm ermöglicht es, Vokabeln zu speichern und im Quiz zu lernen

# Funktion: Neue Vokabel hinzufügen
def neue_vokabel_hinzufuegen():
    # Benutzer gibt eine neue Frage (z.B. deutsches Wort) ein
    frage = input("Gib das Wort oder die Frage ein: ").strip()
    
    # Benutzer gibt die passende Antwort ein (z.B. Übersetzung)
    antwort = input("Gib die richtige Antwort ein: ").strip()
    
    # Benutzer wählt eine Kategorie (z.B. Englisch oder Französisch)
    kategorie = input("Gib eine Kategorie ein (z.B. Englisch, Französisch): ").strip()

    # Prüfen ob gültige Kategorie eingegeben wurde
    if kategorie != "Englisch" and kategorie != "Französisch":
        print("Ungültige Kategorie. Bitte Englisch oder Französisch eingeben.")
        return

    # Benutzer wählt ein Niveau (z.B. B1 oder B2)
    niveau = input("Gib ein Niveau ein (z.B. B1, B2): ").strip()

    # Prüfen ob gültiges Niveau eingegeben wurde
    if niveau != "B1" and niveau != "B2":
        print("Ungültiges Niveau. Bitte nur B1 oder B2 eingeben.")
        return

    # Benutzer überprüft die eingegebenen Daten vor dem Speichern
    print("\nBitte überprüfe deine Eingaben:")
    print("Frage:", frage)
    print("Antwort:", antwort)
    print("Kategorie:", kategorie)
    print("Niveau:", niveau)

    # Benutzer entscheidet, ob die Eingaben korrekt sind
    print("\nIst alles korrekt?")
    print("1 - Ja, speichern")
    print("2 - Nein, neu eingeben")

    bestaetigung = input("Bitte wählen: ").strip()

    # Falls die Eingaben falsch sind → Funktion neu starten
    if bestaetigung == "2":
        print("\nDie Vokabel wird erneut eingegeben.\n")
        neue_vokabel_hinzufuegen()
        return

    # Vorhandene Vokabeln aus der JSON-Datei laden
    vokabeln = lade_vokabeln()

    # Prüfen ob die Vokabel bereits existiert
    for vokabel in vokabeln:

        if (
        vokabel["frage"].lower() == frage.lower()
        and vokabel["antwort"].lower() == antwort.lower()
        and vokabel["kategorie"].lower() == kategorie.lower()
        and vokabel["niveau"].lower() == niveau.lower()
    ):

            print("Diese Vokabel existiert bereits.")
            return

    # Neue Vokabel als Objekt der Klasse "Vokabel" erstellen
    neue_vokabel = Vokabel(frage, antwort, kategorie, niveau)

    # Objekt wird in ein Dictionary umgewandelt und zur Liste hinzugefügt
    vokabeln.append(neue_vokabel.in_dictionary_umwandeln())

    # Aktualisierte Vokabelliste wieder in die Datei speichern
    speichere_vokabeln(vokabeln)

    print("Vokabel wurde erfolgreich gespeichert.")

# Funktion: Vokabel löschen
def vokabel_loeschen():

    # Gespeicherte Vokabeln laden
    vokabeln = lade_vokabeln()

    # Prüfen ob Vokabeln vorhanden sind
    if len(vokabeln) == 0:
        print("Keine Vokabeln vorhanden.")
        return

    print("\n--- Gespeicherte Vokabeln ---")

    # Alle Vokabeln nummeriert anzeigen
    for i, vokabel in enumerate(vokabeln):
        print(f"{i+1} - {vokabel['frage']} → {vokabel['antwort']} ({vokabel['kategorie']} | {vokabel['niveau']})")

    try:
        # Benutzer wählt Nummer der Vokabel
        auswahl = int(input("\nWelche Vokabel möchtest du löschen? "))

        # Prüfen ob gültige Nummer eingegeben wurde
        if auswahl < 1 or auswahl > len(vokabeln):
            print("Ungültige Nummer.")
            return

        # Gewählte Vokabel aus Liste löschen
        del vokabeln[auswahl - 1]

        # Aktualisierte Liste speichern
        speichere_vokabeln(vokabeln)

        print("Vokabel wurde erfolgreich gelöscht")

    except ValueError:
        print("Ungültige Eingabe.")

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
    auswahl = input("Wähle eine Kategorie (Nummer): ").strip()

    try:
        auswahl = int(auswahl)

        # Wenn letzte Option gewählt wurde → alle Kategorien
        if auswahl == len(kategorien) + 1:
            gewaehlte_kategorie = "ALLE"
        else:
            # sonst gewählte Kategorie aus Liste nehmen
            gewaehlte_kategorie = kategorien[auswahl - 1]

    except ValueError:
        print("Ungültige Auswahl.")
        return

    gefilterte_vokabeln = []

    # Vokabeln nach gewählter Kategorie filtern
    for vokabel in vokabeln:
        if gewaehlte_kategorie == "ALLE" or vokabel["kategorie"] == gewaehlte_kategorie:
            gefilterte_vokabeln.append(vokabel)

    # Nur die gefilterten Vokabeln werden verwendet
    vokabeln = gefilterte_vokabeln

    # Benutzer wählt Anzahl der Fragen
    print("\nWie viele Fragen möchtest du lernen?")
    print("1 - 5 Fragen")
    print("2 - 10 Fragen")
    print("3 - Alle Fragen")

    fragen_auswahl = input("Bitte wählen: ").strip()

    if fragen_auswahl == "1":
        anzahl_fragen = 5

    elif fragen_auswahl == "2":
        anzahl_fragen = 10

    elif fragen_auswahl == "3":
        anzahl_fragen = len(vokabeln)

    else:
        print("Ungültige Eingabe.")
        return

    # Falls weniger Vokabeln vorhanden sind als gewählt
    if anzahl_fragen > len(vokabeln):
        anzahl_fragen = len(vokabeln)

    # Benutzer wählt ein Niveau
    print("\nWelches Niveau möchtest du lernen?")
    print("1 - B1")
    print("2 - B2")
    print("3 - Alle")

    niveau_auswahl = input("Bitte wählen: ").strip()

    if niveau_auswahl == "1":
        gewaehltes_niveau = "B1"

    elif niveau_auswahl == "2":
        gewaehltes_niveau = "B2"

    elif niveau_auswahl == "3":
        gewaehltes_niveau = "ALLE"

    else:
        print("Ungültige Eingabe.")
        return

    gefilterte_niveaus = []

    # Vokabeln nach Niveau filtern
    for vokabel in vokabeln:
        if gewaehltes_niveau == "ALLE" or vokabel["niveau"] == gewaehltes_niveau:
            gefilterte_niveaus.append(vokabel)

    vokabeln = gefilterte_niveaus

    # Falls weniger Vokabeln vorhanden sind als gewählt
    if anzahl_fragen > len(vokabeln):
        anzahl_fragen = len(vokabeln)

    # Zufällige Auswahl der gewünschten Anzahl an Vokabeln
    vokabeln = random.sample(vokabeln, anzahl_fragen)

    # Zähler für richtige und falsche Antworten
    richtige = 0
    falsche = 0

    # Liste für falsch beantwortete Vokabeln
    falsche_vokabeln = []

    # Benutzer wählt den Lernmodus
    print("\nWelchen Lernmodus möchtest du verwenden?")
    print("1 - Normaler Lernmodus")
    print("2 - Multiple Choice")

    lernmodus = input("Bitte wählen: ").strip()

    if lernmodus != "1" and lernmodus != "2":
        print("Ungültige Eingabe.")
        return  

    # Haupt-Lernschleife
    for vokabel in vokabeln:

        # Frage wird angezeigt (inkl. Kategorie zur Orientierung)
        print(f"\nFrage ({vokabel['kategorie']} | {vokabel['niveau']}):", vokabel["frage"])
        antwort = input("Antwort: ").strip()

        # Aus Dictionary wird wieder ein Vokabel-Objekt erstellt
        aktuelle_vokabel = Vokabel(
            vokabel["frage"],
            vokabel["antwort"],
            vokabel["kategorie"],
            vokabel["niveau"]
        )

        # Überprüfung der Antwort mithilfe der Methode der Klasse
        if aktuelle_vokabel.pruefe_antwort(antwort):
            print("Richtig!")
            richtige += 1
        else:
            print("Falsch! Richtige Antwort:", aktuelle_vokabel.antwort)
            falsche += 1
            falsche_vokabeln.append(vokabel)

    # Ergebnis am Ende anzeigen
    print("\n===== Lernergebnis =====")
    print("Richtig:", richtige)
    print("Falsch:", falsche)

    # Gesamtanzahl der beantworteten Fragen berechnen
    gesamt = richtige + falsche

    # Trefferquote in Prozent berechnen
    prozent = (richtige / gesamt) * 100

    # Trefferquote im Terminal anzeigen
    print(f"Trefferquote: {prozent:.1f}%")

    # Prüfen, ob die Statistik-Datei bereits existiert
    datei_existiert = os.path.exists("lernstatistik.csv")

    # Statistik-Datei öffnen oder neu erstellen
    with open("lernstatistik.csv", "a", encoding="utf-8") as datei:
        
        # Falls die Datei neu ist → Überschriften hinzufügen
        if not datei_existiert:
            datei.write("Richtig,Falsch,Trefferquote\n")

        # Lernergebnis in die CSV-Datei speichern
        datei.write(f"{richtige},{falsche},{prozent:.1f}%\n")

    # Statistik-Datei automatisch öffnen
    if os.name == "nt":
        os.system("start lernstatistik.csv")
    else:
        os.system("open lernstatistik.csv")

    # Falls es falsche Antworten gab → nochmal üben
    if len(falsche_vokabeln) > 0:
        print("\n--- Wiederholung der falschen Antworten ---")

        for vokabel in falsche_vokabeln:

            print(f"\nFrage ({vokabel['kategorie']}):", vokabel["frage"])
            antwort = input("Antwort: ").strip()

            aktuelle_vokabel = Vokabel(
                vokabel["frage"],
                vokabel["antwort"],
                vokabel["kategorie"],
                vokabel["niveau"]
            )

            # Zweite Überprüfung
            if aktuelle_vokabel.pruefe_antwort(antwort):
                print("Stark! Beim zweiten Versuch richtig beantwortet 💪")
            else:
                print("Nicht schlimm 😄 Diese Vokabel braucht noch etwas Übung.")
                print("Richtige Antwort:", aktuelle_vokabel.antwort)

# Hauptprogramm für VocaLearn

# Funktion: Hauptmenü anzeigen und steuern
def hauptmenue():

    print("\n===================================")
    print("📚 Willkommen bei VocaLearn 📚")
    print("Lerne spielerisch Englisch und Französisch 😄")
    print("Viel Spass beim Lernen und Üben!")
    print("Entwickelt von Valentino & Erduan")
    print("===================================\n")

    while True:

        # Menü wird angezeigt
        print("1 - Neue Vokabel hinzufügen")
        print("2 - Vokabel löschen")
        print("3 - Lernen starten")
        print("4 - Programm beenden")

        auswahl = input("Bitte wählen: ").strip()

        # Je nach Eingabe wird eine Funktion ausgeführt
        if auswahl == "1":
            neue_vokabel_hinzufuegen()

        elif auswahl == "2":
            vokabel_loeschen()

        elif auswahl == "3":
            lernen_starten()

        elif auswahl == "4":
            print("Programm beendet.")
            break
        
        else:
            print("Ungültige Eingabe!")
# Startpunkt des Programms
# Dieser Teil sorgt dafür, dass das Menü gestartet wird
if __name__ == "__main__":
    hauptmenue()