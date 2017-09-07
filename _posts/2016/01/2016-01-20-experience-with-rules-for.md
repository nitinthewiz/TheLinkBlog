---
title: "Experience with Rules-Based Programming for Distributed Concurrent Fault-Tolerant Code"
date: 2016-01-20 11:11:01 +0000
external-url: http://blog.acolyer.org/2016/01/19/dcft/
hash: a9b2ef2681d9ca5022047d6b1ca507cb
---

To demonstrate applicability outside of the RAMCloud system, the team also re-wrote the Hadoop Map-Reduce job scheduler (which uses a traditional event-based state machine approach) using rules. The original code has three state machines containing 34 states with 163 different transitions, about 2,250 lines of code in total. The rules-based re-implementation required 19 rules in 3 tasks with a total of 117 lines of code and comments.
