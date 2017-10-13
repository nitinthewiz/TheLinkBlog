---
title: "MediaWiki on Nginx - Bigdinosaur Blog"
date: 2013-05-14 15:18:09 +0000
external-url: http://blog.bigdinosaur.org/mediawiki-on-nginx
hash: 79fa4fd816866b1aed997ff464e3c8ef
year: 2013
month: 05
scheme: http
host: blog.bigdinosaur.org
path: /mediawiki-on-nginx

---

There are lots of MediaWiki-on-Nginx guides out there, but I didnt find anything approaching the completeness of the much more common MediaWiki-on-Apache guides. The configuration I settled on was a mix of things from around the web, including the MediaWiki site and the Nginx Wiki, and my own ideas, with an eye toward closing off access to as much of the internals as possible and pulling the main configuration components out of the web root.
