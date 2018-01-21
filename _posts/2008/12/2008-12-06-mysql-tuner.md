---
title: "MySQL Tuner"
slug: mysql-tuner
date: 2008-12-06 09:16:00 -0600
category: 
external-url: http://wiki.mysqltuner.com/MySQLTuner
hash: c4c216cd774a07ab27d63bafa37530f1
year: 2008
month: 12
scheme: http
host: wiki.mysqltuner.com
path: /MySQLTuner

---

Having performance issues with MySQL but don’t know why? The kids over at RackerHacker have released a free, open source tool that might be able to help.




MySQLTuner is a script written in Perl that will assist you with your MySQL configuration and make recommendations for increased performance and stability. Within seconds, it will display statistics about your MySQL installation and the areas where it can be improved.




For kicks, I ran it on my local development box, and here’s its report:




-------- Recommendations -----------------------------------------------------
General recommendations:
    Run OPTIMIZE TABLE to defragment tables for better performance
    Enable the slow query log to troubleshoot bad queries
    When making adjustments, make tmp_table_size/max_heap_table_size equal
    Reduce your SELECT DISTINCT queries without LIMIT clauses
    Set thread_cache_size to 4 as a starting value
Variables to adjust:
    key_buffer_size (> 15.9M)
    query_cache_size (>= 8M)
    tmp_table_size (> 32M)
    max_heap_table_size (> 16M)
    thread_cache_size (start at 4)
    innodb_buffer_pool_size (>= 376M)


As you can see, MySQLTuner actually had some pretty good advice. Of course it won’t replace your local neighborhood MySQL expert, but it’s probably a good starting point, and its results just might surprise you.



[permalink]

