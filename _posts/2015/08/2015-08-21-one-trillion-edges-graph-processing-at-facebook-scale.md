---
title: "One Trillion Edges: Graph Processing at Facebook-Scale"
slug: one-trillion-edges-graph-processing-at-facebook-scale
date: 2015-08-21 16:35:19 -0500
external-url: http://www.vldb.org/pvldb/vol8/p1804-ching.pdf
hash: f93f2b50b5eb81546436a508a87ff0cc
year: 2015
month: 08
scheme: http
host: www.vldb.org
path: /pvldb/vol8/p1804-ching.pdf

---

Analyzing large graphs provides valuable insights for social networking and web companies in content ranking and rec- ommendations. While numerous graph processing systems have been developed and evaluated on available benchmark graphs of up to 6.6B edges, they often face significant dif- ficulties in scaling to much larger graphs. Industry graphs can be two orders of magnitude larger - hundreds of bil- lions or up to one trillion edges. In addition to scalability challenges, real world applications often require much more complex graph processing workflows than previously evalu- ated. In this paper, we describe the usability, performance, and scalability improvements we made to Apache Giraph, an open-source graph processing system, in order to use it on Facebook-scale graphs of up to one trillion edges. We also describe several key extensions to the original Pregel model that make it possible to develop a broader range of production graph applications and workflows as well as im- prove code reuse. Finally, we report on real-world operations as well as performance characteristics of several large-scale production applications.
