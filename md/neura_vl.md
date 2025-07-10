---
title: "Neuartige Rechenarchitektur - CPU Design VL - BUS & Peripherie"
date: 2025-07-10
tag: "neura"
[comment]: # use "gf" to follow links
---

# CPU Design VL - BUS & Peripherie
- Unterscheidung zwischen On-Chip- und Off-Chip-Protokolle
    - AXI ist On-Chip
- Interconnect verbindet die Anfragen vom Master zum Slave. Hier können diverse Modifikationen stattfinden bspw. QoS
- CPU und Peripherie Constroller sind an On-Chip Bussysteme angebunden
- Singlelayer Bus:
    - verschiedene Mulitplexer
    - es ist nur eine Anfrage von einem Master zu einem Slave möglich, nicht parallel
- Multilayer Bus:
    - mehrere Multiplexer
    - parallele Anfragen möglich
    - Priorisierung durch QoS
- AXI als Bus Protocol im ARM AMBA
    - Open Source
    - es gibt AXI5, aber am weitesten verbreitet AXI4
    - verschiedene Ausführungen: AXI4-Stream, AXI4, AXI4-Lite
    - AXI Handshake essentiell mit definierten Regeln! (*nochmal anschauen*)
- Unterschied zwischen AXI Memory Mapped Lesen und AXI Memory Mapped Schreiben
- AXI Channel Abhängigkeiten (AWVALID, AWREADY, ...)
- AXI4 Adresskontrollsignale darstellen
- Unterschiede On-Chip- und Off-Chip-Protokolle
