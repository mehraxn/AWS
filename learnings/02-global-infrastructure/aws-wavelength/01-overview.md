# AWS Wavelength

## Simple definition

AWS Wavelength is an AWS service that puts AWS compute and storage closer to mobile users inside telecom providers’ 5G networks, so applications can run with very low latency.

## Core idea in plain English

Normally, an app sends traffic from a phone to an AWS Region, which may be far away. AWS Wavelength moves some app resources closer to the user by placing them at the edge of a mobile carrier network.

That means the app can respond faster, which is important for real-time experiences.

## Main use cases

AWS Wavelength is used for applications that need ultra-low latency for mobile users.

Common use cases include

 Real-time gaming on mobile devices
 Live video streaming with interactive features
 Augmented reality (AR) and virtual reality (VR)
 Smart city and IoT applications
 Real-time video analytics
 Connected vehicles and industrial edge applications

## Key features

 Runs AWS infrastructure closer to 5G users
 Uses Wavelength Zones, which are connected to a parent AWS Region
 Lets you extend your Amazon VPC into a Wavelength Zone
 Supports familiar AWS services such as Amazon EC2 and some storagenetworking features
 Helps reduce latency for mobile applications
 Still connects back to services in the main AWS Region

## How it works

1. You create a VPC in an AWS Region.
2. You extend that VPC into a Wavelength Zone.
3. You launch supported resources, such as EC2 instances, in the Wavelength Zone.
4. Mobile users on the telecom provider’s network reach the application with lower latency.
5. The application can still communicate with other AWS services running in the parent Region.

Think of it like this

 Region = main AWS home
 Wavelength Zone = AWS mini-location inside a telecom network for faster mobile access

## Why it is important for the exam

For the Cloud Practitioner exam, AWS Wavelength matters because AWS often tests whether you can choose the right service for low-latency edge use cases.

You should recognize that Wavelength is the best fit when the question mentions

 5G networks
 Mobile users
 Ultra-low latency
 Real-time processing near telecom users

## Related AWS services and differences

### AWS Wavelength vs AWS Local Zones

 Wavelength puts AWS infrastructure inside or very close to a telecom provider’s mobile network.
 Local Zones put AWS infrastructure closer to a city or metro area, but not specifically inside a 5G carrier network.
 Choose Wavelength for ultra-low-latency mobile and 5G workloads.
 Choose Local Zones when you want AWS resources closer to users in a geographic area.

### AWS Wavelength vs AWS Outposts

 Wavelength is for low-latency applications near mobile carrier networks.
 Outposts brings AWS hardware to your own on-premises location.
 Choose Wavelength when users are mobile and on telecom networks.
 Choose Outposts when workloads must run in your data center or facility.

### AWS Wavelength vs Amazon CloudFront

 Wavelength runs application compute closer to users.
 CloudFront caches content closer to users.
 CloudFront is mainly for fast content delivery.
 Wavelength is for real-time application processing.

### AWS Wavelength vs AWS Global Accelerator

 Global Accelerator improves global traffic routing to application endpoints.
 Wavelength places workloads closer to mobile users.
 Global Accelerator helps traffic take a better path.
 Wavelength reduces distance to the application itself.

## Common exam traps

 Do not confuse Wavelength with CloudFront. CloudFront caches content; Wavelength runs application workloads closer to mobile users.
 Do not confuse Wavelength with Outposts. Outposts is for your own site; Wavelength is for telecom edge locations.
 Do not confuse Wavelength with Local Zones. Local Zones are metro-area extensions of Regions; Wavelength is specifically for carrier and 5G edge workloads.
 If the exam question says 5G, mobile devices, or ultra-low latency, AWS Wavelength is a strong clue.

## Easy real-world example

A company builds a mobile AR game. Players need instant responses when they move, tap, and interact with objects on screen.

If the app runs only in a distant AWS Region, the delay may feel too slow.

With AWS Wavelength, the company can place the game backend closer to users inside a telecom network, reducing delay and making the game feel smoother.

## Final summary

AWS Wavelength is an edge computing service for mobile and 5G applications that need ultra-low latency.

It works by extending a VPC from an AWS Region into a Wavelength Zone located in or near a telecom provider’s network. This lets developers run application components closer to mobile users while still using AWS services in the parent Region.

## Short exam answer

AWS Wavelength is an AWS service that brings compute and storage closer to mobile users on 5G networks to support ultra-low-latency applications.

## Memory trick

Wavelength = wireless + low latency

Think

 Wave = mobile signal  telecom network
 Length = distance becomes shorter

So AWS Wavelength means AWS closer to wireless users.
