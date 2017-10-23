---
title: "Ask 37signals: Why did you restart Highrise?"
slug: ask-37signals-why-did-you-restart-highrise
date: 2008-01-09 11:34:00 -0600
external-url: http://www.37signals.com/svn/posts/772-ask-37signals-why-did-you-restart-highrise
hash: 276c6ec38650e7597c1fdb4168147043
year: 2008
month: 01
scheme: http
host: www.37signals.com
path: /svn/posts/772-ask-37signals-why-did-you-restart-highrise

---

Johni Brown asks:



Can you describe initial direction you took when developing Highrise, before you started over? How did it differ from today’s Highrise? What aspect of it were you unhappy with, and why?

The primary problem with the first version of Highrise was that we didn’t use it ourselves. It was built on fantasy requirements of what some people might need one day. That’s an incredibly hard way to build software. And it certainly isn’t our way of building software.



Here’s an early (ugly) screenshot from the initial direction. Lots of unstyled stuff, but hopefully it gives you an idea of the complexity we didn’t like.







The focus on “some people” lead us down the path of “they might also need this” and “it would probably be cool to have that”. Before we knew it, the create a new note screen had a barrage of options that needed to be set before you could post. It was too cumbersome, too slow, and surprisingly too rigid despite trying to be flexible. (The aha moment for us was contrasting the ease of getting data into Campfire vs Highrise at the time).



Getting too clever with language and permissions
We also got lost down the rabbit hole of cleverness a few times. We wanted categories for your notes that would align to natural language. I forget the specifics exactly, but it was akin to “David has completed a phone call with Jason”. Where “phone call” would be the category. But how do you figure out what the joining words would be when the category is “fax”? “David has completed a fax with Jason” doesn’t really work. We tried too hard for too long to be clever on wording when it really doesn’t matter all that much.



The second rabbit hole was permissions. Permissions is always a deep, dark dungeon that you really would rather not venture into. But some times dragons need slaying and so we did. We started out with a ridiculously flexible system that allowed you to mix and match any number of groups and people together. You could have a note visible by “Marketing, Programming, John, and Jane”. That proved to be incredibly complex on both the implementation side and the UI side. But for a long time we couldn’t let go because we were caught up chasing edge cases.



The promises that got us back on track
So when we finally realized that this wasn’t going to work, we rebooted the project with a number of promises:



Design for yourself, make everyone on the team want to use Highrise—not just Jason talking to journalists, but Ryan dealing with his mechanic as well
Not every edge case needs solving—yes, there might be a case where having both Marketing and Jane see something but not Joe, but it’s not worth the complexity of enabling that case.
Start using the product right away—a lot of “what ifs” and “wouldn’t it be cools” just go away when you actually start using something and discover what really matters.

As you can see, these lessons are nothing new. We’ve been preaching these ideas for a long time, but living them is so much harder. When we let the core principles of Getting Real slide, not even we could produce software worth a damn.



Got a question for us?
Got a question about design, business, marketing, etc? We’re happy to try to provide some insight into how we’d tackle the problem. Just email svn [at] 37signals dot com with the subject “Ask 37signals”. Thanks.

  

