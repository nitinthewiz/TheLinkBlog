---
title: "2.9 Features Vote Results"
slug: 2-9-features-vote-results
date: 2009-08-05 11:55:40 -0500
external-url: http://wordpress.org/development/2009/07/2-9-vote-results/
hash: 67d6bd130c663eb113bdc1fc55c62157
year: 2009
month: 08
scheme: http
host: wordpress.org
path: /development/2009/07/2-9-vote-results/

---

Earlier this month, over 3500 of you responded to our survey asking you to help us prioritize some of the media features that had been suggested for the 2.9 release. While the exact features for 2.9 have not been hammered out yet, as we continue to match up developers with features, we wanted to share the survey results and let you know what we’re thinking in terms of approach.

First, the results. The first question, and the only one that was mandatory, asked what single media feature you would choose to include in version 2.9. The top vote-getter was standalone editable photo albums (as opposed to the current per-post gallery) at 17.5%, followed closely by easier embeds for videos and other third-party content at 16.5%. Next came basic image editing (such as rotating, cropping and resizing) at 13.7%, and post thumbnails (image teasers for posts featured on the home page) at 12.9%. The rest of the features each took less than ten percent of the vote. The full list came in like this:



The second question was optional (3406 people answered it), and asked you to rate each feature on a scale going from top priority down to definitely not for implementation priority. Results here were in line with the results from the first question, with most features rated as nice to have more often than anything else. The features that scored the highest in question 1 were more likely to have earned higher votes in the Top Priority column, but no feature was ranked as a Top Priority more often than it was ranked as a Nice to Have (though Media Albums, Easier Embeds and Post Thumbnails came close). The complete tabulations are shown in the chart below.



Question three was getting at the same thing, but in a more granular fashion, asking you to rank the eleven features in order of priority to you. As only one feature could be assigned to each position, this prevented people from assigning the same priority to multiple features, and we wondered if it would alter the results. Though some features got more recognition in this question, the overall rankings were still in line with the results from question 1. Here are the exact votes per feature/per position:



The fourth question asked for your preferences regarding including new media features in core, bundling them as plugins with the core download, or developing them as plugins but not bundling them with the core download. This vote was more interesting to watch. As the notice for the voting went first to the development community, then to the user community, it was possible to see a shift in the voting. Earlier in the voting cycle, there were more votes for bundling ‘core plugins’ for the advanced media features, while later votes skewed heavily toward just putting the features in core. This vote shows, I think, one of the differences between developer and user perspectives. While developers are heavily interested in keeping the core code lean and relying on plugins for advanced functionality, many users would prefer features they want to be included in core rather than being a separate plugin. The final tally on this question was 56.2% for including features in core, 38.1% for bundled plugins, and 5.7% for non-bundled plugins. The actual numbers:



Clearly this issue deserves more discussion, and the concept of how we move toward a system of canonical plugins and/or core “packages” intended for different use cases (CMS, photoblog, portfolio, etc) will be a big topic in the months ahead.

So where does that leave us regarding features coming down the road? When the vote closed, the results were discussed in the #wordpress-dev IRC chat to divvy up feature development.

The top-voted feature, standalone photo albums, is being worked on as a Google Summer of Code project by Rudolf Lai, under the mentorship of WordPress Lead Developer Mark Jaquith. The “pencils down” date for GSOC is in less than two weeks, at which point we’ll be assessing the state of Rudolf’s project. Hopefully, we’ll be able to incorporate it with 2.9 development, do some testing,  amend the code and/or UI as needed, and have this launch with the 2.9 release (in core or as plugin TBD). Undoubtedly, additional functionality will be contributed by core contributors who have also been working on media plugins.

Easier embeds, the second most popular feature, is being looked at in a couple of ways. One, more shortcodes for third-party services. Work on this has already begun. In addition, Viper007Bond, of Viper’s Video Quicktags plugin fame, has taken on the task of working on a way to improve the embed experience in core. We’re not sure quite how this will work yet, but stay tuned.

Adding some basic editing functions like 90-degree rotation, cropping and resizing was considered an obvious winner in the dev chat, and as several plugins handle this functionality, we’re hopeful it will be included soon.

Post thumbnails are being handled by Mark Jaquith, who has created this functionality before, with an assist from Scribu, who has a similar plugin in the repository.

Lower ranked features aren’t off the radar, but may take lower priority than some other (non-media) features we have in the works. One of my favorite 2.9 features is in trunk now, and changes the way we delete content. Goodbye, annoying popup asking me if I’m sure I want to delete a comment/post/etc. Hello, fast and quiet removal into a trash can, from which the content can be retrieved if it was deleted by accident. Think Gmail style. We’re also hoping to work on improving page management, though that has a number of technical issues that may cause it to be a 3.0 feature instead.

As always, you can keep track of development progress in a number of ways:
1. Keep track of Trac. Contribute a patch, test a patch, just read through tickets if you have some time to kill, whatever. There are over 500 tickets against the 2.9 milestone currently. Patches and testing can help us get that number down.

2. Follow Trac commits on Twitter. Don’t want to get involved in the nitty gritty, just want to see what’s getting committed? Follow wpdevel on Twitter and you’ll get core commit updates in your stream.

3. See what’s on the dev agenda. Each week for the IRC dev chat, there’s an agenda, created based on developer suggestions posted at wpdevel.wordpress.com. This blog also contains discussions about specific development issues.

4. Join the dev chat. The day changed this week, to accommodate European schedules. Chats are now held for one hour each week on Thursday at 21:00 UTC. That’s 5pm NYC, 2pm in California, etc. Chats are in the #wordpress-dev room at irc.freenode.com.

5. Watch this blog. If you’re not a developer and prefer to stick to major announcements, the occasional survey to help decide a feature, and security notices, just keep doing what you’re doing. Reading this blog will get you all of these things.

Thanks again for your help in prioritizing features for version 2.9, hopefully coming toward the end of the year to a server near you!

