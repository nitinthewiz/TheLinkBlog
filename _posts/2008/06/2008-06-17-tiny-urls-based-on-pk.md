---
title: "Tiny URLs based on pk"
date: 2008-06-17 14:59:29 -0500
external-url: http://blog.leahculver.com/2008/06/tiny-urls-based-on-pk.html
hash: f2ad6cf30daa9b365b6b10f9dc737872
year: 2008
month: 06
scheme: http
host: blog.leahculver.com
path: /2008/06/tiny-urls-based-on-pk.html

---

Ive been wanting to make a short url for Pownce permalink pages for an upcoming project. Pownce note permalink pages on the website currently look like this: http://pownce.com/leahculver/notes/2477365/

The generic form is:  http://pownce.com/&lt;sender username&gt;/note/&lt;note id&gt;/

While these URLs are pretty descriptive and simple, theyre also a bit long. The note id is really the only piece of information we need from the URL, the sender username is just fluff. Id like to have an alternate URL that is quite a lot shorter that redirects to the final (longer) URL.

I think the following set of characters look pretty good in URLs:
23456789abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ
Basically, 0-9a-zA-Z minus the confusing characters: 01loIO.

Now, its fairly simple to convert a base 10 note id to this strange base 56 set assuming that the character order (digit-lower-upper) is maintained. The (very freshman-like) code is here.

The result is something like http://pownce.com/~g7YF/ will redirect to http://pownce.com/leahculver/notes/2477365/

This works very well for finding a note page based off a note id. Its also super handy for making a generic tiny-urlizing service. The only data that needs to be stored is the real URL and a numerical id - the unique primary key for the database row! I have no desire to run a tiny-urlizing service, but this would probably be how Id do it.

Note: Pownce user profile pages are in the form http://pownce.com/&lt;username&gt;/ so a non-username character, such as ~ can signify that this is a note permalink as oppose to a profile page. I like the tilde, its got style a bit confusing for the Unix folks though. Since its the code isnt in production yet, other character suggestions are welcome.
