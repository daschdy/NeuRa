---
title: "Neuartige Rechenarchitektur - Gliederung"
date: 2025-27-06
tag: "neura"
[comment]: # use "gf" to follow links
---

# Outline
1. Introduction
    - Worum geht es:
        - Seminar "Neuartige Rechnerarchitekturen"
        - Paper vorstellen
        - Hintergrund und wesentliche Aspekte
    - Wieso ist das Thema aktuell bzw. relevant?
        - wachsende Anzahl von Kernen und Funktionseinheiten bedeutet, dass die Kommunikation zwischen diesen immer herausfordernder und bedeutender wird --> **NoC-Architekturen**
        - in vielen Anwendungen sind geringe Latenzen, garantierte Bandbreiten wichtig, daher ist eine flexible QoS-Unterstützung essentiell --> **Herausforderungen von QoS**
        - AXI4 Standard ist weit verbreitet und in vielen industriellen Designs verwendet. Daher praxisnah und relevant für viele Anwendungen
        - Interessant da...
            - Kombination aus TDM (Time Devision Multiplexing) und VC (Virtual Channel) = Echtzeitanforderungen und flexible Datenströme
            - Durch NI (Intelligente Netzwerk-Schnittstelle) Umwandlung von AXI4-Transaktionen und Vererbung von QoS-Informationen
            - Traffic Converter für bessere Lastenverteilung
            - Auch konkrete Simulationen
2. Hintergrund und Stand der Technik
    - Überblick über NoC
    - AXI4-Protokoll
    - QoS-Konzepte
    - Vergleichbare Literaturansätze
3. Architekturübersicht
    - Gesamtstruktur der vorgeschlagenen NoC-Architektur
    - Rolle der zwei Subnetzwerken (VC und TDM)
    - Netzwerk-Schnittstelle (NI)
        - Aufbau und Funktion
        - Umwandlung von AXI4-Transaktionen
        - QoS-Vererbungsmechanismus
        - Traffic Converter: Funktion und Nutzen
4. Resultate vom Experiment
5. Fazit
