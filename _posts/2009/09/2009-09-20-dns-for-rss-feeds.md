---
title: "DNS for RSS feeds"
slug: dns-for-rss-feeds
date: 2009-09-20 23:57:52 -0500
external-url: http://scripting.com/stories/2009/09/20/dnsForRssFeeds.html
hash: ade3aa65fd47e94d646bfa2479f335ad
year: 2009
month: 09
scheme: http
host: scripting.com
path: /stories/2009/09/20/dnsForRssFeeds.html

---

Here is a Unix shell command that gets the address of my RSS feed: dig +short davewiner.supercloud.org TXT
It makes a DNS call to get the TXT record associated with davewiner.supercloud.org. That's different from an A record or a CNAME record. TXT records are used for things like this. That's why when you go there in your browser it doesn't go anywhere. 
I have an app up for you all to try out, so you can have a supercloud.org domain for your RSS feed (it works equally well for Atom, or anything that can be parsed as XML).
http://dns.rsscloud.org/
Enter your Twitter username and password and the URL of your feed. It verifies that it is the correct password. (And it doesn't store it or use it for any other purpose.) And then if everything goes well, your username will map to a supercloud.org domain and point to your feed.
This is of course not rocket science.
But it does seem to work. 
PS: Why this is interesting, possibly, is that it may give us a way to shorten URLs and make them more flexible if we want to build a loosely-coupled Twitter-like network with feeds distributed around the net. DNS is the little bit of centralization that the Internet, itself a loosely-coupled network, is built on.
