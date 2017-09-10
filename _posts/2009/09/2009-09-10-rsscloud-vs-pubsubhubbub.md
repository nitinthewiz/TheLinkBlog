---
title: "RSSCloud Vs. PubSubHubbub: Why The Fat Pings Win"
date: 2009-09-10 11:49:02 +0000
external-url: http://techcrunch.com/2009/09/09/rsscloud-vs-pubsubhubbub-why-the-fat-pings-win/
hash: a411c5d4dda43fa390413333ff9e048f
year: 2009
month: 09
scheme: http
host: techcrunch.com
path: /2009/09/09/rsscloud-vs-pubsubhubbub-why-the-fat-pings-win/

---



Editor’s note: With all of the debate lately between RSSCloud versus PubSubHubbub, we wanted to hear from a developer who could actually tell us which one might be better and why. The following guest post is written by Josh Fraser, the co-founder of EventVue, who is an active contributor to PubSubHubbub in his free time.  He has contributed several client libraries for PubSubHubbub including a WordPress plugin.  Guess which side of the debate he falls on.

In the past few months, a lot of attention has been given to the rise of the real-time web.  The problem is that the web wasn’t designed with real-time in mind.  There is a huge need for the tech community to get behind new protocols that will power this fundamental shift in how web applications work.  Today I want to take a look at two of the leading protocols that enable real-time notifications on the web.  While there are older protocols that enable real-time notifications like XEP-0060, PubSubHubbub (PuSH) and rssCloud are two new protocols which show a lot of promise of gaining adoption.

Both PuSH and rssCloud address a fundamental flaw in the way web applications work today.  Currently, getting updates on the web requires constant polling.  Subscribers are forced to act like nagging children asking, “Are we there yet?”  Subscribers must constantly ping the publisher to ask if there are new updates even if the answer is “no” 99% of the time.  This is terribly inefficient, wastes resources, and makes it incredibly hard to find new content in as soon as it appears.  Both protocols flip the current model on its head so that updates are event driven rather than request driven.  By that I mean that both protocols eliminate the need for polling by essentially telling subscribers, “Don’t ask us if there’s anything new.  We’ll tell you.”

Dave Winer deserves the credit for coming up with the idea long before anyone else.  In fact, the <cloud> element was added to the RSS 2.0 specification in 2001, but has only recently been revived (largely in response to the interest in PuSH).  rssCloud made major progress this week with the announcement that WordPress was adding rssCloud support for all 7.5 million blogs on WordPress.com. In contrast, PuSH is currently enabled for well over 100 million feeds with adopters including Friendfeed, Blogger, Google Reader, LiveJournal, Google Alerts and FeedBurner. I expect to see many more services adopt these new protocols soon.

But if you find yourself confused about how they are different, you’re not alone.

Conceptually, both protocols are very similar.   Both add a simple declaration to a feed that tells a subscriber which hub/cloud has been delegated the responsibility of handling subscriptions.  Both protocols have a centralized hub that notifies subscribers when new content is published.  Both protocols are HTTP based.

The subtle differences in implementation are important to understand, however.  And in my opinion, PuSH is the better protocol for now.  There are basically three things that make PuSH a more robust protocol:

First, PuSH doesn’t just tell you that something changed, it actually sends you the new content (also known as a “fat ping.”) This is an important feature that is missing from rssCloud.  Not only do fat pings make integration simpler for subscribers, they also eliminate the danger of inadvertent denial of service attacks as thousands of subscribers respond to the ping notification and request the updated feed at exactly the same time.  This problem is well known in computer science and is often referred to as “the thundering herd problem.”  While this would be relatively simple to fix in rssCloud, it has yet to be addressed.

Second, PuSH allows variable callbacks (custom URL’s for where the notification is sent) which rssCloud does not.  The rssCloud specification states “Notifications are sent to the IP address the request came from. You can not request notification on behalf of another server.”  This is highly limiting since you cannot separate the servers which are handling subscriptions from the servers which are receiving the ping notifications.

Third, PuSH has a more friendly policy for handling unsubscribes.  In rssCloud, every feed is automatically unsubscribed after 25 hours.  In PuSH, there is an explicit unsubscribe function with the option to automatically unsubscribe after a given amount of time.  Again, this small detail matters a lot when you’re operating at scale.  With rssCloud, RSS readers will be responsible for resubscribing millions of feeds every night – which is far less efficient than sending subscribe/unsubscribe requests only when something changes.

This isn’t to say that there aren’t benefits to rssCloud.  It is far easier to implement an RSS cloud than it is to implement a PuSH hub.  By design, PuSH hubs are not simple to implement.

There are other small differences, but these are the issues that matter most.  Everything else boils down to semantics.

I want to address a couple of misconceptions that are floating around about both protocols.  For example, many people think that rssCloud is simply about building a distributed alternative to Twitter.  This is largely due to Dave Winer’s stated goal for rssCloud to create “a loosely-coupled Twitter-like network of people and 140-character status messages.”  While that is certainly an interesting use-case, it promotes a very narrow view of the protocol and what it enables.  I think rssCloud has far more potential than Dave gives it credit for.

The biggest misconception about PuSH is that it is somehow owned and controlled by Google.  This simply isn’t true.  Not only are there plenty of independent developers like me working on PuSH, there are also other PuSH hubs like SuperFeedr which aren’t controlled by Google.  Brett Slatkin points out:

Our spec development process is completely transparent. You can see every code check-in since August 5th 2008. All discussion is on the public mailing list (there is no Google-internal one). The whole point of this spec is to be open, decentralized, and not in control of any company.

Overall, I believe that both PubSubHubbub and rssCloud represent a huge step forward for the web. While I personally believe that PuSH is a better choice, competition is always good and will make both protocols stronger.

(Photo credit: Flickr/Libertinus)
Crunch Network:  MobileCrunch Mobile Gadgets and Applications, Delivered Daily.

TechCrunch50 Conference 2009: September 14-15, 2009, San Francisco













    


