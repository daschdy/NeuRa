---
title: "Neuartige Rechenarchitektur - NoC"
date: 2025-05-06
tag: "neura"
[comment]: # use "gf" to follow links
---

# Network-on-Chip (NoC)
- [Network on Chip - an Overview](https://ignitarium.com/network-on-chip-an-overview/)
- (accessed 14.05.2025)
- Evolution Of Interconnects
    - Shared Buses: Such as ARM's AMBA bus and IBM's CoreConnect are the commonly used communication mechanisms in SoCs. They support a modular design approach that uses standard interfaces and allows IP reusem but shared but structure becomes a performance bottleneck as the system bandwidth requirements scale-up
    - Hierarchical Bus: Would involve using multiple buses or bus segments to alleviate the load on the main bus. This hierarchical structure would allow for local communication between modules on the same bus segment without causing congestion to the rest of the bus. The disadvantages to this approach are its reduced flexibility and scalability and its complication of the design process. The more cores are attached to the bus, the harder it is to accomplish time closure and QoS
    - Bus Matrix: A full crossbar system is an alternative for on-chip bus communication. Still, as the number of participating system rises, the complexity of wires could be dominant over the logic part. Also, these interconnect logic do not decouble activities generally classified as transport, transaction and physical layer. Hence, when we need any system upgrade, the interface design is affected, and all connected blocks affected. Even though computation and storage benefit from the sub-micron technology uses smaller logic cells and memory, the energy for commmunication is not scalling down. Instead, the crosstalk effects, electromigration, and interconnect delay are affecting timing closure negatively 
    - Thus, in the early 2000s some authors proposed the use of a pre-defined platform to implement the communication among the several cores in a chip. Such a platform is implemented as an integrated switching network, called **Network-on-Chip** (NoC), and meets some of the key requirements of future systems: reusability, scalable bandwidth, and low power consumption. Mainy analytical studies happened in this concept to quantize the advantage of switching to a netword instead of wires
- NoC
    - replaces the ad-hox global wire connections across a chip intelligent network infrastructure
    - Models, techniques, and tools from the network are applied to SoC design with proper customization
    - Wire communication is changed to packet communication
- Building Blocks of NoC
    - a network-on-chip is composed of three main building blocks:
        - the first and most important ones are the links, that physically connect the nodes and implement communication
        - the second are the routers, that implement the communication protocol
        - The last building block is the network adapter (NA) or network interface (NI). This block makes the logical connection between the IP cores and the network
- Link
    - a communication link is composed of a set of wires and connects two routers in the network
    - may consist of one or more logical or physical channels, and each channel is composed of a set of wires
    - the implementation of a link includes the definition of synchronization protocol between source and target nodes
    - this protocol can be implemented by dedicated wires set during the communication or through other approaches such as FIFOs
- Routers
    - NoC router comprises a number of input ports, a number of output ports, a switching matrix connectiong the input ports to the output ports, and a local port to access the IP core connected to this router
    - The router also contains a logic block that implements the flow control policies and defines the overall strategy for moving data through the NoC
    - **Flow Control**: Characterizes packet movement in NoC, both global and local
    - **Routing Algorithm**: Logic that selects one output port to forward a packet that arrives at the input port. There is deterministic and adaptive routing
    - **Arbitration Logic**: While the routing algorithm selects an output port for a packet, the arbitration logic implemented in the router selects one input port when multiple packets
    - **Buffering**: The Buffering policy is the strategy used to store information in the router when there is congestion in the network, and a packet cannot be forwarded right away
    - **Switching**: The switching defines how the data is transmitted from the source node to the target one. In the circuit switching approach, the whole path from source to node is previously established and reserved for the transmission of the whole packet. The payload is not sent until the whole path has been reserved. This can increase latency, but once the path is defined, this approach can give some guaranteed throughput
- Network Interface
    - This block makes the logic connection between the IP cores and the network since each IP max have a distinct interface protocol with respect to the network



