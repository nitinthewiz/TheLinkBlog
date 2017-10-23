---
title: "NoSQL: Comparing the Different Solutions"
slug: nosql-comparing-the-different-solutions
date: 2010-11-04 20:35:00 -0500
external-url: http://readwrite.com/2010/11/04/nosql-comparison
hash: 9fb2fd382ac140a785c25d0261aadf72
year: 2010
month: 11
scheme: http
host: readwrite.com
path: /2010/11/04/nosql-comparison

---

Adrian Cockcroft, a cloud architect at Netflix, is running a series of posts looking at how different NoSQL databases handle common cloud computing tasks. All the usual disclaimers apply: SQL is good for some things, and different scenarios call for different NoSQL solutions. No one solution is necessarily "better" overall. However, as Cockcroft writes "We need a basis for comparison across them, so that we understand the differences in behavior."

Sponsor


Cockcroft created an example use case and is asking different NoSQL database developers to explain how  their databases handle availability zones, partitioning between zones, appending items to lists, handling silent data corruption, and backup and restore. Cockcroft uses terms from Amazon AWS, but the concepts should be applicable to other cloud hosting platforms. The use case Cockcroft describes is as follows:


A TV based device calls the API to add a movie to its favorites list (like the Netflix instant queue, but I have simplified the concept here), then reads back the entire list to ensure it is showing the current state. The API does not use cookies, and the load balancer (Amazon Elastic Load Balancer) is round robin, so the second request goes to a different API server, that happens to be in a different Amazon Availability Zone, and needs to respond with the modified list.

He goes on to ask a series of detailed questions about how different NoSQL databases would deal with different aspects of this scenario. His original post is here. Cassandra and MongoDB replied here and here.


Cockcroft says he will offer a summary and comparison of the options after enough developers have replied. Vendors: what are you waiting for? Send in your answers already!

Discuss
