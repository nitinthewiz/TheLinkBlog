---
title: "Service discovery and load balancing with DCOS and marathon-lb: Part 2 - Mesosphere"
date: 2015-12-20 02:59:00 +0000
external-url: https://mesosphere.com/blog/2015/12/13/service-discovery-and-load-balancing-with-dcos-and-marathon-lb-part-2/
hash: 11359acc1ae08a7f47dd29aa5a659fdb
year: 2015
month: 12
scheme: https
host: mesosphere.com
path: /blog/2015/12/13/service-discovery-and-load-balancing-with-dcos-and-marathon-lb-part-2/

---

Marathon-lb works by automatically generating configuration for HAProxy and then reloading HAProxy as needed. Marathon-lb generates the HAProxy configuration based on application data available from the Marathon REST API. It can also subscribe to the Marathon Event Bus for real-time updates. When an application starts, stops, relocates or has any change in health status, marathon-lb will automatically regenerate the HAProxy configuration and reload HAProxy.
