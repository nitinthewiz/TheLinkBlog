---
title: "Gravatar: Big changes afoot"
slug: gravatar-big-changes-afoot
date: 2008-03-14 16:11:47 -0500
category: 
external-url: http://blog.gravatar.com/2008/03/14/big-changes-afoot/
hash: 369e226a9f8aa471f81d12392e457cae
year: 2008
month: 03
scheme: http
host: blog.gravatar.com
path: /2008/03/14/big-changes-afoot/

---

Howdy everyone!  Its been an exciting few months for us since weve taken on the role of helping Gravatar grow.  Weve been doing a lot of work to get those gears turning, and set things up for some serious forward motion.

The first thing we did, after stabilizing the service, was set out to rewrite Gravatar in PHP.  Now before we launch into any holy wars Id like to point out that our decision on this matter had nothing to do with Ruby, or Rails  in fact we have a great respect for both!  The reason, the only reason, we switched is that PHP is our core competency at Automattic.  As a PHP application we will be able to apply the sum total of our collective abilities to bear on any problems that Gravatar might face.  The guys I work with are genuinely some of the most technically gifted people I know!

Of the things that you might notice there are a couple which will be most prominent.  First off the speed of the user interface has increased dramatically especially when it comes to applying your uploaded imaged to your email addresses, a process which used to take minutes.  Weve fixed the biggest issue with the cropper (it would throw an error if you tried to use an image that was already 8080 pixels or smaller.)

Now for some things that you probably have not noticed.

We have increased the size limit for avatars to 512 pixels (thats a big avatar!)  With existing gravatars the image will be pixelated at 512, but new gravatars created from from higher resolution images will be very clear. For backwards compatibility the default size for serving images with no specific requested size will be the 80 pixel version.


You can now abbreviate the avatar.php options as follows: size=80 can be s=80, rating=PG can be r=PG, default=foo can now be d=foo.  The rating is also case insensitive (r=PG is the same as r=pg). Oh and gravatar_id=foo can be g=foo, not that youll need it because weve implemented a new cleaner URL API.  Our new API is actually really simple, and not a huge departure from the original URL structure.

http://www.gravatar.com/avatar/767fc9c115a1b989744c755db47feb60

All of the aforementioned get parameters still work, such as ?s=80&r=g&default=http%3A%2F%2Fwww.mysite.com%2Fimage.jpg  Also, for convenience and compatibility with certain software (for example some forum software wont allow you to use a url as an avatar if it doesnt have an image extension), you can append .jpg to the end of the MD5 of the email

http://www.gravatar.com/avatar/767fc9c115a1b989744c755db47feb60.jpg?s=128&r=g

Weve also added support for gravatar images over SSL (please use the hostname secure.gravatar.com for this)!

https://secure.gravatar.com/avatar/767fc9c115a1b989744c755db47feb60

We have lots more stuff planned to make Gravatar.com a great service for everyone, so stay tuned!
