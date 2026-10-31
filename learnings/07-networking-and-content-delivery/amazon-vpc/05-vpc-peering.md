# VPC Peering

## Simple definition

VPC Peering is a private network connection between two Amazon VPCs. It lets resources in one VPC communicate with resources in the other VPC using private IP addresses.

## Core idea in plain English

Think of VPC Peering like building a private bridge between two separate AWS networks.

After the bridge is created, resources on both sides can talk to each other privately, as long as routing and security rules allow it.

## Main use cases

* Connect two VPCs that need to share resources
* Allow application servers in one VPC to talk to databases in another VPC
* Connect VPCs in different AWS accounts
* Connect VPCs in different AWS Regions
* Separate environments, such as production and shared services, while still allowing private communication

## Key features

* Private communication using private IPv4 or IPv6 addresses
* Works between VPCs in the same account or different accounts
* Works in the same Region or across Regions
* No VPN hardware required
* No single point of failure or bandwidth bottleneck managed by you
* Traffic stays on the AWS network and does not go over the public internet
* One-to-one connection between two VPCs

## How it works

1. You create a peering request from one VPC to another.
2. The owner of the other VPC accepts the request.
3. The peering connection becomes active.
4. You update route tables in both VPCs so traffic knows to use the peering connection.
5. You make sure security groups and network ACLs allow the traffic.

Important idea: creating the peering connection alone is **not enough**. You must also configure routing and security rules.

## Why it is important for the exam

VPC Peering appears in AWS exam questions because it tests whether you understand **private VPC-to-VPC connectivity**.

You should know when AWS wants:

* a simple direct connection between two VPCs
* a larger hub-and-spoke network design
* private access to a service instead of full VPC connectivity

For the Cloud Practitioner exam, the big idea is:

* **VPC Peering = connect two VPCs directly**
* **Transit Gateway = connect many networks through a hub**
* **PrivateLink = private access to a service, not the whole VPC**

## Related AWS services and differences

### VPC Peering vs AWS Transit Gateway

* **VPC Peering** is direct, one-to-one connectivity between two VPCs.
* **Transit Gateway** is a central hub that connects many VPCs and even on-premises networks.
* Use **VPC Peering** for simple designs.
* Use **Transit Gateway** for larger environments with many VPCs.

### VPC Peering vs AWS PrivateLink

* **VPC Peering** connects whole VPCs.
* **AWS PrivateLink** gives private access to a specific service or application.
* Use **PrivateLink** when you want to expose only one service, not the full network.

### VPC Peering vs Site-to-Site VPN

* **VPC Peering** connects AWS VPC to AWS VPC.
* **Site-to-Site VPN** connects on-premises networks to AWS using encrypted VPN tunnels.
* VPN is for hybrid connectivity, not direct VPC-to-VPC peering inside AWS.

### VPC Peering vs Direct Connect

* **VPC Peering** is for VPC-to-VPC communication in AWS.
* **Direct Connect** is a dedicated private connection from your on-premises location to AWS.
* Direct Connect is for connecting your company network to AWS, not for connecting two VPCs directly.

## Common exam traps

* **Trap 1: Thinking peering is transitive**
  It is **not** transitive.

  If VPC A is peered with VPC B, and VPC B is peered with VPC C, that does **not** mean VPC A can talk to VPC C through VPC B.

* **Trap 2: Forgetting route tables**
  Even if peering is active, traffic will not flow until route tables are updated.

* **Trap 3: Forgetting security groups and NACLs**
  Routing alone is not enough. Security rules must also allow the traffic.

* **Trap 4: Using overlapping CIDR ranges**
  You cannot create VPC Peering between VPCs with overlapping IP address ranges.

* **Trap 5: Choosing peering for many VPCs**
  Peering works well for simple designs, but it becomes hard to manage when many VPCs need to connect to each other.

* **Trap 6: Confusing Peering with PrivateLink**
  Peering gives broader network connectivity. PrivateLink is for private service access.

## Easy real-world example

A company has:

* one VPC for its web application
* one VPC for a shared database

The company wants the application servers to access the database privately without using the internet.

They create a **VPC Peering** connection between the two VPCs, update route tables, and allow the required database port in the security rules.

Now the application can reach the database using private IP addresses.

## Final summary

VPC Peering is a simple way to privately connect **two** VPCs.

It is best when you need direct VPC-to-VPC communication and the design is small or straightforward.

Remember these exam points:

* private connection between two VPCs
* same account or different accounts
* same Region or different Regions
* route tables must be updated
* overlapping CIDRs are not allowed
* peering is **not transitive**

## Short exam answer

VPC Peering is a private, one-to-one network connection between two VPCs that allows resources in both VPCs to communicate using private IP addresses.

## Memory trick

**Peering = Private bridge between two VPCs**

Think:

* **Peering = pair**
* a pair means **two**
* so VPC Peering is best for **two VPCs connected directly**

---

## Exam coach note

If the question says:

* **connect two VPCs privately** → think **VPC Peering**
* **connect many VPCs easily** → think **Transit Gateway**
* **privately access one service** → think **AWS PrivateLink**
