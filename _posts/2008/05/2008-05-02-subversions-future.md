---
title: "Subversion’s Future?"
date: 2008-05-02 14:31:17 +0000
external-url: http://mjtsai.com/blog/2008/05/02/subversions-future/
hash: 947de56816895105dfaeba20629baf56
year: 2008
month: 05
scheme: http
host: mjtsai.com
path: /blog/2008/05/02/subversions-future/

---

Ben Collins-Sussman:


I’ve chatted with other developers, and we’ve all come to some similar private conclusions about Subversion’s future.  First, we think that this will probably be the “final” centralized system that gets written in the open source world — it represents the end-of-the-line for this model of code collaboration.  It will continue to be used for many years, but specifically it will gain huge mindshare in the corporate world, while (eventually) losing mindshare to distributed systems in the open-source arena.

The thing is, DVCSs can be preferable to Subversion, even when used in a centralized style. That’s mostly how I use Git, but I appreciate its speed, the efficiency of its disk use (much less space used and many fewer files, which really matter for multi-gigabyte repositories), merging, and not having to worry about .svn folders getting clobbered or moved to the wrong place when I reorganize. Subversion works well, and there are a lot of tools that integrate with it, but as the ecosystems for the DVCSs improve, I can’t see why they wouldn’t start to gain mindshare and marketshare, even outside the open-source world.

Secondly, I don’t really see why Collins-Sussman thinks that Subversion’s advantage is with large projects. I think it’s the opposite.

