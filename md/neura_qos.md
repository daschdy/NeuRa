---
title: "Neuartige Rechenarchitektur - QoS"
date: 2025-05-06
tag: "neura"
[comment]: # use "gf" to follow links
---

# QoS - Quality of Service
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


