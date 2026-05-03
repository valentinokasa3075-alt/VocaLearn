# VocaLearn

## Projektname & Team

**Projektname:** VocaLearn

**Teammitglieder:**
- Valentino
- Erduan

## Projektbeschreibung

### Was
Entwicklung eines Vokabeltrainers mit Python. Das Programm ermöglicht die Speicherung und Abfrage von Lerninhalten, um Benutzern beim Erlernen von Vokabeln zu helfen.

### Wie
Das Programm ist textbasiert und läuft im Terminal. Die Daten werden in einer JSON-Datei gespeichert. Es verwendet objektorientierte Programmierung (OOP) mit Klassen zur Strukturierung des Codes.

### Warum
Der Vokabeltrainer unterstützt Benutzer beim effektiven Lernen von Vokabeln. Das Projekt dient der Anwendung und Vertiefung von Python-Kenntnissen sowie der Umsetzung eines realistischen Softwareprojekts.

## Ziel des Projekts

Das Hauptziel ist die Entwicklung eines funktionierenden Lernprogramms. Dabei sollen Python-Grundlagen angewendet, objektorientiertes Programmieren eingesetzt und eine strukturierte, erweiterbare Software erstellt werden.

## Minimalziel

Das Minimalziel umfasst die folgenden Kernfunktionen, die klar und detailliert umgesetzt wurden:

- **Vokabeln eingeben:** Benutzer können neue Vokabeln mit Übersetzungen über die Eingabeaufforderung hinzufügen.
- **Vokabeln speichern:** Alle eingegebenen Vokabeln werden automatisch in einer JSON-Datei gespeichert, um Datenpersistenz zu gewährleisten.
- **Vokabeln laden:** Beim Programmstart werden vorhandene Vokabeln aus der JSON-Datei geladen, sodass der Lernfortschritt erhalten bleibt.
- **Abfragemodus starten:** Ein dedizierter Modus zum Testen des Wissens, in dem Vokabeln abgefragt werden.
- **Antworten überprüfen:** Das Programm vergleicht die Benutzerantworten mit den gespeicherten korrekten Übersetzungen.
- **Ausgabe von richtig/falsch:** Sofortiges Feedback nach jeder Antwort, ob sie korrekt oder falsch ist.
- **Anzeige einer Auswertung:** Am Ende des Abfragemodus wird eine Zusammenfassung mit der Anzahl richtiger und falscher Antworten sowie einer prozentualen Bewertung angezeigt.

Diese Funktionen bilden die Basis des Programms und sind vollständig implementiert.

## Erweiterungen (Iteration / Weiterentwicklung)

### Bereits umgesetzte Erweiterungen

Über das Minimalziel hinaus wurden folgende Erweiterungen implementiert, um das Programm leistungsfähiger und benutzerfreundlicher zu machen:

- **Kategorien:** Unterstützung für verschiedene Sprachkategorien wie Englisch und Französisch, um das Lernen thematisch zu organisieren.
- **Mehrere Sprachen:** Möglichkeit, Vokabeln in verschiedenen Sprachen zu speichern und abzufragen.
- **"ALLE"-Modus:** Ein gemischter Lernmodus, in dem Vokabeln aus allen Kategorien zufällig abgefragt werden.
- **Wiederholung falscher Antworten:** Nach dem ersten Durchlauf werden nur die falsch beantworteten Vokabeln erneut abgefragt, um gezieltes Nachlernen zu ermöglichen.
- **Objektorientierte Umsetzung:** Verwendung einer dedizierten Klasse "Vokabel" zur Kapselung der Daten und Methoden.

Diese Erweiterungen zeigen, dass das Team über das Minimalziel hinaus gearbeitet und zusätzliche Funktionalitäten erfolgreich umgesetzt hat.

### Mögliche zukünftige Erweiterungen

Für die Weiterentwicklung des Projekts wurden folgende zusätzliche Erweiterungen identifiziert:

- **Grafische Benutzeroberfläche (GUI):** Entwicklung einer benutzerfreundlichen Oberfläche zur einfacheren Bedienung des Programms.
- **Lernstatistik:** Anzeige des individuellen Lernfortschritts, z.B. Anzahl richtiger und falscher Antworten über mehrere Durchläufe hinweg.
- **Multiple-Choice-Modus:** Alternative Abfragemethode mit vorgegebenen Antwortmöglichkeiten.
- **Erweiterung um weitere Sprachen:** Unterstützung zusätzlicher Sprachen zur Erweiterung des Einsatzbereichs.
- **Benutzerverwaltung:** Möglichkeit, mehrere Benutzer anzulegen und individuelle Fortschritte zu speichern.

Diese möglichen Erweiterungen zeigen, dass das Projekt flexibel aufgebaut ist und sich in Zukunft weiter ausbauen lässt.

## Technische Umsetzung

**Programmiersprache:** Python

**Datenformat:** JSON

**Struktur:**
- `vocalearn.py`: Enthält die Hauptlogik, das Menü und die Benutzerinteraktion.
- `vokabel.py`: Definiert die Klasse "Vokabel" für die Datenstruktur.
- `datenbank.py`: Behandelt das Laden und Speichern der Daten in die JSON-Datei.
- `vocalearn_data.json`: JSON-Datei zur Speicherung der Vokabeldaten.

**Verwendete Konzepte:**
- Funktionen zur Modularisierung des Codes
- Schleifen für wiederholte Abläufe (z.B. Abfragen)
- Bedingungen für Entscheidungen (z.B. richtige/falsche Antworten)
- Listen und Dictionaries zur Datenverwaltung
- Klassen und Objekte für objektorientierte Programmierung

Das Projekt wurde mit Git versioniert und auf GitHub verwaltet, um Änderungen nachvollziehbar zu machen und die Zusammenarbeit im Team zu unterstützen.

## Programmablauf

Der Programmablauf ist einfach und benutzerfreundlich gestaltet:

1. Der Benutzer startet das Programm.
2. Ein Hauptmenü erscheint mit Optionen wie Vokabeln hinzufügen, Lernmodus starten usw.
3. Der Benutzer wählt eine Option aus.
4. Bei Bedarf werden Vokabeln aus der JSON-Datei geladen.
5. Im Lernmodus wird eine Kategorie ausgewählt.
6. Fragen werden nacheinander gestellt, und der Benutzer gibt Antworten ein.
7. Jede Antwort wird überprüft und Feedback gegeben.
8. Nach allen Fragen wird eine Ergebnisauswertung angezeigt.
9. Falsche Antworten werden in einem separaten Durchlauf wiederholt.

Zur Verbesserung der Benutzerfreundlichkeit wird im Lernmodus die Kategorie angezeigt, damit klar ist, in welcher Sprache geantwortet werden muss.

## Teamarbeit

**Valentino:**
- Detaillierte Abläufe folgen..

**Erduan:**
- Detaillierte Abläufe folgen..

## Projektplan

Der Projektplan wurde schrittweise umgesetzt:

1. Planung der Idee und Konzeption des Projekts
2. Umsetzung des Minimalziels mit den Kernfunktionen
3. Testen des Programms auf Funktionalität und Fehlerfreiheit
4. Hinzufügen der Erweiterungen zur Verbesserung
5. Strukturverbesserung durch Einführung von OOP
6. Erstellung der Dokumentation
7. Vorbereitung der Präsentation

## Fazit / Erkenntnisse

folgen..