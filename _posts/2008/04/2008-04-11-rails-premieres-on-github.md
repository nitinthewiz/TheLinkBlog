---
title: "Rails premieres on GitHub"
date: 2008-04-11 14:45:00 +0000
external-url: http://weblog.rubyonrails.org/2008/4/11/rails-premieres-on-github/
hash: 5acae77563d9223e5c03c836ef6c3da8
year: 2008
month: 04
scheme: http
host: weblog.rubyonrails.org
path: /2008/4/11/rails-premieres-on-github/

---

GitHub has now officially launched and Rails is right there at the premiere. The Rails repository now lives at rails/rails and you can check it out with:



git clone git://github.com/rails/rails.git


If you dont have git, or dont enjoy running it on your platform, you need not fear. Weve set up an automated task to produce a zip file of Rails Edge thatll be kept up to date all the time: http://dev.rubyonrails.org/archives/rails_edge.zip. This is also what weve made the new rake rails:freeze:edge use.



This also means that development on the Subversion repository has stopped and will no longer be kept up to date. Well keep the Subversion repository around for some time for people to transition off svn:externals, though. But if you want the latest edge, youll have to use either git or the new zip files.



Well also soon go live with our new ticket management system, which will be running on a new version of Lighthouse. When that happens, the Trac installation will follow the Subversion repository into legacy. Well still keep it around so we can work through all the patches and tickets that are there, but everything new will happen on the Lighthouse setup.



We hope youll enjoy this upgrade to the Rails collaboration infrastructure. Were really looking forward to the onslaught of marvelous patches that the Git lords have promised us will flow from the mountain now.
