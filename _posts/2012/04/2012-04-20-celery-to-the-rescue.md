---
title: "Celery to the rescue"
date: 2012-04-20 02:05:33 +0000
external-url: http://blog.bluelinescreative.com/?p=21
hash: a1f2357650542f3a49543c905282f5b9
annum:
    year: 2012
    month: 04
hostname: blog.bluelinescreative.com
---

We use this message broker for all of our stuff at 8thBridge, because Paul was a big advocate for it. It's worked really well thus far.  <blockquote> I was on the lookout for a way to manage long running tasks and kick of scheduled tasks without resorting to cron. Dont get me wrong, cron is cool and works well, but I wanted something a bit easier and that was easy to deploy with simple git hooks. My setup was Django with MongoDB for data storage. I had some requests that would collect a lot of data from external sources, like the Facebook Open Graph. I was doing more that just load the data which made the calls slooooow. We also needed to handle the rare state that Facebook was down. So celery came to the rescue. </blockquote> 
