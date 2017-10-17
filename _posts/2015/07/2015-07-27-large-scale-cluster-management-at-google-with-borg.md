---
title: "Large-scale cluster management at Google with Borg"
date: 2015-07-27 05:17:58 -0500
external-url: https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/43438.pdf
hash: c117784ecfeb26df2f7245f59bd97c84
year: 2015
month: 07
scheme: https
host: static.googleusercontent.com
path: /media/research.google.com/en//pubs/archive/43438.pdf

---

Google’s Borg system is a cluster manager that runs hundreds of thousands of jobs, from many thousands of different applications, across a number of clusters each with up to tens of thousands of machines.

It achieves high utilization by combining admission control, efficient task-packing, over-commitment, and machine sharing with process-level performance isolation. It supports high-availability applications with runtime features that minimize fault-recovery time, and scheduling policies that reduce the probability of correlated failures. Borg simplifies life for its users by offering a declarative job specification language, name service integration, real-time job monito ing, and tools to analyze and simulate system behavior.

We present a summary of the Borg system architecture and features, important design decisions, a quantitative anal- ysis of some of its policy decisions, and a qualitative examination of lessons learned from a decade of operational experience with it.
