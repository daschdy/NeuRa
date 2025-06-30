---
title: "Neuartige Rechenarchitektur"
date: 2025-05-06
tag: "neura"
[comment]: # use "gf" to follow links
---

# Notes
- 8 - 12 Seiten (Text)

## Paper Summary
[Flexible and Efficient QoS Provisioning in AXI4-Based NoC Architectures](neura_paper.md)

## AXI
- [AMBA AXI4 Interface Protocol](https://www.amd.com/de/products/adaptive-socs-and-fpgas/intellectual-property/axi.html#tabs-ceeab8b2b8-item-766c793914-tab)
- higher productivity:
    - consolidates broad array of interfaces into one
    - makes integrating IP from different domains easier
    - saves design effort
- greater flexibility:
    - supports embedded, DSP and Logic Edition users
    - tailor the interconnect to meet system goals: Performance, power, area
    - key benefits:
- consistent
    - fully specified
    - standardized
    - interface-decoupled
    - extendable
- difference to AXI3:
    - support for burst length up to 256 beats
    - Quality of Service signaling
    - Support for multiple region interfaces

- [Introduction to AMBA AXI4](https://developer.arm.com/-/media/Arm%20Developer%20Community/PDF/Learn%20the%20Architecture/102202_0100_01_Introduction_to_AMBA_AXI.pdf?revision=369ad681-f926-47b0-81be-42813d39e132)
- Advanced Microcontroller Bus Architecture (AMBA)
- What is AMBA?
    - open-standard, on-chip interconnect specification for the connection and management of functional blocks in system-on-a-chip (SoC) designs
    - define how functional blocks communicate with each other
- Why use AMBA?
    - efficient IP reuse
    - flexibility
    - compatibility
    - support
    - related to bus interface performance (main characteristics):
    - latency
    - bandwidth
- AXI protocol overview
    - AXX is an interface specification that defines the inferface of IP blocks, rather than the interconnect itself
    - AXI Master - \[AXI Slave, AXI Interconnect component, AXI Master\] - AXI Slave
    - In AXI4 there are only two AXI interface types: Master and Slave, which are symmetrical
    - direct connections between AXI Masters and AXI Slaves gives maximum bandwidth with no extra logic
    - only one single protocol to validate
    - AXI Protocol defines the signals and timing of the point-to-point connections between masters and slaves $\rarr$ it is a point-to-point specification, not a bus specification
- AXI channels:
    1. Write Address (AW)
    2. Write Data (W)
    3. Write Response (B = Buffered)
    4. Read Address (AR)
    5. Read Data (R)
    - Write operations:
        - The master sends an address on the AW channel and transfer data on the W channel to the slave
        - The slave writes the received data to the specified address. Once the slave has completed the write operation, it responds with a message to the master on the B channel
    - Read operations:
        - The master sends an address on the AR channel to the slave
        - The slave sends the data from the requested address to the master on the R channel
        - The slave can also return an error message on the R channel. An error occurs if, for example, the address is not valid, or the data is corrupted, or the access does not have the right security permission
        - Seperate address and data channels for read and write operations helps to maximize the bandwidith of the interface
    - There is not timing relationship between the channels. Read sequence can happen at the same time as a write sequence
- Main AXI features
    - Independent read and write channels
    - Multiple outstanding addresses
    - No strict timing relationship between address and data operations
    - Support for unaligned data transfers
    - Out-of-order transaction completion
    - Burst transactions based on start address
- Channel Handshake:
    - all channels share the same handshare mechanism that is based one the VALID and READY signals
    - VALID signal goes from the source to the destination and READY goes from the destination to the source
- Differences between transfers and transactions:
    - a **transfer** is a single exchange of information, with one VALID and READY handshake
    - a **transaction** is an entire burst of transfers, containing an address transfer, one or more data transfers, and, for write sequences, a response transfer
- ... (exclusive transaction examples)
- Data size, length:
    - each read and write transaction has attributes that specify the data length, sire and burst signal attributes for that transaction
    - x stands for write and read
    - AxLEN $\rarr$ for AxLEN\[7:0\] has 8 bits, which specifies a range of 1-256 data transfers in a transaction
    - AxSize\[2:0\] describes the maximum number of bytes to transfer in each data transfer. Three bits of encoding indicate 1,2,4,8, ..., 128 bytes per transfer
    - AxBurst\[1:0\] describes the burst type of the transaction: fixed, incrementing or wrapping
- burst type:
    - FIXED - 0x00 - reads the same address repeatedly. Useful for FIFOs
    - INCR - 0x01 - incrementing burst. Useful for block transfers
    - WRAP - 0x10 - wrapping burat. Commonly used for cache line accesses
    - RESERVED - 0x11 - not for use
- Protection level support:
    - AXI provides access permission signals, AWPROT and ARPROT, that can protect againt illegal transactions downstream in the system
    - if a transaction does not have the correct level of protection, a memory controller could refuse read or write access by using these signals
    - AxPROT\[0\] (P) identifies an access as unprivileged or privileged
    - AxPROT\[1\] (NS) identifies an access as Secure or Non-secure
    - AxPROT\[2\] (I) indicates whether the transaction is an instruction access or a data access
- Cache support:
    - modern SoC systems often contain caches that are placed in several points of the system
    - AWCACHE and ARCACHE signals indicate how transactions are required to progress through a system
    - AxCACHE\[0\] (B): the bufferable bit
    - AxCACHE\[1\]: the modifiable bit
    - AxCACHE\[2\]: the RA bit
    - AxCACHE\[3\]: the WA bit
- Response signaling
    - provides response signaling for both read and write transactions
    - for read transactions, the response information from the slave is signaled one the read data channel using RRESP
    - for write transactions, the response information is signaled on the write response channel using BRESP
    - RRESP and BRESP are both composed of two bits and the encoding of these signals can transfer for responses (00 = OKAY, 01 = EXOKAY, 10 = SLVERR, 11 = DECERR)
- Write Data Strobes
    - signal is used by a master to tell a slave which bytes of the data bus are required
    - useful for cache accesses for efficient movement of sparse data arrays
    - in addition you can optimize data transfers using unaligned start addresses
    - one strobe bit per byte on the data bus. These bits make the WSTRB signal
    - master must ensure, that the write strobes are set to 1 only for byte lanes that contain valid data
- Atomic accesses with the lock signal
    - see also chapter 6
    - AxLOCK signal is used to indicate when atomic accesses are being performed
    - AXI Protocol supports two types of atomic accesses:
        - Locked accesses: A locked transfer locks the channel, which remains locked until an unlocked transfer is generated. Locked accesses are similar to the mechanism supported with the AHB protocol
        - Exclusive accesses: Exclusive accesses are more efficient then locked transactions, and they allow multiple masters to access a slave at the same time
    - AXI4:
        - 0b0 - normal access
        - 0b1 - locked access
- Quality of Service (QoS)
    - extra signals to support QoS
    - allows to prioritize transactions allowing to improve system performance by ensuring that more important transactions are dealt with higher priority
    - two signals:
        - AWQOS: Sent on Write Address channel for each write transaction
        - ARQOS: Sent on Read Address channel for each read transaction
    - both signals are 4 bits wide, where the value 0x0 indicates the lowest priority and 0xF indicates the highest priority
- Region signaling
    - optional feature
    - single physical interface on a slave can provide multiple logical interfaces. Each logical interface can have a different location in the system address map
    - when used, slave does not have to support the address decode between different logical interfaces
    - 4-bit region: AWREGION and ARREGION
    - can uniquely identify up to 16 different regions
- User signals
    - option to include a set of user-defined signals
    - can be used on each channel to transfer extra custom control information between master and slave components
    - width of the User signals is defined by the implementation and can be different on each channel
- Dependencies
    - WLAST transfer must be complete before BVALID is asserted
    - RVALID cannot be asserted until ARADDR has been transferred
    - WVALID can assert before AWVALID

## QoS
- [What Is Quality Of Service (QoS) In Networking?](https://www.fortinet.com/resources/cyberglossary/qos-quality-of-service?utm_source=chatgpt.com)
- (accessed 14.05.2025)
- What Is QoS In Networking?
    - the use of mechanisms or technologies that work on a network to control traffic and ensure the performance of critical applications with limited network capacity
    - enables organizations to adjust their overall network traffic by prioritizing specific high-performance applications
    - typically applied to networks that carry traffic for resource-intensive systems. Common services for which it is required include internet protocol television (IPTV), online gaming, streaming media, videoconferencing, video on demand (VOD) and Voice over IP (VoIP)
    - using QoS in networking, organizations have the ability to optimize the performance of multiple applications on their network and gain visibility into the bit rate, jitter, and packet rate of their network
    - key goal is to enable networks and organizations to prioritize traffic, which includes offering dedicated bandwidth, controlled jitter and lower latency
- How Does QoS Work?
    - marking packets to identify service types, then configuring routers to create separate virtual queues for each application, based on their priority
    - As a result, bandwidth is reserved for critical applications or websited that have been assigned priority access
    - provide technologies provide capacity and handling allocation to specify flows in network traffic. This enables the network administrator to assign the order in which packets are handled and provide the appropriate amount of bandwidth to each application or traffic flow
- Types of network traffic:
    - Bandwidth: Speed of a link
    - Delay: Time it takes for a packet to go from its source to its end destination
    - Loss: The amount of data lost as a result of packet loss
    - Jitter: The irregular speed of packets on a network as a result of congestion, which can result in packets arriving late and out of sequence
- Advantages of QoS:
    - Unlimited application prioritization: most mission-critical applications will always have priority and the necessary resources to achieve high performance
    - Better resource management: better manage the organization's internet resources. This reduces costs and the need for investments in link expansion
    - Enhanced user experience: The end goal of QoS is to guarantee the high performance of critical applications, which boils down to delivering optimal user experience
    - Point-to-point traffic management: Managing a network is vital however traffic is delivered, be it end to end, node to node, or point to point
    - Packet loss prevention: Packet loss can occur when packets of data are dropped in transit between networks
    - Latency reduction: Latency is the time it takes for a network request to go from the sender to the receiver and for the receiver to process it

- [What is Quality of Service)](https://www.paloaltonetworks.com/cyberpedia/what-is-quality-of-service-qos)
- (accessed 14.05.2025)
- What is QoS?
    - set of technologies that work on a network to guarantee its ability to dependably run high-priority applications and traffic under limited network capacity
    - QoS technologies accomplish this by providing differentiated handling and capacity allocation to specific flows in network traffic
    - Enables the network administrator to assign the order in which packets are handled and the amount of bandwidth afforded to that application or traffic flow
- Types of Traffic
    - Bandwidth (maximum rate of transfer)
    - Throughput (actual rate of transfer)
    - Latency (delay)
    - Jitter (variation in latency)
- QoS is key to:
    - Voice and video applications
    - Email
    - Interactive applications
    - Batch applications
    - Online purchasing
- How QoS Technologies Work
    - as business depend on the network to transmit information between endpoints, the data is formatted into packets. Network packets allow computers to organize the data similary to envelopes packed with letters sent throigh postal services
    - job of QoS software is to prioritize network packets to maximize the fixed amount of network bandwidth. The network can only transmit a limited amount of data at one. Therefore, QoS gives priority to the appropriate packets. Brandwidth is strategically allocated to deliver the highest service levels in a limited amount of time
    - networking mechanisms for ordering packets and alloting bandwidth are queueing and bandwidth management respectively
    - the classification of traffic according to policy ensures consistency and adequate availability of network resources for the most important applications
    - queuing and bandwidth management tools are assigned rules to handle traffic and data flows. Rules are specific to the classification they received upon entering the network
- bandwidth management
    - control traffic flows on the network
    - preventing exceeding its capacity allows for network congestion avoidance that occurs
    - traffic shaping - a rate limiting technique used to optimize or guarantee performance and increase usable bandwidth where necessary
    - scheduling algorithms - algorithms that offer varied methods for providing bandwidth to specific traffic flows
- Why QoS is important
    - businesses face the need to provide reliable, consistent services for both staff and customers
    - Since QoS shapes the user experience, reputation can be negatively impacted when services are unstable
    - When QoS is low, security and data integrity can be jeopardized. People depend on the communicaion services to work, and poor QoS leads to poor work quality
    - QoS mechanisms give network administrators the power to prioritize applications ad determined by the needs of the business
- Benefits of QoS
    - business rely on applications designed to carry audio and video content for meeting, presentations and even virtual conferences. These types of applications must be delivered at high speed
    - QoS ensures critical applications requiring high bandwidth for real-time traffic can perform at high levels
        - availability of the network as well as the application that run on it
        - critical applications have access to the resources they require to run successfully
        - user experience is improved as data is transported through the network efficiently and securely without disruption
        - bandwidth is used more efficienttly, which reduces costs by eliminating the need to upgrade bandwidth
        - administrators can more effectively manage traffic
- How to implement QoS
    - three main stages:
        1. Strategically define business objectives to be achieved using QoS
        2. Determine service-level requirements of traffic classes
        3. Design and test QoS policies

- [What is quality of service?](https://www.juniper.net/us/en/research-topics/what-is-qos.html?)
- (accessed 14.05.2025)
- What is quality of service?
    - manipulation of traffic such that a network device, such as a router or switch, forwards it in a fashion consistent with the required behaviors of the applications generating traffic
    - QoS enables a network device to differentiate traffic and then apply different behaviors to the traffic
- Problems That QoS Addresses
    - applications run on converged, packet-based networks where traffic shares a common infrastructure and network resources
    - These packet-based networks are intended to deliver traffic on a best effort basis
- What Can You Do with QoS?
    - essential for managing traffic in today's packet-based networks and includes these capabilities:
        - prioritizing traffic over other traffic based on protocol, address and port number
        - filtering traffic upon ingress or egress
        - controlling the allowed bandwidth transmitted or received on the device
        - reading and writing QoS behavior requirements in the packet header
        - controlling congestion so that the device sends the highest priority traffic based on scheduler priorities
        - controlling packet loss using random early detection (RED) algorithms, so that the device knows the packets to drop or process
- How Does QoS Work?
    - A network device, such as a routers or switch, differentiates traffic as follows:
        1. It receives packets on its ingress interface, examines the packets, and classifies the traffic into groups calles classes of service (CoS)
        2. If an optional policer is configured, it limits or assigns the traffic to a different class
        3. Queues hold packets while they await transmission resources
        4. The Scheduler takes the packets out of the queues and transmits them in the order configured for the scheduler
        5. If there is a shaper configured, it shapes the traffic to the configured shaping-rate
        6. If remaking is configured, the device remarks the value of the DS-field of the IP header so that the next device to receive the packet knows how to classify

- [What Is Quality of Service in Networking?](https://www.baeldung.com/cs/quality-of-service?)
- (accessed 14.05.2025)
- What is Quality of Service?
    - measures the capapbility of a network to provide high-quality services to an end-user. More specifically, it designates the mechanisms and technologies for managing data traffic and controlling network resources
    - primary goal of QoS is to prioritize critical applications and specific types of data
    - QoS technologies seek to increase throughput, lower latency and reduce packet loss
- How to Measure QoS?
    - a network flow is a sequence of packets going from one device to another. To quantify the QoS in a network, we need to measure the flow
        - reliability
        - delay or latency
        - jitter
        - bandwidth
- Techniqus to improve QoS?
    - Classification and Marking
    - Queuing and Scheduling
    - Policing and Shaping

## NoC - Network-on-Chip
- [Network on Chip - an Overview](https://ignitarium.com/network-on-chip-an-overview/)
- (accessed 14.05.2025)
- Evolution Of Interconnects
    - Shared Buses: Such as ARM's AMBA bus and IBM's CoreConnect are the commonly used communication mechanisms in SoCs. They support a modular design approach that uses standard interfaces and allows IP reusem but shared but structure becomes a performance bottleneck as the system bandwidth requirements scale-up
    - Hierarchical Bus: Would involve using multiple buses or bus segments to alleviate the load on the main bus. This hierarchical structure would allow for local communication between modules on the same bus segment without causing congestion to the rest of the bus. The disadvantages to this approach are its reduced flexibility and scalability and its complication of the design process. The more cores are attached to the bus, the harder it is to accomplish time closure and QoS
    - Bus Matrix: A full crossbar system is an alternative for on-chip bus communication. Still, as the number of participating system rises, the complexity of wires could be dominant over the logic part. Also, these interconnect logic do not decouble activities generally classified as transport, transaction and physical layer. Hence, when we need any system upgrade, the interface design is affected, and all connected blocks affected. Even though computation and storage benefit from the sub-micron technology uses smaller logic cells and memory, the energy for commmunication is not scalling down. Instead, the crosstalk effects, electromigration, and interconnect delay are affecting timing closure
