---
title: "More Usable URLs: Twitter.com"
date: 2009-04-28 14:28:27 +0000
external-url: http://garrickvanburen.com/archive/more-usable-urls-twittercom
hash: 7c9521f6e5064d3fbbae2385d232ab2f
annum:
    year: 2009
    month: 04
hostname: garrickvanburen.com
---

URLs are consistently the least usable aspect of our interaction with web-based information services - which is terribly unfortunate considering their prominence in how we access, share, and interact with these services.  

With that in mind, let’s take a look at how Twitter’s URLs could be more usable - by either being more logical, more readable, more share-able, or a combination of all 3.

Here’s a standard Twitter URL:
http://twitter.com/garrickvanburen/status/161277022

Let’s break this apart:
/garrickvanburen
The person’s Twitter account we’re interested in - very clear1. 

/status
I’m not sure what ’status’ is - seems like a very system-centric term. For the sake of this conversation, let’s assume it’s a synonym for ‘note’, ‘message’, ‘news’, ‘memo’, or the collection of things I publish at Twitter.

/161277022
This is the individual ’status’ identifier. Presumably, it’s the primary key ID of this ’status’ within all the ’statuses’ in Twitter’s database - making this ’status’ ID global - not nested within ‘garrickvanburen’.   Again, very system-centric and kind of backwards - if we assume URLs should go from largest logical entity to smallest nested entity. 

A RESTful URL structure would dictate the following:
/Plural Version of Resource Name
/Individual Resource Identifier
/Plural Version of Sub-Resource Name
/Individual Sub-Resource Identifier
/(et. al.)


If we mapped Twitter’s existing structure against this model we’d have:
http://twitter.com/people/garrickvanburen/statuses/161277022

We can see, Twitter’s URLS aren’t exactly RESTful, and since they’re not - let’s look at some ways to make them more logical.

Proposal 1: Logically Long
http://twitter.com/garrickvanburen/twitter-suggestion-put-the text-of-the-tweet-in-the-tweets-permalink.
This is the most usable and readable for both people and machines. It has the huge benefit of having the entire message in the URL (the mind reels with possibilities). WordPress does a great of making legal URL strings out of a weblog post’s title.
Benefits: Highly-readable, logical nested structure, great for search engines
Detriments: Long (though Twitter’s built-in limits provide a maximum length)

Proposal 2: Globally Short
http://twitter.com/1612770222
This is akin to my WordPress URL Shortening Hack
Benefits: Short
Detriments:  Almost no information provided makes this the least usable and equivalent to the shortened URLs you find throughout Twitter.

Proposal 3: Personally Short
http://twitter.com/garrickvanburen/5954
Where 5954 is the number of the individual message in the pool of all my messages.
Benefits: Short, encourages numerically navigating through a person’s messages.
Detriments: Numbers are always less usable than words.

The great thing about these proposals is they’re not mutually exclusive. In fact - different URL structures bias different usages and contexts. In the same way different formats (HTML, RSS, XML, Text-only, etc) providing different presentations of the same webpage to different devices are more usable - different URL strings pointing to the same webpage are as well. 


1. Identi.ca’s URL structure doesn’t include the person’s name [example]- making the number less confusing, but the URL itself less usable.


