---
title: "Adobe Releases BlazeDS, Open Source Version of LiveCycle Data Services"
date: 2007-12-12 23:00:27 -0600
external-url: http://techcrunch.com/2007/12/12/adobe-releases-blazeds-open-source-version-of-livecycle-data-services/
hash: 2d4dad16b0a75bfcd484ae17c93b7615
year: 2007
month: 12
scheme: http
host: techcrunch.com
path: /2007/12/12/adobe-releases-blazeds-open-source-version-of-livecycle-data-services/

---

One of the difficulties facing developers who want to create rich internet applications is HTMLs static nature, which requires that pages (unassisted by other scripting languages) must refresh in their entirety for any new information to load and appear. Technologies such as Ajax and Flash have been developed, at least in part, to overcome this limitation of HTML and facilitate the loading of new data onto a page without the requirement of a refresh. Many Web 2.0 companies have taken advantage of such technology in making their applications operate more seamlessly like desktop apps, but the technology still has quite a way to go. 

AJAX, for example, isnt designed to load new information onto a page unless that page has makes the initiative to request more data in the first place (i.e. the user interacts in a particular way with the page that causes it to ping the server for extra stuff). If you want to design an application that pushes information out to a page (say, up-to-the-second stock prices) whether or not the page has made a request, you can pull off the functionality with Ajax but your code wont be elegant and it probably wont be very efficient either.

Adobe is making a set of announcements tonight, the largest of which is meant to solve this issue of sending data back and forth with a visitors browser more elegantly, thereby helping developers create richer internet applications. The company has offered a product called LiveCycle Data Services (previously Flex Data Services) that works with Flex, a technology for building Flash applications. It provides advanced capabilities for Flash applets that allow them to connect up with server-side, back-end systems (in other words, to communicate back home with the server that originally loaded a page).

Tonight, Adobe is releasing an open sourced, beta version of LiveCycle Data Services called BlazeDS. The open source nature of BlazeDS will make it a welcome addition to the developers arsenal. But on top of opening it up, Adobe is adding extra functionality called HTTP streaming that enables clients (i.e. applets in end-user browsers) to initiate persistent connections with servers that allow those servers to push data back to the client whenever the server deems a transfer necessary (e.g. to send the latest stock price). The hope is that this technology will make it possible for data to flow both ways (from server and back) much more efficiently. The most notable difference for website visitors should be faster performance, and hopefully better functionality as well.

Adobe will also be making available something called LiveCycle Data Services Community Edition, basically BlazeDS but with Adobe quality control (i.e. certification) and support. This enterprise version of the technology, which the company compares to Red Hats enterprise offerings, will not be ready until early 2008 and pricing has yet to be disclosed.

In addition to the introduction of BlazeDS and its Community Edition, Adobe is releasing beta 3 versions of both Flex and AIR tonight. A commercial, non-open source version of BlazeDS (simply retaining the old name, LiveCycle Data Services) will also be maintained by Adobe and continue to offer some additional functionality not found in the open source version.
Crunch Network:  CrunchBoard because its time for you to find a new Job2.0
