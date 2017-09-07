---
title: "Avoiding Bogus Alerts Using AWS-Based Proxies & Outsourced BGP for Distributed Monitoring"
date: 2014-03-06 03:20:00 +0000
external-url: http://blog.logicmonitor.com/2014/03/05/avoiding-bogus-alerts-using-aws-based-proxies-outsourced-bgp-for-distributed-monitoring/
hash: 93c20dc5cd6f08670c7538d11c46b9e4
---

We also could have decided to start peering directly with additional ISPs with the idea being that more connections equals a greater likelihood for transit success, but a simpler solution that avoids us having to manage our own BGP peerings was to deploy a number of proxy servers in various EC2 regions. Proxies receive requests from Collectors and forward them (storing nothing on disk) to LogicMonitors data centers.
