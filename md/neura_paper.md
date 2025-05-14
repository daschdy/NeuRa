---
title: Flexible and Efficient QoS Provisioning in AXI4-Based Network-on-Chip Architectures
date: 2025-05-05
tag: "neura"
---

# Notes 
## Introduction
- AXI4 (Advanced eXtensible Interface 4) is the fourth generation of the AMBA (Advanced Microcontroller Bus Architecture) protocol developed by ARM, which supports high-performance, high-frequency system designs
- It uses five individual channels for communication between master and slave interfaces
- Initially it was design as a bus-oriented protocol, but with the development of semiconduction technology, the number of cores increases, requiring a more efficient interconnect architecture
- There are already some system architectures supporting AXI4, but they are not showing the details in the network interface or their NoC architectures do not consider the support of QoS
- the authors propose an AXI-based NoC architecture to provide three different QoS schmes:
  1. message format conversion $\rarr$ making the NoC design independent from the AXI4 protocol
  2. three different QoS services and a NoC-based communication architecture with two sub-networks to efficiently support them
  3. traffic converter unit in each NI to smartly distribute packets $\rarr$ improving NoC performance
  4. three different control mechanisms in the VC subnetwork
  5. cycle-accurate simulator
  6. in this simulator, the authors propose a two-level Markov modulatd process (MMP)-based traffic generator for better simulation

## Related Work
### AXI4-Based Communication Support
- Kwon et al.: In-network reorder buffer to satisfy the in-order packet delivery requirement
- Yang et al.: proposed an AXI-compliant on-chip NI architecture to offer the transaction reordering processing
- Ebrahimi et al.: proposed a hybrid NI architecture with reorder buffer sharing in both the memory and the processor
- Neishaburi and Zilic proposed a debug-aware NI
- Ramirez et al., Tidala and Nguyen et al. take the NoC interconnect into consideration to design an AXI-based system in FPGA
- Radulescu et al. proposed an on-chip NI offering backward compatibilty with existing bus protocols
- Liao et al. implemented the AXI protocol on the 3D system on chips
- Satisfying the transactions' ordering requirements of AXI4 but do not consider the signal format conversion
- the related work do not mention the support of different QoS schemes in NoC

### QoS Provisioning in NoCs
- Sharifi et al.: higher priority to packets that will access idle memory banks
- Chen et al.: DRAM access packets. It models the roundtrip latency prediction, based on which diffrent priorities are offered to packets
- Liu et al.: highway-based time-division multiplexing (TDM) NoC.
- Goossens et al.: buffering function into the TDM network

### Flow Control in NoCs
- Ma et al.: Flow control design based on fully adaptive routing algorithms
- Pérez et al.: proposed a mechanism that allows ty bypass flits even if the buffers to bypass are not empty
- Evain and Diguet proposed a prereservation mechanism
- Lu et al.: proposed a $(\sigma, \phi)$-based flow regulation as a design instrument for SoC architecs to control QoS and achieve cost-effective communication
- Jafari et al.: proposed a flow controll regulation, which is performed per flow for its peak rate and burstiness
- Lu and Yao used a fuzzy-algorithm-based control method to regulate the incjection rate in each NI
- Wang et al.: proposed an artificial neural network (ANN)-based admission control for the on-chip network

### TDM Routing Algorithm
- Lu and Jantsch: two-step approach for routing in the TDM-based virtual circuit network
- Patil et al.: multiiteration routing algorithm to combine path and time slot selection in a single pass
- Kapre et al.: use two different routing algorithms
- Shpiner et al.: latency-based schedulin algorithm
- Stefan et al.: distributed routing mechanism
- Winter and Fettweis: different realizations of a central hardware unit
- Liu et al.: probe-based distributed solution for dynamic path searching

### Router Microarchitecture Design
- Ramnujam et al.: new router design that aims to emulate an output-buffer router (OBR) practically based on a distributed shared-buffer router (DSB) router architecture
- Lu et al.: low-latency wormhole router for packet-swichted NoC designs
- Xin and Choy: dynamic look-ahead bypass to reduce packet latency in NoC
- Wang et al.: high-performance and low-cost router design based on a generic two-stage router
- Li et al.: low level latency and power efficiency by relaxing the constraint of lossless communication

### Industrial Designs for AXI4-Based QoS
- Xilinx: QoS schemes in the AXI-based Zynq-7000 AP SoC devices
- Kazaz et al.: 5G wireless infrastructure architecture where the NoC is applied to supported the communication among IP cores that follow AXI4 standards
- Liß et al.: novel networking device that provides low-lateny switching and routing

### Compared With Our Previous Work
- extention of 6-page conference publication

## Background and Motivation
### AXI4 Channels
- burst-based protocol, which supports hich-performance, high-frequency system design
- read transaction with two independent transaction channels:
  - read address channel
  - read data channel
- write transaction with three independent transaction channels:
  - write address channel
  - write data channel
  - write response channel
- all signlas include a 4-bit QoS tag to identify the corresponding transaction service

### QoS Support in AXI4-Compatible NoC
- quite different from the packet format in the NoC sytem
- message format conversion between the AXI4 protocol and the NoC system $\rarr$ from flit/ frame to packet
- AXI4 signals may have multiple QoS requirements:
  - guaranteed bandwidth
  - priority requirement
  - best-effort requirement

### AXI4 Ordering Requirement
- possible out-of-order delivery in NoC-based communication $\rarr$ master-side and slave-side AXI4 ordering units are required
- mechanism can avoid deadlock and ath the same time provide higher performance
- NIs ordering units are responsible for maintaining the ordering restrictions

## System Design
### QoS Definition and Overall Architecture
- three different QoS services:
  1. Latency Critical Service
  2. Guaranteed Rate Service
  3. Unspecified Rate Service
- system can be divided into three parts:
  1. master/ slave nodes: utilized the AXI4 protocol
  2. NI: protocol conversion and QoS provisioning
  3. NoC
- specific target format of packet in the NoC depends on the QoS identifier in the AXI4 protocol (4-bit)
- identifier LCS or URS will be packed as VC packet transferring in the VC subnetwork
- identifier GRS will be packed as TDM packet transferring in the TDM subnetwork
- this scheme makes NoC design independent from the AXI4 protocol
- offers high-performance NoC design
- QoS inheritance mechanism in the slave-side NI

### Supporting Message Format Conversion in the NI
- two options:
  1. Convert AXI4 signal in each AXI4 channel into a packet format and utilize five individual channels to transfer them in the NoC. TDM and VC subnetwork jhave five independent channels separately connected to the five AXI4 channels
  2. AXI4 protocol adapt to the traditional NoC architecture
- primary idea of 2): NoC independent from AXI4, NoC architecture individuall withouth the restrictions from the AXI4 protocol
- more about 2) solution:
  - AXI4 signals will be converted into read request and response packets, write request and response packets transferred by the shared NoC resources
  - offers high-performance NoC architecture
  - NoC can also make all kinds of communication architectures, such as bus, NoC, etc., compatible with the AXI4 protocol
  - NI has three functionalities:
    - receiving signals from AXI4 channels and NoC subnetworks, which will then dispatched to the corresponding AXI4 channels according to the AXI4 signal type (read/ write) or the corresponding NoC subnetwork (TDM/ VC)
    - responsible for message format conversion between the AXI4 signal and NoC packet
    - slave-side NI applies QoS inheritance mechanism to the response packet so that the QoS scheme can be applied to the packet's round-trip transfer in the NoC system
- Master-side NI:
  - AXI4 signals in five AXI4 channels are forwarded to/ from four AXI4 payload buffers through the AXI4 slave interface in the master-side NI
- ...

### Traffic Converter
- traffic converter locates after the switch to NoC
- convert traffic between VC and TDM subnetworks once their loads are imbalenced and necessary conditions are met before the AXI4 signals are packed into packets (VC or TDM packets)
- NI architectures with switch units, QoS inheritance mechanism and traffic converter

### Supporting QoS in the NoC-Based Architecture
- increasing link utilization
- buffer for the best effort service will influence the frequency and hardware area consumption
- integration of all three different QoS schemes into one network architecture is less likely a reasonable solution
- therefore: eclectic architecture of two subnetworks, a VC-based wormhols subnetwork and a TDM-based virtual-circuit subnetwork, to separately support the LCS, URS and GRS
- VN consists of two VCs
- utilize the virtual-circuit TDM for message transfer. Each router has it own input and output port and global sense of synchronized time slot. The routing table in each router is based on the time slot


## Experiments
### Methodology
- build own simulator, which supports AXI4, two-subnetwork NoC architecture and three QoS schemes
- ...

### Experimental Results
1. Throughput:
  - the upper bound on ideal throughput of the VC subnetwork is determined by the critical link
  - the upper bound on ideal throughput of the TDM subnetwork is determined by the overall available preestablished communication paths
2. Traffic Injection:
  -  ...
3. Resource Utilization
  - ...
4. Latency
  - ...
5. Performance of Traffic Conversion
  - ...
