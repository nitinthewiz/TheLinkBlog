---
title: "Cacti Data Queries"
date: 2010-12-09 18:52:33 +0000
external-url: http://docs.cacti.net/manual:087:3a_advanced_topics.3_data_queries
hash: ae22bd702c471c47b782f716786746ff
annum:
    year: 2010
    month: 12
hostname: docs.cacti.net
---

Data queries are not a replacement for data input methods in Cacti. Instead they provide an easy way to query, or list data based upon an index, making the data easier to graph. The most common use of a data query within Cacti is to retrieve a list of network interfaces via SNMP. If you want to graph the traffic of a network interface, first Cacti must retrieve a list of interfaces on the host. Second, Cacti can use that information to create the necessary graphs and data sources. Data queries are only concerned with the first step of the process, that is obtaining a list of network interfaces and not creating the graphs/data sources for them. While listing network interfaces is a common use for data queries, they also have other uses such as listing partitions, processors, or even cards in a router.
