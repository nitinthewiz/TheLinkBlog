---
title: "Dissecting Message Queues - Brave New Geek"
date: 2014-09-06 14:57:24 +0000
external-url: http://www.bravenewgeek.com/dissecting-message-queues/
hash: c5a95816af57470fa8a4fca8fbc9d00f
---

Continuing my series on message queues, I spent this weekend dissecting various libraries for performing distributed messaging. In this analysis, I look at a few different aspects, including API characteristics, ease of deployment and maintenance, and performance qualities.The message queues have been categorized into two groups: brokerless and brokered. Brokerless message queues are peer-to-peer such that there is no middleman involved in the transmission of messages, while brokered queues have some sort of server in between endpoints.
