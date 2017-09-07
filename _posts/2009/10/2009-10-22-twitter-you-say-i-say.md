---
title: "Twitter: You Say Transparency, I Say Vulnerability"
date: 2009-10-22 03:45:34 +0000
external-url: http://techcrunch.com/2009/10/21/twitter-you-say-transperancy-i-say-vulnerability/
hash: 6ef9749925438ecdce25900509b90b87
---



We received a number of tips early this morning that the majority of web servers at Twitter was exposing server and load-balancer status information to the public. The status page, which are an (often default) option in the open source Apache web server dump an output of all connections and state information for a particular server. The information is used by administrators to monitor servers, and the pages are often either removed entirely or locked down to prevent the information from being used for nefarious purposes.

At some point in the past 24 hours (I would more accurately guess 22 hours 28 minutes and 4 seconds ago, based on the status page itself), the Twitter web servers introduced a misconfiguration to expose this information to the public. The page includes overall server statistics along with every HTTP requests currently being handled by that server, with the full request URL. The server status page is usually accessed by requesting /server-status for a web server. In the case of Twitter, this exposure allows anybody to see requests that sometimes rely on being secret to remain secure, such as oAuth keys, which are used to authorize applications to access Twitter accounts.

News of the pages being open spread quickly through Twitter, with some calling it “great transparency” while others recognizing it for what it is – a little too much transparency, and unintentional. Twitter were very quick to respond and blocked all access to the page, and the vast majority of the information found is purely informational and can be deduced through other means. Your Twitter account is probably safe again, but that doesn’t mean we can’t geek out while we get a sneak peak at what Twitter looks like behind the curtain.

Screenshot of one such page below with some of the information cut out.



Crunch Network:  CrunchGear drool over the sexiest new gadgets and hardware.














    

