---
title: "Google Analytics goes async"
date: 2009-12-04 03:14:37 +0000
external-url: http://www.stevesouders.com/blog/2009/12/01/google-analytics-goes-async/
hash: 0dba1c60568c64d3ed1833ec1a6c300a
---

Today’s announcement that Google Analytics Launches Asynchronous Tracking is music to my ears. Not only does it make web sites faster, switching over to this async pattern improves uptime and increases the amount of analytics data gathered. I’ll touch on each of these three benefits, and wrap-up with an overview of the new code snippet.

Faster
The pain of loading JavaScript files is that they block the page from rendering and block other resources from downloading. There are workarounds to these problems. Chapter 4 of Even Faster Web Sites describes six techniques for Loading Scripts Without Blocking. One of those, the Script DOM Element approach, is the technique used in the new Google Analytics async pattern. Google Analytics’ ga.js file is a perfect example of a script that should be loaded asynchronously - it doesn’t add any content to the page, so we want to load it without blocking the images and stylesheets that give users what they really came to see.

Improved Uptime
What happens if a script takes a long time to load, or fails to load? Because scripts block rendering, users are left staring at an empty page. Google Analytics has an amazing infrastructure behind it, but any resource, especially from third parties, should be added cautiously. It’s great that the GA team is evangelizing a pattern that separates the web site and ga.js.

More Data
One workaround to the blocking problem is to move scripts to the bottom of the page. In fact, this is exactly what’s suggested in the old ga.js snippet. But this means users who leave a page quickly won’t generate any analytics data (they leave before the script at the bottom finishes loading). This is too good to believe - not only do you get a faster, more resilient page, but you actually get better insights into your traffic.

The Async Snippet
Just to be clear, ga.js will continue to work even if web site owners don’t make any changes. But, if you want a faster site, greater uptime, and more data, here’s what the new async snippet looks like:

var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-XXXXX-X']);
_gaq.push(['_trackPageview']);

(function() {
var ga = document.createElement('script');
ga.src = ('https:' == document.location.protocol ?
    'https://ssl' : 'http://www') +
    '.google-analytics.com/ga.js';
ga.setAttribute('async', 'true');
document.documentElement.firstChild.appendChild(ga);
})();
It’s extremely cool to see this pattern being evangelized for such a major piece of the Internet. A few items of note:


Obviously, you have to replace “UA-XXXXX-X” with your ID.
Since ga.js is being loaded asynchronously, we need a way for web site owners to couple their desired GA functions with the code when it finishes loading. This is done by pushing commands onto the Google Analytics queue object, _gaq.
Once all your callback commands are queued up, the ga.js script gets loaded. This is wrapped inside an anonymous function to avoid any namespace conflicts.
Inside the anonymous is where we see the Script DOM Element approach being used - with two nice improvements. A ’script’ element is created and its SRC is set to the appropriate ga.js URL. Looking ahead to support of asynchronous scripts in HTML5, the ‘async’ attribute is set to ‘true’. Very nice! The main benefit of this is it tells the browser that subsequent scripts can be executed immediately - they don’t have to wait for ga.js. The last line is adds the script element to the DOM. This is what triggers the actual download of ga.js. In most of my code I do document.getElementsByTagName(”head”)[0].appendChild, but that fails if the document doesn’t have a head element. This is a more robust implementation.

It’s always hard to find the right spot on the complexibility curve. This async snippet hits it just right. It’s slightly more complex than the old pattern, but not by much. Besides the benefits highlighted here, this new pattern is able to support more advanced usage patterns, including pushing an array of commands and pushing functions.

The theme driving much of my work this year is fast by default. I want high performance to be baked into the major components of the Web, so things are just fast. Seeing Google Analytics adopt this high performance async pattern is a huge win. But the proof is in the pudding. If you switch over to the new async pattern, measure how it affects your page load times and the amount of data gathered, and add a comment below. My prediction: 200ms faster and 10% more data. What do you see?

