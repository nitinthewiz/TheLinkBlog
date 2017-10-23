---
title: "NGiNX HTTP Push Module"
slug: nginx-http-push-module
date: 2009-11-19 06:44:12 -0600
external-url: http://ajaxian.com/archives/nginx-http-push-module
hash: 128f2668a4fac96b8e89714d4f69f475
year: 2009
month: 11
scheme: http
host: ajaxian.com
path: /archives/nginx-http-push-module

---

Even PHP developers can write web applications that use all sorts of fancy long-polling.


That is what Leo said about his NGiNX HTTP push module:


This module turns Nginx into an adept HTTP Push and Comet server. It takes care of all the connection juggling, and exposes a simple interface to broadcast messages to clients via plain old HTTP requests. This lets you write live-updating asynchronous web applications as easily as their old-school classic counterparts, since your code does not need to manage requests with delayed responses.

NHPM fully implements the Basic HTTP Push Relay Protocol, a no-frills publisher/subscriber protocol centered on uniquely identifiable channels. It it an order of magnitude simpler and more basic than similar protocols (such as Bayeux). However, this basic functionality together with the flexibility of the server configuration make it possible to reformulate most HTTP Push use cases in Basic HTTP Push Relay Protocol language with very little application- and client-side programming overhead.


Configure NGiNX and write some code to talk to it.


  

