---
title: "Rails 2.0: It's done"
date: 2007-12-07 15:03:00 +0000
external-url: http://weblog.rubyonrails.org/2007/12/7/rails-2-0-it-s-done/
hash: 23c84ff8ad790977c17bf090b0230969
year: 2007
month: 12
scheme: http
host: weblog.rubyonrails.org
path: /2007/12/7/rails-2-0-it-s-done/

---

Rails 2.0 is finally finished after about a year in the making. This is a fantastic release thats absolutely stuffed with great new features, loads of fixes, and an incredible amount of polish. Weve even taken a fair bit of cruft out to make the whole package more coherent and lean.



What a milestone for Ruby on Rails as well. Ive personally been working on this framework for about four and a half years and we have contributors whove been around for almost as long as well. Its really satisfying to see how far weve come in that period of time. That weve proven the initial hype worthy, that weve been able to stick with it and continue to push the envelope.



Before jumping into the breakdown of features, Id just like to extend my deep gratitude towards everyone who helped make this release possible. From the stable of merry men in the Rails core to the hundreds of contributors who got a patch applied to everyone who participated in the community over the year. This release is a triumph for large-scale open source development and you can all be mighty proud of the role you played. Cheers!



With the touchy-feely stuff out of the way, lets dig into the feast and look at just a sliver of whats new:

Rails 2.0 is finally finished after about a year in the making. This is a fantastic release thats absolutely stuffed with great new features, loads of fixes, and an incredible amount of polish. Weve even taken a fair bit of cruft out to make the whole package more coherent and lean.



What a milestone for Ruby on Rails as well. Ive personally been working on this framework for about four and a half years and we have contributors whove been around for almost as long as well. Its really satisfying to see how far weve come in that period of time. That weve proven the initial hype worthy, that weve been able to stick with it and continue to push the envelope.



Before jumping into the breakdown of features, Id just like to extend my deep gratitude towards everyone who helped make this release possible. From the stable of merry men in the Rails core to the hundreds of contributors who got a patch applied to everyone who participated in the community over the year. This release is a triumph for large-scale open source development and you can all be mighty proud of the role you played. Cheers!



With the touchy-feely stuff out of the way, lets dig into the feast and look at just a sliver of whats new:



Action Pack: Resources



This is where the bulk of the action for 2.0 has gone. Weve got a slew of improvements to the RESTful lifestyle. First, weve dropped the semicolon for custom methods instead of the regular slash. So /people/1;edit is now /people/1/edit. Weve also added the namespace feature to routing resources that makes it really easy to confine things like admin interfaces:



map.namespace(:admin) do
