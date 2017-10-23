---
title: "How Protoblogger.com works"
slug: how-protoblogger-com-works
date: 2010-12-08 10:21:20 -0600
external-url: http://scripting.com/stories/2010/12/08/howProtobloggercomWorks.html
hash: f47035470fcfcba911832deb31e667d2
year: 2010
month: 12
scheme: http
host: scripting.com
path: /stories/2010/12/08/howProtobloggercomWorks.html

---

Every day I push a bunch of links through Twitter. I have this process fairly well streamlined. I click on a bookmarklet, it grabs the headline and URL and shoots it to an app on one of my servers. It shortens the URL and then sends it to twitter.com, where it all appears in my status box. I edit it, and click the Tweet button and off it goes.

Another app checks in with Twitter every five minutes to see if I've posted anything new and if it has a link in it. If it does, it is saved in a database. This database has been going since April 2009.

On Monday I added another element to the flow. Now the current day's tweets-with-links are pushed to a post on Protoblogger.com, which is a site running on wordpress.com. The connection is very simple, through the MetaWeblog API. So now there's another way to get my links, without going through Twitter.

The links have been available via RSS for quite some time.

