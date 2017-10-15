---
title: "Flash Ajax Update: Flex LiveCycle Data Services Goes Open-Source"
date: 2007-12-12 23:01:30 -0600
external-url: http://ajaxian.com/archives/ajax-in-flash-flex-livecycle-data-services-goes-open-source
hash: 12d18957db9a330382999acd7b07969c
year: 2007
month: 12
scheme: http
host: ajaxian.com
path: /archives/ajax-in-flash-flex-livecycle-data-services-goes-open-source

---

Flash (via Flex or AIR) allows developers to open connections to servers (binary sockets), much like XHR in Web applications. And, just as frameworks like DWR and JSON RPC allow for remoting objects via XHR, a number of frameworks allow for remoting objects in Flex. One of the most popular has been Flex LiveCycle Data Services, but it's also a commercial product with a big enough price tag to cause many developers to steer clear.

Not anymore.

Adobe just announced that they are open-sourcing the remoting and HTTP messaging features of Flex LiveCycle Data Sources in a new product called Blaze DS, which will be LGPL licensed. In addition, they are taking a page from Comet and making it easy to create a persistent connection for "server push" functionality for the HTTP messaging. The "data management" features (i.e., keeping a client and server model in sync) remain payware.

In addition, they are publishing the spec to their object remoting protocol (AMF), making it easy for others in the community to create remoting servers (previously, folks had to reverse-engineer the protocol). This opens the door for other non-Java platforms to provide middle tiers in the Flex stack (i.e., Flex doesn't include any public database drivers, so you have to write a middle-tier to transfer data to Flex apps, and right now Java is the only first-class option).

Many folks wonder why Ajax developers don't just use Flash; as Adobe open-sources more and more of their stack, it's going to be very interesting to see the reaction of the community. We at Ajaxian aren't in the "Open Web or Else" crowd, but a fully open Flash stack would sure make the world a touch more interesting.
