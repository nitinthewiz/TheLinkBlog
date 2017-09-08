---
title: "What Are We Waiting For?"
date: 2009-05-27 16:35:14 +0000
external-url: http://kernest.com/blog/archive/what-are-we-waiting-for
hash: 02939e068e29baada4f40a7f8b54cbf0
annum:
    year: 2009
    month: 05
hostname: kernest.com
---

“Thus, as we consider integrating real fonts into our designs, we must navigate between browsers that support @font-face now (Safari), those that will do so soon (Opera, Chrome, Firefox), and the one that possibly never will (IE, with a dwindling but still overwhelming market share).”  - Jeffrey Zeldman

Zeldman’s right. I also see a bigger issue.

@font-face still won’t be supported on the Kindle, the iPhone, the Blackberry, the XBox, Android, etc. All of those devices and browsers provide a very different font rendering experience than Safari on a Mac.

Even that font rendering experience is different than Firefox on Ubuntu or even Internet Explorer on Windows (pick a version).

If the goal is rock solid visual consistency across all - web designers lost the battle long ago. 

If the goal instead is to provide the best possible experience within the constraints of a given browser environment, then….

There isn’t anything technical preventing web sites from specifying fonts that are native to specific platforms within the regular font-family CSS declaration.

I’m optimistic about the opportunity  @font-face provides to type designers and web designers. 

I also see very little reason Arial or Times New Roman should ever be listed first in font-family listing.

We don’t need to wait until Firefox 3.5 to spec Jazz LET or Big Caslon. They ship with Macs today.

