---
title: "New directions in web architecture. Again."
date: 2010-11-16 18:00:00 +0000
external-url: http://radar.oreilly.com/2010/11/new-directions-in-web-architec.html
hash: c65729bb27e5e77526ae8eee4dd0e0a6
---

In 2005, Jesse James Garrett at Adaptive Path published the seminal blog "Ajax: A New Approach to Web Applications" and ushered in new age of web architecture.  Ajax meant using the possibilities latent in JavaScript (specifically, the XMLHttpRequest object) so that a web page could contact the server asynchronously and request new data.


This was revolutionary; within months, we were seeing pages that were more dynamic and interactive. Ajax short-circuited the submit/response loop that dominated web applications up to that time.  Instead of making an HTTP request, receiving an entire web page, and rendering that page as a replacement for the current page, the browser requested a chunk of data. It used that chunk of data to interact with the DOM and rewrite the page it was displaying on the fly.



Around the same time, the RESTful paradigm started taking hold. REST represented a much simpler, web-oriented way for servers to interact with their clients.  As Roy Fielding pointed out in his dissertation, the basic operations of the HTTP protocol were capable of providing general access to data; stateful applications could be built upon stateless protocols; hypermedia could be used to maintain application state.  Although Fielding's dissertation dates back to 2000, it took a few years of bad experience with SOAP and its heirs to realize its importance.  With REST, it becomes easier for a website to see itself as a source of data for machines to process, rather than as a source of content for humans to read. Websites become data servers.  





The HTML page you get from the new Twitter is largely a bunch of empty divs, with a big wad of JavaScript. The JavaScript is the entire application.


Important as Ajax and REST have been to the history of the web, each only represents half of a larger revolution.  And in the past few months, we've seen some new sites that have taken the revolution to its logical conclusion.  Specifically: take a look at the new Twitter.  It's a nice web application, sure -- but look at the HTML.  There's not much there.  The HTML page you get from Twitter is largely a bunch of empty divs, with a big wad of JavaScript.  What's happening?  The JavaScript is the entire application; the divs exist only to provide tags so the JavaScript can rewrite the DOM at will.  In turn, the JavaScript is constantly (and asynchronously) making requests from the Twitter site, which is just returning data from its API.  In fact, the Twitter site is returning the same data for its web page that it would return for its mobile app, for TweetDeck, or for any of the apps in the Twitter ecosystem. 



This design isn't particularly new; we've seen it ever since developers started reverse-engineering GMail and Google Maps to get ideas for their own projects.  Those big Google apps may have been the first examples of this architectural trend. They were certainly among the first to use JavaScript as a full-fledge client programming language.  But we're seeing many more sites built along these lines.  Why now, what does this shift mean, and why is it important?



"Why now" is perhaps the easiest question to answer.  A few short years ago, web developers only had one platform to support, and that was the "browser."  Granted, there were a dozen or so browsers of significance, and the browser world was riddled with incompatibilities.  We're in a different world now.  Browser compatibilities have been ironed out, to some extent (though conscientious developers still support "legacy" browsers, all the way back to IE6 or even IE5).  But it's no news that the most important new apps these days run on devices ranging from phones (iPhone, Android, BlackBerry, Windows Phone), tablets (iPad, Android/ChromeOS devices), and potentially ebook readers and other new devices.  With these new devices on the table, browser incompatibilities pale in significance.  It's another sign of the times that I can't conceive of an interesting application that doesn't access data across the network.  A static application that never accesses remote data -- that's so 1990s.


So, while it's tempting to say that the new age is characterized by the browser as platform, and that applications running in the browser can do anything that native code can do, that's looking in the wrong place.  HTML5 certainly ups the ante, as far as browser capabilities -- and is supported to some extent by all of the other devices we're concerned with.  But the real meaning and importance of this architectural shift is on the server side, driven both by the need to support many heterogenous device and application types, and by the primacy of live data in modern applications.



Related books and videos

Ajax
-- Head First Ajax
-- Ajax, TDG


REST
-- Rest in Practice   
-- RESTful Web Services    
-- RESTful Web Service Cookbook


HTML5
-- HTML5: Up and Running  
-- HTML5 Mobile Web Development (video)
In the browser-dominated world, static content and data were inevitably mixed.  Yes, we had templating systems that let developers separate static content and design elements from data.  But once the application server did its magic, what was delivered to the browser was HTML pages mixing data with other content.  Browsers were similar enough that, with some browser detection hacks on both the server and client side, it was relatively easy (though a pain) to generate pages that would run anywhere.  That doesn't work any more. It's naive to think that you can wrap some HTML around data and be done with the job; the chances are that you're leaving a huge chunk of your human audience behind, and making things more difficult for another audience -- machines that just want to consume your data.  To build a modern application, developers must focus on the data: they must see themselves as data providers, they must develop documented and stable public APIs for accessing their data.  Over the past few years, we've realized the importance of data.  What's the value of Google without the data behind it?  Or Facebook? Or, going back 15 or so years, GNN?  It took a long time for us to understand the importance of data, as opposed to "content." But when you've gotten that lesson, your design goals change: designing and publishing a stable API to a data service becomes the highest priority.  


That's the driving force behind this architectural shift. Front ends, user interfaces, clients, apps, whatever you decide to call them, don't disappear.  But we have learned how important it is to keep the data interface separate from the user interface.  Your next project will probably have multiple front ends, some delivered through HTML5, and some delivered through native code. Building them on a common data API is going to be much cleaner and simpler.  In addition, third parties can build their own apps on top of your API. An important component of Twitter's success has been the ecosystem of applications that have built on their data: TweetDeck, TweetGrid, Tweetie, etc.; Twitdom, the Twitter applications directory, lists more than 1,800 apps.  Until the "new Twitter" went live, the Twitter website was significantly less capable than most of the third-party apps.



Although it has been a long time coming, we're finally finishing the revolution that started with Ajax.  Get data that users care about, make it available via an API, provide a data presence that's distinct from your HTML-based web presence, and build multiple front ends to serve your customers, on whatever platforms they care about.  Your value is in the data.



Related:


 What is data science?
 The SMAQ stack for big data
 Data as a service
 Building data startups
 Lies, damn lies, and visualizations





   

