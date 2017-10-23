---
title: "Fast, easy, realtime metrics using Redis bitmaps"
slug: fast-easy-realtime-metrics-using-redis-bitmaps
date: 2011-11-30 13:20:31 -0600
external-url: http://blog.getspool.com/2011/11/29/fast-easy-realtime-metrics-using-redis-bitmaps/
hash: 39813907054f2be1d1b3ab31c2e8b795
year: 2011
month: 11
scheme: http
host: blog.getspool.com
path: /2011/11/29/fast-easy-realtime-metrics-using-redis-bitmaps/

---

At Spool, we calculate our key metrics in real time. Traditionally, metrics are performed by a batch job (running hourly, daily, etc.). Redis backed bitmaps allow us to perform such calculations in realtime and are extremely space efficient. In a simulation of 128 million users, a typical metric such as “daily unique users” takes less than 50 ms on a MacBook Pro and only takes 16 MB of memory. Spool doesn’t have 128 million users yet but it’s nice to know our approach will scale. We thought we’d share how we do it, in case other startups find our approach useful.
