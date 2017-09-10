---
title: "F1: A Distributed SQL Database That Scales"
date: 2013-09-01 02:40:10 +0000
external-url: http://research.google.com/pubs/pub41344.html
hash: f9f9a9b428b36f8bd07f10848583d8cc
annum:
    year: 2013
    month: 09
url-parts:
    scheme: http
    host: research.google.com
    path: /pubs/pub41344.html

---

F1 is a distributed relational database system built at Google to support the AdWords business. F1 is a hybrid database that combines high availability, the scalability of NoSQL systems like Bigtable, and the consistency and usability of traditional SQL databases. F1 is built on Spanner, which provides synchronous cross-datacenter replication and strong consistency. Synchronous replication implies higher commit latency, but we mitigate that latency by using a hierarchical schema model with structured data types and through smart application design. F1 also includes a fully functional distributed SQL query engine and automatic change tracking and publishing.
