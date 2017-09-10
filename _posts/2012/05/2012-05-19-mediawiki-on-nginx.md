---
title: "MediaWiki on Nginx"
date: 2012-05-19 01:42:51 +0000
external-url: http://blog.bigdinosaur.org/mediawiki-on-nginx/
hash: 58f1cf8c153975a4e07a525022217ecc
annum:
    year: 2012
    month: 05
url-parts:
    scheme: http
    host: blog.bigdinosaur.org
    path: /mediawiki-on-nginx/

---

Really thorough and complete guide on configuring nginx for MediaWiki. The internal directives that he uses were completely new to me. I'm going to update my config to have a similar lockdown.

<blockquote>
There are lots of MediaWiki-on-Nginx guides out there, but I didnt find anything approaching the completeness of the much more common MediaWiki-on-Apache guides. The configuration I settled on was a mix of things from around the web, including the MediaWiki site and the Nginx Wiki, and my own ideas, with an eye toward closing off access to as much of the internals as possible and pulling the main configuration components out of the web root.
</blockquote>

