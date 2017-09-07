---
title: "System Outages Explained"
date: 2009-03-14 04:40:12 +0000
external-url: https://uto.asu.edu/blog/2009/03/05/system-outages-explained/
hash: 3f3e58d94313e84b79188145554999df
---

 If you’ve been at ASU this semester, you’ve probably been inconvenienced by one of the five major system outages we’ve experienced so far this term. And as you might imagine, I’ve received more than a few emails from concerned members of the ASU Community expressing their frustration with being unable to access Blackboard, or My ASU or the various other services that have been affected in the past several weeks.

For example:

I am writing as an ASU graduate student, enrolled in an online 8-week, 3-hour graduate course this semester. The repeated system outages, including the one this morning — unable to get into Blackboard … AGAIN … unable to get into “System Health” to find out what’s going on and how long it will take to correct — has left me frustrated beyond words.

Or this one from an ASU professor:

This week, for the second time this semester, we have had large numbers of students unable to log in to Blackboard in order to take their weekly quiz. The problems seem to have been intermittent, but at a rough guess I would say that about 20 percent of the class has been affected.

I’d like everyone at ASU to know that here at the UTO, we all understand the frustration and lack of productivity that these outages cost and on behalf of myself and our team I apologize for the poor system performance we’ve had this term. This is not the level of service that you have come to expect from ASU and none of us are satisfied with our performance so far this term.

Given how central information technology is to the life of the University, we know that anything short of 100% uptime has become unacceptable. Our team works hard towards that goal, and we treat every system outage as a critical event. So we feel very keenly the amount of disruption that recent system instability has caused this term and we’re committed to correcting it.

Since January 1st, we’ve had five major incidents:


 Incident 1: On the afternoon of January 21/22, DARS degree audits and course catalog searches were unusually and inconveniently slow.
 Incident 2: From the evening of Feb. 1st to the morning of Feb 3rd, Internet access from ASU was unreliable.
 Incident 3: On February 5th, wireless access in a portion of the Tempe campus was unavailable. There was also a one hour interruption to My ASU and Citrix.
 Incident 4: For two hours on the morning of February 16th, Internet access from ASU was unreliable.
 Incident 5: On February 25th, many of ASU’s Web services were inaccessible for most of the day.

To a user experiencing these issues — even one who regularly visits our System Health site for updates and information — it must seem that all these outages must arise from some common cause. Our graduate student writes:

What’s even more troubling is that no one can explain what the problem is, or why it continues to happen, or what the plan is to get the University beyond this. Additionally, there’s been no communication on Blackboard or via email to students with any information.

 While the professor understands that people are working hard, but makes it clear that we can’t confuse effort with results:

I have generally found your staff to be knowledgeable and hardworking, so I am sure that this down time has been hard on them. I have no idea what the technical problems are behind these time out and login errors. But these issues really do create havoc in this kind of course and make it impossible to keep to the weekly class schedule.

As tempting as it is to think all these incidents are manifestations of the same thing, each of the 5 incidents we’ve experienced this term has arisen from a different proximate cause:


Incident 1 arose from an unusually large demand for DARS and Catalog services, a demand far greater than in prior terms.
Incident 2 was caused by a latent defect in our border firewall, which a rogue server exploited successfully overloaded the ASU network. Working with CISCO engineers, our team worked around the clock to identify and successfully correct the problem, but only after many hours of interruption.
Incident 3 was the result of a flood in BAC.
Incident 4 was caused by a mistake made by ASU’s Internet service provider that affected all of its clients.
Incident 5 was caused by a failure in the UPS backup system that protects the systems in the University data centers in the event of power outages. The resulting hard reset of the systems in the data center made service restoration complex — it took more than 8 hours to rebuild the systems and restore services.

But even if each incident has a separate technical cause, surely all of them are evidence of incompetence? With all these problems, surely its a sign that the people running these systems don’t know what they are about?

It’s certainly a sentiment that more than one writer has communicated as an outgrowth of their frustration. And it’s understandable. But understandable or not, it isn’t true.

Having witnessed first hand the level of dedication shown by the ASU technical professionals who design and maintain our systems and who scramble out of bed in the middle of the night or spend their weekends responding to the equipment failures, power outages, floods, denial of service attacks and hundreds of other failure modes that information systems are heir to, one thing I can assure is that at ASU we don’t lack for competent, dedicated, hard-working people committed to providing the information services the University requires.

Unfortunately, despite the dedication and skill of our systems people, to quote the t-shirt, “Stuff Happens.” And when it happens, we are either in position with redundant equipment and services that allow us to recover without interruption — or, if not, we have to rely on people to put the pieces back together again. While our investments in redundant equipment, our 24×7 monitoring, and the expertise and diligence of the ASU staff that oversee our systems successfully protect us from many different sources of outage, we remain vulnerable to system failures along many dimensions.

Over the long run, our overall systems performance is between 2 and 3 “nines.” That means they are available a little more than 99% of the time. Sounds pretty good until you realize that 1% of a year is 87 hours. And that doesn’t count planned outage windows. Include those and the number of off-line hours gets even worse. 90 hours a year may not seem like much, but if one of those hours is when you have a class that needs to take a quiz on Blackboard, its completely unacceptable.

So what does it take to achieve higher levels of reliability? What do we have to do to move our systems from 2 “nines” to 5? 

The answer, unfortunately, lies in additional investments, which is not what anyone wants to hear during the present economic situation. ASU’s primary data centers are more than 25 years old, and while they have served the University well, they were built for a day when IT was a luxury, not a necessity. We’ve helped the situation over the years, with some strategic investments and by working with strategic partners like Google and CedarCrestone. Because data services are our partners’ core business and they operate at scales much greater than ours, they’ve helped us increase our levels of reliability. We’ve also migrated some of the services we run ourselves from our older data centers to some of ASU’s newer facilities. But in doing so we’ve had to be conservative in our spending, moving gradually over time as hardware ages, to consolidate servers and storage and simplify their delivery.

And up until this term, we’d been pretty lucky. Term over term, our reliability was increasing. But clearly, this term, our lucky streak has run out.

I want you to know we’re doing more than waiting for our luck to change.

The president has challenged UTO to quickly put a plan together to get us a couple more “nines” of reliability. We are hard at work on that plan now. It will suggest accelerating migration out of the oldest data centers, moving additional services to strategic partners, improving power redundancy and backup. And obviously, it will be constrained by the realities of our fiscal situation. But I’m confident we will get the support we need to make things better for our community.

In my next post, I’ll tell you about some systems we’re going to release this month to improve our ability to communicate with you during those times when the information systems are having trouble. We’ve learned a lot from our recent history and I think we have a good plan to make things better.

As always, we’re interested in your comments on these issues, and any others. At the UTO, we’re committed to overcoming these recent issues and steadily improving system reliability. We’re sincerely sorry for the inconvenience when things don’t work right.

Thanks for your patience. We don’t take it for granted. 

