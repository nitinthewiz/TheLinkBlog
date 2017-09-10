---
title: "NginX Reporting for Duty"
date: 2008-06-09 18:45:42 +0000
external-url: http://www.opticality.com/blog/2008/06/09/nginx-reporting-for-duty/
hash: a841a1e5855a96b5e4c179681deabf9f
annum:
    year: 2008
    month: 06
url-parts:
    scheme: http
    host: www.opticality.com
    path: /blog/2008/06/09/nginx-reporting-for-duty/

---

Last week, my friend Jamie Thingelstad tweeted from the Rails Conference that he was considering switching to NginX (I’ll probably drop the caps starting now) after sitting in on a session about it.

Prior to that mention, I had only heard of it once, when an internal tech email at Zope Corporation mentioned that one of our partners was happy with it as their web server. I didn’t pay too much attention to it at the time…

I was curious, so I downloaded and built nginx-0.7.1. Since there is no equivalent to mod_php for nginx, I also had to decide on a strategy for managing PHP via FastCGI for this blog (I use Zope to serve up all other publicly available content on the site). It seemed that the most prevalent solution out there was to use spawn-fcgi, part of the lighttpd web server package (another very popular alternative to Apache, which is what I was using).

After searching further, I noticed that a number of people were recommending a package called php-fpm (PHP FastCGI Process Manager). I decided that I’d give this one a try first.

Finally, while researching all of this, in particular noting results by WordPress users (after all, that was my one use case for doing this), I also decided to install an op-code cacher for the first time ever, settling on XCache (also brought to you by the fine folks who bring you Lighttpd!).

Within minutes I had nginx installed and running, serving content on an alternate port (so Apache was still serving all production content on port 80). Shortly thereafter I had php-fpm installed and running as well. XCache installed easily too, but it did take me a few minutes longer to correctly change one particular entry in the conf file.

I had some serious frustrations along the way, all of which were due to a fundamental lack of understanding on my part of how things are ultimately supposed to work (meaning, nothing was wrong with the software, just with my configuration of it!), but to underscore the bottom line, nginx/php-fpm/xcache are all in production now. If you’re reading this in your RSS reader, or in a browser, it was delivered to you by that combination of software (unless this is far in the future, and I’ve changed again).  

If you aren’t interested in the twists and turns of getting this into production, then read no further, as the above tells the story. If you care to know what pitfalls I encountered, and what I had to do to overcome them, read on…

Getting everything set up to generically serve content on the alternate port was trivial. Like I said earlier, I was serving test pages in minutes (even before downloading php-fpm and xcache). In that regard, you have to love the simplicity of nginx!

With extremely little effort, I was able to write a single line proxy_pass rule in nginx to serve up all of my Zope content on the alternate port. Done! I figured that this was going to be really easy, since the WordPress/PHP stuff has so many more real world examples documented. Oops, I was wrong.

To begin with, the main reason that I was wrong is due specifically to WordPress (hereinafter, WP), and not nginx or PHP whatsoever. Basically, I ran into the same problem the first time I fired up XAMPP on my laptop to run a local copy of my production WP installation.

WP stores the canonical name of blog in the database, and returns it on every request. This means that your browser automatically gets redirects, which at a minimum (in the nginx case) dropped the alternate port, and in the XAMPP case, replaced localhost with www.opticality.com. The fix for XAMPP was easy (yet still annoying!). I had to go into the MySQL database, and change all references to www.opticality.com to localhost.

In the case of nginx, I couldn’t do that, since I was testing on my live production server. In retrospect, this was stupid (and cost me hours of extra time), since I have a test server I could have installed it on, run it on port 80, change the blog name, etc., and been sure that I had everything right before copying over the config. Of course, I learned a ton more by keeping my feet to the fire, especially when my public site was hosed (which it was a number of times this weekend!), perhaps shortening the overall learning experience due to necessity!  

That made testing WP extremely painful. Instead, I tested some standalone php scripts, and some other php-based systems that I have installed on the server, but don’t typically activate. All worked perfectly (including my ability to watch xcache return hits and misses from the op-code cache), so I was growing in my confidence.

Sometime late Wednesday night I was mentally prepared to cut over (since switching back to Apache would only take a few seconds anyway), but I decided to wait until the weekend, when traffic to this blog is nearly non-existent (come on folks, you can do something about that!).  

Saturday morning, very early, I stopped Apache, reloaded nginx with a configuration that pointed to port 80, and held my breath. I was amazed that everything seemed to be working perfectly, on the first shot! I moved on to other things.

Later in the day, I visited the admin interface for WP (Firefox is my default browser, though I obviously have IE installed as well, and for yucks, I also have Safari, which I very rarely launch). Oh oh, I had zero styling. Clearly, something was causing the CSS not to be applied! I quickly ran back to the retail interface and thankfully, that was still being served up correctly. That meant that I could take my time to fix this problem, as it only affected me!

I turned on debugging in nginx and saw that the CSS was indeed being sent to the browser. That’s not good either, as it seemed that this wasn’t going to be a simple one-line fix in nginx.

Yesterday morning, after nginx had been in production for 24 hours, I decided to check out IE for the admin pages. They showed correctly! Firefox was still showing zero styling. I compared the source downloads, and Firefox was larger, but had everything that IE had as well (including the CSS). At first I incorrectly assumed that perhaps it was the extra ie.css that IE was applying, and Firefox was ignoring, but that really couldn’t have been it, and I didn’t waste any time on that.

Now that I had a data point, I started Googling. It took me quite a while to find a relevant hit (which still surprises me!), and I had to get pretty creative in my search terms. Finally, one solitary forum hit for a php-based product called Etomite CMS (I had never heard of it before) describing exactly what was happening to me. Here’s the link to the forum post.

OK, their take was that the CSS was coming down with a MIME type of text/html, rather than the correct: text/css. I went back to Firefox, and did what I should have done at the beginning (my only excuse is that I’ve never had this type of use case to debug before!). I enabled Firebug on the admin page (I already had Firebug installed, but I’ve rarely ever needed it).

Immediately, I could see that the CSS had been downloaded (I knew it was sent from the nginx logs, but now I knew it was received and processed). I could also see instantly that the CSS was not recognized as CSS. Going to the Net tab in Firebug revealed the headers for each individual request, and indeed, all of the CSS came back with text/html as the type. So, IE ignores that, and applies the CSS anyway, because it sees the extension (I’m guessing), but Firefox doesn’t. Fair enough.

But, why is it coming back text/html? I checked the nginx MIME types file, and CSS was coded correctly (I didn’t touch that file anyway). Looking at the headers again, I spotted the problem. All of the CSS files were being returned by PHP, not statically by nginx. In other words, my nginx config was wrong (even though it was otherwise working), as it was passing requests for CSS files to the FastCGI PHP process, and getting back an incorrect MIME type for those files!

A very cursory search didn’t reveal how I would tell PHP to return a correct MIME type. I’ll save that investigation for another day, as it would have been an immediate, but suboptimal solution anyway, since these files can be served faster by nginx to begin with. That meant figuring out what was wrong with my nginx configuration.

The docs for nginx are pretty good (with a few exceptions, but I’m not quibbling). There are also a ton of cookbook examples, some good and detailed, some should be deleted until they are completed. I realized pretty quickly that even though my retail interface was working, I had less of an understanding of how the different stanzas in my configuration file were interacting (specifically, the location directives).

I really didn’t want to revert to Apache, so I decided to experiment on the live server. It was Sunday evening, and I figured traffic would be relatively light. Sparing you (only a drop, given how long this is already), I hosed the server multiple times. I could see that search bot requests were getting errors, and my tests were returning a variety of errors as well. At one point, I had nearly everything working, and then promptly screwed it up worse than before.  

Eventually, under a lot of pressure (put on myself only by me), I simplified my configuration file, and it all started working, retail and admin alike. Whew. I’m now serving all static files directly from the file system, and all php files through the FastCGI process. The world is safe for blog readers again.  

Like I said above, the problem was never with nginx, though I can’t say the same thing for PHP returning text/html for a CSS file. Clearly, PHP shouldn’t have to process those files, but if it does, it should do the right thing in setting the MIME type. Of course, if it had, I would likely have never noticed that my static files weren’t being served as I intended them!

One real complaint, aimed at nginx. Since I use the proxy_pass directive to serve up all Zope content (and like I said, that worked from the first shot, and has worked ever since!), I was quite frustrated by the limitations on where it can be used, and how. Specifically, it can’t be used within a regular expression based if test, even if you aren’t using variable substitution in the proxy_pass itself. That simply doesn’t make sense to me. And, now that I mentioned it, there are other rules about when/how you can use variable substitution as well.

Clearly, I got it working, so the above isn’t a giant complaint, it just eludes my current understanding. As for getting the rest to work, I have a better understanding than I did, but I’m sure that if I were to muck around a little more, which I’ll inevitably do, I’ll break it again, showing that my understanding is still at the beginner level.

In any case, for the moment, it’s doing what I intended, and is in production.  

Aside from Jamie’s pointer, in doing the initial research, what got me excited was reading that WordPress.com had switched to nginx for their load balancing (and might eventually switch for their web serving as well), and that Fastmail is using nginx for the IMAP/POP mail proxying as well. Clearly, nginx is ready for prime time (my puny blog notwithstanding). 


Tags: Apache, blog software, Computers, Etomite, FastCGI, Firebug, Lighttpd, NginX, php-fpm, wordpress, XCache

Related posts

WordPress Ate My Posting Date (0)
Welcome WordPress 2.5 (0)
Testing Windows Live Writer (0)
CSS Hack Added (0)
Yet Another Theme Update (0)

