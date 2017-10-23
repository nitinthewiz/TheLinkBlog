---
title: "Building for HTTP/2"
slug: building-for-http-2
date: 2015-11-29 16:54:24 -0600
external-url: http://rmurphey.com/blog/2015/11/25/building-for-http2
hash: bdf4e6b02fe7a96d53d65a9faca113e2
year: 2015
month: 11
scheme: http
host: rmurphey.com
path: /blog/2015/11/25/building-for-http2

---

This is everything-you-thought-you-knew-is-wrong kind of stuff. In an HTTP/2 world, there are few benefits to concatenating a bunch of JS files together, and in many cases the practice will be actively harmful. Domain sharding becomes an anti-pattern. Throwing a bunch of <script> tags in your HTML is suddenly not a laughably terrible idea. Inlining of resources is a thing of the past. Browser caching — and cache busting — can occur on a per-module basis.


