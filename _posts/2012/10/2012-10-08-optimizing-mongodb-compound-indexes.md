---
title: "Optimizing MongoDB Compound Indexes"
slug: optimizing-mongodb-compound-indexes
date: 2012-10-08 15:08:13 -0500
category: 
external-url: http://emptysqua.re/blog/optimizing-mongodb-compound-indexes/
hash: ab20af3bfec576cbca3c228d0e3d97f5
year: 2012
month: 10
scheme: http
host: emptysqua.re
path: /blog/optimizing-mongodb-compound-indexes/

---

How do you create the best index for a complex MongoDB query? I'll present a method specifically for queries that combine equality tests, sorts, and range filters, and demonstrate the best order for fields in a compound index. We'll look at the explain() output to see exactly how well it performs, and we'll see how the MongoDB query-optimizer selects an index.
