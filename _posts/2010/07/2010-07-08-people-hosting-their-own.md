---
title: "People hosting their own servers"
date: 2010-07-08 09:49:31 +0000
external-url: http://scripting.com/stories/2010/07/08/peopleHostingTheirOwnServe.html
hash: bba3426ff4a063ca7f5f44cceb445a59
annum:
    year: 2010
    month: 07
url-parts:
    scheme: http
    host: scripting.com
    path: /stories/2010/07/08/peopleHostingTheirOwnServe.html

---

My Scripting2 to-do list is getting small again, but there are still some big items there. One of them is to get an Amazon AMI ready for people to create their own blogging servers.

My goal is to make it as turnkey as possible to set up your own server. One of my frustrations with WordPress is that you have to understand so much about hosting before you start hosting. There's so much you have to understand before you start. It's kind of a Catch-22. You have to be highly motivated, you're making a real commitment. That's why so many people go with wordpress.com. (None of this is presented as fact, just my conjecture.)

With Scripting2 there will be, at first, a scarcity of hosting options. I want people to seriously consider setting up their own EC2 server. It costs about $90 per month, and it can host dozens of bloggers using Scripting2 (in theory, that's what we're going to find out). The economics work for me. With Radio and Manila, I had to get into the hosting business. This time, I am determined not to be the central point of failure. Eventually it made so sick that I had to drop the ball. This time I don't want it to be dependent on me. That was the mistake last time.

My role is to work on software and to be a community leader. That's what I do best. 

Also, by having people host their own servers from the start, we get past the bottleneck of the typical "User Generated Content" play in the tech world. In that world, the users are like little hamsters in cages spinning around the wheels that drive ad impressions that generate revenue for the tech company and stock options of the programmers go up in value, and the little hamsters have the satisfaction of knowing they helped make other people rich. This always struck me as out of balance. 

It works when the founders can find a quick exit as the YouTube guys did. But in the more common case, the company drifts and the platform suffers, and the users wait and things never get better.

The WordPress guys found a better formula, by offering people the option of hosting their own blogs on their own hardware for free. Even your wordpress.com blog is free. You only pay when you get serious about your blog. When you need features that serious people need. That ecosystem has a much better feel to it. And they get to relax, get rich, and the users have their independence. 

At my point in life, I'm less concerned with making money myself, and more concerned about setting up something that works, long-term. I was looking for an answer and along came Amazon and I couldn't believe what I was seeing. With EC2, I get to create my own operating system, and offer it to you. Eventually I can even ask for some of the money to flow back to me to fund the continued development of the software. Maybe I'll even get rich from it, that wouldn't be so terrible. 

Unlike the WordPress ecosystem, that had evolved to create entities like Bluehost, who have confusing startup plans, we'll have one that's a simple howto that takes at most an hour from beginning to end, and has zero commitment to anyone. You can launch the server, create your blog, and after one day decide it's not for you, and owe Amazon less than $1 for the experience. (It's all charged to your credit card the same way you pay for books or clothes.)

So now I'm swinging back to polish the AMI, get it so that the code within auto-updates properly, and then at some point I'll be looking for guinea pigs er testers to try it out. 

