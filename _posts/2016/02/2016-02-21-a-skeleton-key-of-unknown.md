---
title: "A Skeleton Key of Unknown Strength | Dan Kaminsky's Blog"
date: 2016-02-21 14:06:52 +0000
external-url: http://dankaminsky.com/2016/02/20/skeleton/
hash: f01546ba3a05a9ec4cfe7f1822cf84c8
annum:
    year: 2016
    month: 02
hostname: dankaminsky.com
---

The glibc DNS bug (CVE-2015-7547) is unusually bad.  Even Shellshock and Heartbleed tended to affect things we knew were on the network and knew we had to defend.  This affects a universally used library (glibc) at a universally used protocol (DNS).  Generic tools that we didn’t even know had network surface (sudo) are thus exposed, as is software written in programming languages designed explicitly to be safe. Who can exploit this vulnerability? We know unambiguously that an attacker directly on our networks can take over many systems running Linux.  What we are unsure of is whether an attacker anywhere on the Internet is similarly empowered, given only the trivial capacity to cause our systems to look up addresses inside their malicious domains.
