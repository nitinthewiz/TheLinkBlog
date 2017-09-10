---
title: "MySQL Fork Drizzle Finally Releases First General Availability Version"
date: 2011-03-18 11:07:01 +0000
external-url: http://www.readwriteweb.com/hack/2011/03/drizzle-a-new-fork-of-mysql.php
hash: 3a4ed0245d0a1463fc4f582fec65023a
year: 2011
month: 03
scheme: http
host: www.readwriteweb.com
path: /hack/2011/03/drizzle-a-new-fork-of-mysql.php

---

 Drizzle, a lightweight fork of MySQL, released its first general availability version today. Drizzle is designed for multicore environments and cloud applications. Unlike NoSQL databases, Drizzle still uses structure queried language. Instead, it attempts to improve performance by cutting the database server down to its core.

Sponsor


The project was started by Sun employees in 2008, and Rackspace hired the team to work on Drizzle full time in Adrian Otto:


Drizzle dispenses with views, triggers, prepared statements, and much more. Instead additional features can be added via plugins. Drizzle makes no attempt at backwards compatibility with legacy systems such as 32-bit environments. Here's a partial list of what Drizzle has kept or dispensed with, from a post by tk on the Rackspace blog:


1 - Micro-Kernel Design, with modular interfaces to plug in features and functions without touching the core code. API's for Replication, Storage Engines, Logging,  Authentication, Client Protocols, etc.
2 - No triggers or stored procedures. That stuff is bloat as done in MySQL, and Drizzle has other ways to deal with these needs. These capabilities can be added in later as needed such that they are done right.
3 - Only UTF8 support, not a multitude of language encodings and collations. Keep it simple. This is the web.
4 - Way Less Source Code, where MySQL has well over a million lines of code, Drizzle is just under 300K lines.
5 - Drizzle Client Protocol, that's pluggable and Asynchronous capable with built-in sharding support and built-in checksum support and BSD license so you can package it in commercial software with no license drama.
6 - Default Storage Engine is InnoDB, for ACID compliance but others can still be used. MyISAM is gone. Long live the Queen!
7 - Pluggable AAA, so integrating with your LDAP user database through PAM is simple as pie, if if you don't want any auth (think memcached) just don't load the plugin, and get a nice performance boost.
8 - Replication will be everything you ever wanted in a replication system. You hate MySQL replication? You now love Drizzle.
9 - Logging is pluggable so you can log to Syslog, a query analyzer, Gearman, or whatever you want to plug in.
10 - Query Rewriting is supported. If you have a misbehaving application, you can fix it at the database if desired.
11 - The Data Dictionary is redone so that no internal tables materialize, and there is only a single code execution path. This means all your base run faster.
12 - FRM Files are Gone. Yep, ever been snagged by the contents of an FRM file not matching what's in the database? Cry no more.
13 - The MySQL Client Protocol is supported so you can use Drizzle with most applications without modification.
14 - It's Easy to Build from Source. Ever tried to compile MySQL from source. Hah! Yeah, drizzle builds like butter.

We covered Drizzle in our look at non-relational databases back in 2009.

Discuss

       

