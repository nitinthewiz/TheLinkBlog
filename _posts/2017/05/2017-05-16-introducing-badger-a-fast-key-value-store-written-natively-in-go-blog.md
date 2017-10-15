---
title: "Introducing Badger: A fast key-value store written natively in Go - Dgraph Blog"
date: 2017-05-16 05:34:43 -0500
external-url: https://open.dgraph.io/post/badger/
hash: 59c7f65af75d608171432c6607051164
year: 2017
month: 05
scheme: https
host: open.dgraph.io
path: /post/badger/

---

We have built an efficient and persistent log structured merge (LSM) tree based key-value store, natively in Go language. It is based upon WiscKey paper included in USENIX FAST 2016. This design is highly SSD-optimized and separates keys from values to minimize I/O amplification; leveraging both the sequential and the random performance of SSDs.
