---
title: "PubSubHubbub support for Reader shared items"
date: 2009-08-06 03:51:10 +0000
external-url: http://googlereader.blogspot.com/2009/08/pubsubhubbub-support-for-reader-shared.html
hash: 252648231de5981281ce581202a13621
---

Speed is very important at Google, and the Reader team is no exception. One way in which we take speed into account is to try to make consumption of feeds be as efficient as possible. We also want to make it as fast (and as easy) as possible to interact with your Reader data on the rest of the web.


We're therefore happy to announce that Reader has begun adoption of the PubSubHubbub protocol, beginning with the publishing of our shared items. All shared item pages have feeds, and now all of those feeds will ping a hub (and there's a <link rel="hub" .../> element in them). This means that if you (as a web app developer) would like to more efficiently and quickly monitor Reader shares, you just have to subscribe at the hub to be notified of changes in real-time. If you want to learn more about PubSubHubbub and how it works, see the site and protocol definition.


One place that takes advantage of this pinging is FriendFeed. This means if you have added your shared items to your FriendFeed account, you and your friends will see them there within a few seconds the "Share" link being pressed in Reader (special thanks to FriendFeeder Benjamin Golub for making sure the experience was as smooth as possible). You can see this in action in FriendFeed's search results and in the screencast below:



[YouTube Video]



Adding PubSubHubbub support was a 20% project between Brad Fitzpatrick, Brett Slatkin, and myself, each of us working in our spare time over the past couple of weeks. Adding PubSubHubbub to your application is definitely a low-effort but high-payoff way of making the Web faster and more efficient. And if you have any questions or feedback about PubSubHubbub support, you can reach us on our help group, Twitter or Get Satisfaction.



