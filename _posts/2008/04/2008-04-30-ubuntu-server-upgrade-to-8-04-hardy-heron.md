---
title: "Ubuntu Server Upgrade to 8.04 Hardy Heron"
slug: ubuntu-server-upgrade-to-8-04-hardy-heron
date: 2008-04-30 02:30:23 -0500
external-url: http://hostingfu.com/article/ubuntu-server-upgrade-8-04-hardy-heron
hash: e2c8733207713f042c1c823775842678
year: 2008
month: 04
scheme: http
host: hostingfu.com
path: /article/ubuntu-server-upgrade-8-04-hardy-heron

---

First of all I have to confess that I have been very busy over the last months or two and have not really been motivated to write. I have a few other projects happening at the same time — at work, at home, at church and at my other websites, and I apologise for neglecting this blog. Hopefully I will get back to writing here again. I am also hoping to write shorter pieces — maybe just 2 or 3 paragraphs — so I can make more frequent posts.


Now, something I have been doing over the last couple of days is to upgrade my Ubuntu servers to 8.04 Hardy Heron, which was “officially” released last Thursday. Now it has been almost two months since I wrote my last blog post, which was about switching from Gentoo to Ubuntu, and now most servers/VPSs that I am personally responsible for (except those at work) are running Ubuntu. Hardy Heron is a LTS (Long Term Support) release which I am hoping to build most my apps on for the next 2 weeks. Upgrading to it from previous Ubuntu releases is surprisingly trivial.





# apt-get update
# apt-get upgrade
# apt-get install update-manager-core
# do-release-upgrade
[blah blah blah]


The first two steps are only there to ensure you already have latest updates for the current release. It’s quite possible that “update-manager-core” has already been installed. “do-release-upgrade” does all the bulky work — checking whether a new release is available, checking how many packages need to be updated, download, unpackage and install all packages + resolving potential conflicts, etc. And at the end it just reboots your server. Wait for a minute and two, connect back in and hopefully you will be running 8.04 Hardy Heron. I was lucky that it worked on all my Ubuntu boxes.


Do note that the upgrading script, which was written in Python, does chew up quite a lot of memory. I have one tiny 64MB (+256MB swap) VPS that almost got killed with OOM. So be prepared, but YMMV.


So far as a server I haven’t experienced with too much differences. PostgreSQL 8.3 was in but Firebird 2.1 wasn’t (although it should be included “soon”). Now, back to more code hacking.

 

