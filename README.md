# VocaLearn

**Projektname:** VocaLearn

**Team:** Valentino, Erduan

## **Projektbeschreibung**

- **Kurz:** VocaLearn ist ein terminalbasierter Vokabeltrainer in Python zum Erstellen, Verwalten und Abfragen von Vokabeln (aktuell Englisch & Französisch).
- **Zweck:** Unterstützt gezieltes Wiederholen, fördert Lernfortschritte und dient als Praxisprojekt für OOP- und Datei-IO-Konzepte.

## **Minimalziel**

- **Vokabeleingabe:** Benutzer können Vokabeln inkl. Frage, Antwort, Kategorie und Niveau hinzufügen (`neue_vokabel_hinzufuegen()`).
- **Persistenz:** Speicherung und Laden aller Vokabeln in `vocalearn_data.json` über `datenbank.py`.
- **Lernmodus:** Zufällige Abfrage einer auswählbaren Anzahl Vokabeln mit sofortigem Feedback (`lernen_starten()`).
- **Auswertung:** Anzeige von richtig/falsch-Zählern und Trefferquote in Prozent; Speicherung der Statistik in `lernstatistik.csv`.

Diese Kernfunktionen sind vollständig implementiert und bilden die Basis des Programms.

## **Schnellstart**

1. Python 3 installieren.
2. Im Projektordner ausführen:

```bash
python3 vocalearn.py
```

3. Menü folgen: Vokabeln hinzufügen → Lernen starten → Statistik einsehen.

## **Erweiterungen (bereits umgesetzt)**

- **Kategorien-System:** Vokabeln sind kategorisiert (z.B. `Englisch`, `Französisch`). Der Benutzer kann eine Kategorie oder `ALLE` wählen.
- **Niveausystem:** Jede Vokabel trägt ein Niveau (`B1` oder `B2`); Filterung im Lernmodus ist möglich.
- **B1/B2-Filter:** Auswahl des gewünschten Niveaus vor dem Start der Abfrage.
- **Zufällige Fragenauswahl:** Auswahl von N zufälligen Vokabeln per `random.sample`.
- **Multiple-Choice-Modus:** Benutzer kann zwischen normalem Lernmodus und Multiple-Choice wählen; im Multiple-Choice-Modus werden drei zufällige falsche Antworten erzeugt und die Antwortmöglichkeiten per `random.shuffle()` gemischt.
- **Wiederholung falscher Antworten:** Falsch beantwortete Vokabeln werden am Ende nochmals abgefragt.
- **Vokabel löschen:** Interaktive Löschfunktion mit nummerierter Auswahl (`vokabel_loeschen()`).
- **CSV-Lernstatistik:** Lernergebnisse werden in `lernstatistik.csv` angehängt und zur Auswertung geöffnet.

## **Technische Umsetzung**

- **Sprache & Laufzeit:** Python 3, terminalbasiert.
- **Dateien und Verantwortlichkeiten:**
	- `vocalearn.py`: Hauptprogramm, Menü und Benutzerinteraktion.
	- `vokabel.py`: Klasse `Vokabel` mit Methoden `pruefe_antwort()` und `in_dictionary_umwandeln()`.
	- `datenbank.py`: Funktionen `lade_vokabeln()` und `speichere_vokabeln()` für JSON-IO.
	- `vocalearn_data.json`: Persistente Datendatei (Speicherformat JSON).
	- `lernstatistik.csv`: Aufgezeichnete Lernläufe (Richtig, Falsch, Trefferquote).

- **Konzepte & Muster:** OOP (Kapselung der Vokabeln), modulare Struktur, einfache CLI-Interaktion, Datei-IO (JSON/CSV), Schleifen & Validierung.

## **Programmablauf (Kurz)**

1. Programmstart → `hauptmenue()`.
2. Menü: Neue Vokabel hinzufügen, Vokabel löschen, Lernen starten, Beenden.
3. Bei Hinzufügen: Eingabe von Frage, Antwort, Kategorie, Niveau → Validierung → Speichern.
4. Beim Lernen: Kategorienliste anzeigen → Kategorie/Niveau wählen → Anzahl der Fragen wählen → Zufällige Auswahl → Abfrage.
5. Ergebnisse: Anzeige Richtig/Falsch, Trefferquote, Anfügen an `lernstatistik.csv` und Öffnen der CSV.
6. Falls Fehler: Falsch beantwortete Vokabeln werden sofort wiederholt.

## **Benutzerfunktionen (Detail)**

- **Neue Vokabel hinzufügen (`neue_vokabel_hinzufuegen`)**: Interaktive Eingabe, Validierung für Kategorie (`Englisch` oder `Französisch`) und Niveau (`B1` oder `B2`), Bestätigung vor Speichern.
- **Vokabel löschen (`vokabel_loeschen`)**: Nummerierte Anzeige aller Einträge, Auswahl per Index, Speichern nach Löschung.
- **Lernmodus (`lernen_starten`)**: Kategorieauswahl inkl. `ALLE`, Auswahl der Frageanzahl (5, 10, Alle), Niveau-Auswahl (B1/B2/Alle), Wahl zwischen normalem Lernmodus und Multiple-Choice, zufällige Auswahl per `random.sample`, sofortiges Feedback.

## **Eingabevalidierung & Benutzerfreundlichkeit**

- Validierung für Kategorie und Niveau bei der Eingabe (Akzeptierte Werte: `Englisch`, `Französisch`, `B1`, `B2`).
- Numerische Auswahl (z. B. bei Lösch- und Kategorienwahl) mit Fehlerbehandlung und freundlichen Fehlermeldungen.
- Bestätigungsabfrage vor dem finalen Speichern neuer Vokabeln, um Eingabefehler zu vermeiden.
- Prüfung auf doppelte Vokabeln, damit identische Einträge nicht mehrfach gespeichert werden.

## **OOP / Klassenstruktur**

- `Vokabel` (in `vokabel.py`):
	- Attribute: `frage`, `antwort`, `kategorie`, `niveau`.
	- Methoden: `pruefe_antwort(eingabe)` — fallunabhängiger Vergleich; `in_dictionary_umwandeln()` — serialisierbares Dict.

Die Klasse kapselt Daten und Validierungslogik, der Rest des Programms arbeitet mit Dictionary-Repräsentationen für einfache JSON-Serialisierung.

## **JSON Speicherung**

- Speicherung: `speichere_vokabeln(vokabeln)` schreibt die komplette Liste als JSON in `vocalearn_data.json`.
- Laden: `lade_vokabeln()` liest die Datei und liefert die Vokabelliste (leer, falls Datei fehlt oder fehlerhaft).
- Pfadhandling: `datenbank.py` verwendet den Ordner der Datei als Basis, sodass relative Pfade konsistent sind.
 - Falls die JSON-Datei noch nicht existiert, wird automatisch eine leere Liste zurückgegeben (`FileNotFoundError`), damit das Programm nicht abstürzt.

## **CSV Lernstatistik**

- Format: `Richtig,Falsch,Trefferquote` als Header (wird bei Neuanlage geschrieben).
- Jeder Lernlauf hängt eine neue Zeile an: z. B. `3,2,60.0%`.
- Datei: `lernstatistik.csv` wird nach dem Schreiben automatisch geöffnet (plattformabhängig).

## **Kategorien & Niveau-System**

- Kategorien sind validiert und auf die Werte `Englisch` und `Französisch` beschränkt.
- Niveau: Zwei feste Stufen `B1` und `B2`; Filter im Lernmodus ermöglicht gezieltes Training.

## **B1/B2 Filter**

- Im Lernmodus kann der Benutzer vor dem Start ein Niveau wählen: nur B1, nur B2 oder Alle. Die Liste der Vokabeln wird entsprechend gefiltert.

## **Wiederholung falscher Antworten**

- Nach dem ersten Durchlauf werden alle falsch beantworteten Vokabeln gesammelt und in einem zusätzlichen Durchgang noch einmal abgefragt, um gezieltes Wiederholen zu unterstützen.

## **Zufällige Fragenauswahl & Trefferquote**

- Fragen werden mit `random.sample()` zufällig ausgewählt, sodass Wiederholungen innerhalb eines Durchlaufs vermieden werden.
- Trefferquote wird als Prozentwert berechnet: $\text{Trefferquote} = \frac{Richtig}{Gesamt} \times 100$ und mit einer Nachkommastelle angezeigt.

## **Benutzeroberfläche / UI-Verbesserungen (CLI)**

- Klar strukturiertes Hauptmenü (`hauptmenue()`), Emojis zur lockeren Visualisierung und erklärende Texte für Optionen.
- Lesbare Darstellung der Kategorie- und Niveau-Informationen neben jeder Frage.
- Freundliche Fehlermeldungen und einfache, konsistente Eingabeaufforderungen.

## **Teamarbeit**

- **Valentino:** Hauptverantwortung für Programmlogik, JSON/CSV-Handling und Dokumentation.
- **Erduan:** Unterstützung bei Architektur, Testläufen, UI-Feinschliff und Code-Review.

## **Herausforderungen & Erkenntnisse**

- **Versionierung & Zusammenarbeit (Git/GitHub):** Umgang mit Branches, Staging, Pull/Push und gelegentlichen Merge-Konflikten erforderte klare Commit-Nachrichten und Abstimmung im Team; durch regelmässige Pulls und gezieltes Stashen wurden Konflikte reduziert.

- **Projektstruktur:** Die Aufteilung in mehrere Module (`vocalearn.py`, `vokabel.py`, `datenbank.py`) verbesserte Lesbarkeit und Wartbarkeit. Die modulare Struktur erleichterte spätere Erweiterungen und Tests.

- **Objektorientierung:** Die Einführung der Klasse `Vokabel` förderte das Verständnis für Kapselung und wiederverwendbare Methoden; dies vereinfacht Validierung und Serialisierung der Daten.

- **Datenpersistenz (JSON):** Arbeiten mit `vocalearn_data.json` machte Fehlerquellen wie fehlende Dateien und Encoding-Probleme sichtbar; robuste Lade-/Speicherfunktionen und UTF-8-Encoding verbesserten die Zuverlässigkeit.

- **Fehlerbehandlung & Validierung:** Validierung von Kategorien und Niveaus sowie defensives Parsen numerischer Eingaben verringerten Laufzeitfehler und verbesserten die Nutzerführung. Gezielte Fehlerbehandlung mit `ValueError` bei numerischen Benutzereingaben erhöht die Robustheit und erlaubt präzisere Fehlermeldungen.

- **Debugging & Logikfehler:** Kleinere Logikfehler wurden iterativ identifiziert und behoben; systematisches Testen einzelner Funktionen und gezieltes Logging beschleunigten die Fehlersuche.

- **Benutzerfreundlichkeit:** Durch klare Menüstrukturen, Bestätigungsabfragen und lesbare Ausgaben wurde die Bedienbarkeit deutlich verbessert.

Diese Erkenntnisse zeigen, wie wiederholte Tests, modulare Struktur und abgestimmte Teamprozesse die Codequalität und Wartbarkeit im Verlauf des Projekts erhöht haben.

## **Weiteres / ToDo**

- Weitere Tests zur Überprüfung der Programmfunktionen.
- Verbesserte Eingabevalidierung und Vermeidung von Fehleingaben.
- Weitere Komfortfunktionen für den Lernmodus und den Datenimport.
- Möglichkeit zur Bearbeitung bestehender Vokabeln direkt im Terminal.
- Fortschrittssystem mit Punkten oder Lernstufen zur Motivation und Nachverfolgung.
- GUI-Version mit grafischer Benutzeroberfläche als alternative Bedienoption.
- Unterstützung weiterer Sprachen und zusätzlicher Kategorien.
- Benutzerkonten mit individuellen Lernstatistiken und getrennten Profilen.

## **Fazit**

- VocaLearn ist ein schlanker, gut strukturierter Vokabeltrainer, der die wichtigsten Funktionen für einen produktiven Lernworkflow bietet: schnelle Eingabe, gezielte Abfrage, Fortschrittsaufzeichnung und Wiederholung von Fehlern.
- Das Projekt hat zentrale technische Grundlagen vertieft, insbesondere die Arbeit mit objektorientierter Programmierung, die Verwaltung von Daten mit JSON und CSV sowie die Zusammenarbeit über Git/GitHub.
- Die modulare Struktur in separaten Modulen (`vocalearn.py`, `vokabel.py`, `datenbank.py`) macht den Code wartbar und gut erweiterbar.
- Die Teamarbeit wurde durch klare Aufgabenverteilung und regelmäßige Abstimmung gestärkt; der Lernprozess war geprägt von iterativem Debugging und der Verbesserung der Benutzerführung.