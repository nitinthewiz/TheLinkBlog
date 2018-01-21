---
title: "Cogmap 2.1 - OpenID support, Newsfeeds, XML APIs"
slug: cogmap-2-1-openid-support-newsfeeds-xml-apis
date: 2008-03-26 22:43:12 -0500
category: 
external-url: http://www.cogmap.com/blog/2008/03/26/cogmap-21-openid-support-newsfeeds-xml-apis/
hash: 39f3d2a302eb21da00c57a56a8a21977
year: 2008
month: 03
scheme: http
host: www.cogmap.com
path: /blog/2008/03/26/cogmap-21-openid-support-newsfeeds-xml-apis/

---

This evening we did another code release with several relatively minor but very cool additions:


OpenID support.  Thats pretty geeky, but pretty cool!  Today we only support having one OpenID associated with an account.  If it turns out that is an issue, leave a comment or send an email and we will work out that last bit of trickery.
MyCogmap has newsfeeds! Now instead of seeing a list of charts you subscribe, edit, and create, we give you, in historical order, the changes that have taken place with charts you subscribe to.  This provides a much richer palette of changes in data going on in the site.
Consume your newsfeed! http://www.cogmap.com/newsfeed_xoxo.php?cogid=&lt;your screen name&gt; returns an XOXO XML document of your newsfeed.  This makes it easy to turn your newsfeed into something consumed by other applications.  Thats kind of fun!  Here is my newsfeed as an example.
# of Subscribers to a map - Now we show it on the map.  Kind of interesting!
A bunch of small fixes, particularly to search.  Now search peruses chart metadata and notes in the results which charts are private charts that you have permission to access.
