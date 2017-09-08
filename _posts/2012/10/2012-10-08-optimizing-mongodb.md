---
title: "Optimizing MongoDB Compound Indexes"
date: 2012-10-08 20:08:13 +0000
external-url: http://emptysqua.re/blog/optimizing-mongodb-compound-indexes/
hash: ab20af3bfec576cbca3c228d0e3d97f5
annum:
    year: 2012
    month: 10
hostname: emptysqua.re
---

How do you create the best index for a complex MongoDB query? I'll present a method specifically for queries that combine equality tests, sorts, and range filters, and demonstrate the best order for fields in a compound index. We'll look at the explain() output to see exactly how well it performs, and we'll see how the MongoDB query-optimizer selects an index.
