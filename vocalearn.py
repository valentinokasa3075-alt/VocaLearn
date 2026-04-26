

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