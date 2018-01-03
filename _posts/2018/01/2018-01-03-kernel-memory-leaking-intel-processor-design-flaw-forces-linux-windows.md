---
title: "'Kernel memory leaking' Intel processor design flaw forces Linux, Windows redesign • The Register"
slug: kernel-memory-leaking-intel-processor-design-flaw-forces-linux-windows
date: 2018-01-03 06:32:09 -0600
external-url: https://www.theregister.co.uk/2018/01/02/intel_cpu_design_flaw/
hash: 574c1035e38c3c8fb462c780d082f0f0
year: 2018
month: 01
scheme: https
host: www.theregister.co.uk
path: /2018/01/02/intel_cpu_design_flaw/

---

This reads like a detective novel and dives into some interesting things about how modern CPU's work and what they do in silicon to protect different memory spaces. This looks like a pretty nasty issue but we won't know the real extent of it until the embargo is removed.

The aside on the name option for the fix made me chuckle:

> The fix is to separate the kernel's memory completely from user processes using what's called Kernel Page Table Isolation, or KPTI. At one point, Forcefully Unmap Complete Kernel With Interrupt Trampolines, aka FUCKWIT, was mulled by the Linux kernel team, giving you an idea of how annoying this has been for the developers.
