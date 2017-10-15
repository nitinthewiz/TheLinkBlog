---
title: "Why We Need An Open Wireless Movement"
date: 2011-04-28 17:08:30 -0500
external-url: http://www.eff.org/deeplinks/2011/04/open-wireless-movement
hash: 99a739f9262c561066036ede977f54fa
year: 2011
month: 04
scheme: http
host: www.eff.org
path: /deeplinks/2011/04/open-wireless-movement

---

If you sometimes find yourself needing an open wireless network in order to check your email from a car, a street corner, or a park, you may have noticed that they're getting harder to find.

Stories like the one over the weekend about a bunch of police breaking down an innocent  man's door because he happened to leave his network open, as well as general fears about slow networks and online privacy, are convincing many people to password-lock their WiFi routers.

The gradual disappearance of open wireless networks is a tragedy of the commons, with a confusing twist of privacy and security debate.  This essay explains why the progressive locking of wireless networks is harmful — for convenience, for privacy and for efficient use of the electromagnetic spectrum.

We will need a political and technological "Open Wireless Movement" to reverse the degradation of this indispensable component of the Internet's infrastructure.  Part of the task will simply be reminding people that opening their WiFi is the socially responsible thing to do, and explaining that individuals who choose to do so can enjoy the same legal protections against liability as any other Internet access provider.1   Individuals, including Bruce Schneier and Cory Doctorow, have laid some of the groundwork.  It's time to spead the message far and wide.

But an Open Wireless Movement will also need to do technical work: we need to build new technologies to ensure that people have an easy way to share a portion of their bandwidth without affecting the performance of their own network connections while at the same time ensuring that there is absolutely no privacy downside to running an open wireless network.

The wireless world we ought to live in
Most of us have had the experience of tremendous inconvenience because of a lack of Internet access.  Being lost in a strange place with no way to find a map; having an urgent email to send with no way to do so; trying to meet a friend with no way to contact them.  Even if we have data plans for our mobile phones, we've probably had these experience in cities or countries where our phones don't have coverage or don't have coverage for less-than-extortionate prices.  We may even experience this problem at home, when our Internet connection dies while we urgently need to use it.  

Finding yourself in one of these binds is a bit like finding yourself parched and thirsty while everyone around you is sipping from nice tall glasses of iced water, or finding yourself cold and drenched in a rain storm because nobody will let you under their umbrella.  At those moments when you are lost, or missing a deadline, or failing to meet your friend, it is almost always true that Internet data links are traveling through your body in the form of electromagnetic wireless signals — it's just that people have chosen to lock those networks so that you can't make use of them.

A tragedy of the commons
When people turn on WEP or WPA encryption for their networks deliberately, there are two common reasons: a desire to prevent their neighbors from "free riding" on their connections; and a fear that unencrypted WiFi is a security or privacy risk.  Both of those reasons have a degree of legitimacy, but neither of them changes the fact that we would be better off if there were more open networks.  Also, both of these problems could be solved without password locking our networks.  What we need, instead, is to develop and deploy better WiFi protocols.

Let's focus on the first issue for a moment: traffic prioritization.

Many people would like to have the fastest network connection possible, and for that reason are reluctant to let their neighbors share their link.  After all, if your neighbor is streaming music or watching YouTube videos on your WiFi, that's going to slow your traffic down a bit!  But those same people would probably be willing to give up some bandwidth at home from time to time, in exchange for having free open wireless everywhere else.  In other words, we'd all be better off if we all left our WiFi open, but we each benefit slightly if we close our WiFi.  Our failure to work together prevents us from enjoying better, more widespread Internet access.

The best solution to this problem is to have WiFi routers which make it very easy to share a certain amount of bandwidth via an open network, but simultaneously provide an encrypted WPA2 network that gets priority over the open network.  Some modern routers already support multiple networks like this, but we need a very simple, single-click or default setting to get the prioritization right.

Securing the Future for Open WiFi
If the problem of open WiFi was just about convincing people to share their connections, we'd be in a better situation.  Enough people understand the importance of sharing that we'd have open networks more or less everywhere.

The problem that's really killing open WiFi is the idea that an unlocked network is a security and privacy risk.

This idea is only partially true.  Computer security experts will argue at great length about whether WEP, WPA and WPA2 actually provide security, or just a false sense of security.  Both sides are partially correct: none of these protocols will make anyone safe from hacking or malware (WEP is of course trivial to break, and WPA2 is often easy to break in practice), but it's also true that even a broken cryptosystem increases the effort that someone nearby has to go to in order to eavesdrop, and may therefore sometimes prevent eavesdropping.

It doesn't really matter that WiFi encryption is a poor defense against eavesdropping: most computer users only understand the simple message that having encryption is good, so they encrypt their network.  The real problem isn't that people are encrypting their WiFi: it's that the encryption prevents them from sharing their WiFi with their friends, neighbours, and strangers wandering past their houses who happen to be lost and in need of a digital map.

We need WiFi that is open and encrypted at the same time!
Insofar as there is some privacy (and psychological) benefit to using an encrypted WiFi network, there's actually no reason why users of open wifi shouldn't get those benefits too!

There is currently no WiFi protocol that allows anybody to join the network, while using link-layer encryption to prevent each network member from eavesdropping on the others.  But such a protocol should exist.  There are some technical details to work through, but they are manageable.2

In fact, this proposed protocol offers some privacy/security benefits not available in shared-passphrase WPA2, which is the strongest  easy-to-deploy WiFi encryption system.  Under WPA2 all the users on the network can calculate each others' session keys and eavesdrop on each other.  With our suggested design, that would cease to be possible.

The Unintuitive Benefits of Open Wireless
Since 1994, the United States government has auctioned off huge portions of the electromagnetic spectrum to telecommunications companies.  WiFi operates in tiny scraps of spectrum that were left over from the auctions.  Similar processes have occurred in many other countries.

But WiFi networks (especially modern 802.11N networks) turn out to make inherently much more efficient use of spectrum than systems of widely spaced cell phone towers.  This results from a property of wireless protocols called area spectral efficiency: basically, if your data only has to travel to a nearby router, the same frequency range can be used for someone else's data around the corner or across the street.  In contrast, if your data needs to travel all the way to a cell tower, nobody else in between can use that same portion of spectrum.

If we want a future where anyone can watch high definition movies or make video calls from anywhere without wires, what we need is short-range networks with routers everywhere — like the one we'd have if everyone opened their WiFi.

What Needs to be Done
EFF will be working with other organizations to launch an Open Wireless Movement in the near future.   In the mean time, we're keen to hear from technologists with wireless expertise who would like to help us work on the protocol engineering tasks that are needed to make network sharing easier from a privacy and bandwidth-sharing perspective.  You can write to us at openwireless@eff.org.


1. If you run an open wireless network, you may be able to receive significant legal protection from Section 230 of the CDA (against civil and state criminal liability for what others publish through the service) and Section 512 of the DMCA (against copyright claims based on what others use the service for).  While these protections are not complete, EFF regularly engages in impact litigation to help ensure that these laws offer as strong protection to network operators as possible.
2. That kind of wireless network could use asymmetric cryptography to generate secret session keys for each user.  The main challenge with this design is how to prevent man in the middle attacks.  Wireless routers do not have canonical names, so they cannot be issued certificates in the same way that, say, TLS encrypted websites are.  A feasible alternative is the trust-on-first-use design employed by SSH: the first time you connect to a wireless network, you might have to assume that the router's key is correct, but you will be notified if ever changes (which would mean that there is a new router, or the beginning or end of a man-in-the-middle attack).  If you can actually see the router, you don't have to assume that the key is correct because you can check it against a number on the box itself.  For other users, the security could be improved by using GPS, or some other means of remembering not only the keys of each router but also whether it was expected to be present in a given location

