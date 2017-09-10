---
title: "Four short links: 5 October 2011"
date: 2011-10-05 10:30:00 +0000
external-url: http://radar.oreilly.com/2011/10/four-short-links-5-october-201-1.html
hash: 1ff6fe73a18c30032641f5bd72ed941d
annum:
    year: 2011
    month: 10
url-parts:
    scheme: http
    host: radar.oreilly.com
    path: /2011/10/four-short-links-5-october-201-1.html

---


Ghostery -- a browser plugin to block trackers, web bugs, dodgy scripts, ads, and anything else you care to remove from your browsing experience.  It looks like a very well done adblocker, but it's done (a) closed-source and (b) for-profit.  Blocking trackers is something every browser *should* do, but because browser makers make (or hope to make) money from ads, they don't.  In theory, Mozilla should do it.  Even if they were to take up the mantle, though, they're unlikely to make anything for IE or Chrome.  So it's in the hands of companies with inarticulate business models. (via Andy Baio)
Perspectives -- Firefox plugin that lets you know when you've encountered an SSL certificate that's different from the ones that other Perspectives users see (e.g., you're being man-in-the-middled by Iran). (via Francois Marier)
Always Connected -- "I've got a full day of staring at glowing rectangles ahead of me! Better get started ...".  I have made mornings and evenings backlight-free zones in an effort to carve out some of the day free of glowing rectangles. (I do still read myself to sleep on the Kindle, though, but it's not backlit)
Is Teaching MapReduce Healthy for Students? -- Google’s narrow MapReduce API conflates logical semantics (define a function over all items in a collection) with an expensive physical implementation (utilize a parallel barrier). As it happens, many common cluster-wide operations over a collection of items do not require a barrier even though they may require all-to-all communication.  But there’s no way to tell the API whether a particular Reduce method has that property, so the runtime always does the most expensive thing imaginable in distributed coordination: global synchronization.  Detailed and interesting criticism of whether Hadoop is the BASIC of parallel tools. (via Pete Warden)




    

