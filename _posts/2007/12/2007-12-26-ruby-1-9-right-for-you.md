---
title: "Ruby 1.9—Right for You?"
date: 2007-12-26 00:40:04 +0000
external-url: http://pragdave.blogs.pragprog.com/pragdave/2007/12/ruby-19right-fo.html
hash: b549673055fa9b4fda1fd3f7cfecc22e
annum:
    year: 2007
    month: 12
url-parts:
    scheme: http
    host: pragdave.blogs.pragprog.com
    path: /pragdave/2007/12/ruby-19right-fo.html

---

As is becoming a tradition, Matz announced the next major release of Ruby on Christmas day. 


Let's start by thanking both him and the entire Ruby core team for the efforts to get us here.


So, should you go and put this new Ruby to work right now? Let's see:


The Upside

This release contains a boatload of new features. Mauricio Fernandez has an impressive list (soon to be updated).



Performance: this new Ruby runs on the new YARV virtual machine. For most compute-intensive applications, you'll see significant speed improvements.

Support for string encodings and transcoding. Every string in Ruby can now have an associated encoding (ASCII, UTF-8, SJIS, and so on). You can transcode the contents of a string (for example converting ISO-8859-1 to UTF-8). 

Integrated RubyGems and rake

Cool new goodies such as Fibers



and so on and so on.


The Downside


This is a development release, not a production release. It has known bugs, and there'll be more to come. 

It contains several incompatible changes (block parameters are now block-local, String is no longer Enumerable, "cat"[1] now returns "a", rather than 65)

It is more rigorous that 1.8 when it comes to detecting invalid code. For example, 1.8 accepts /[^\x00-\xa0]/u, while 1.9 complains of invalid multibyte escapes



Because of this, and based on my experience working on the third edition of the PickAxe, a whole bunch of existing gems and other libraries are broken.


So, Should You Use It?

In production? Probably not yet. It isn't intended for production use, and there will be some rough edges.


For development? Maybe, but take note of some of the issues with gems and other libraries. If you rely on third party code, make sure it has been tested against 1.9.0 before taking the plunge. That goes for Rails users, too.


Now, if you're a library developer and gem maintainer, this is the perfect time to check out a copy of Ruby 1.9 and make sure your code is compatible. Over the coming months, more and more of your users will be basing their applications on 1.9. The future success of your gem requires compatibility.


For experimentation? Absolutely! The new features are wonderful. Not only do they make writing Ruby code even more enjoyable, they also open up whole new avenues to explore. How will fibers (both asymmetric and symmetric) affect they way we code? Let's all find out by playing with them.


My Recommendation

Download 1.9 (either as a tarball/zip file, or directly from the Subversion repository). Build it and install it, but not as your default Ruby. Instead, use the --prefix option to put it somewhere else (I store it under my home directory, so I don't need to be root). 






$ autoconf
$ ./configure --prefix=/Users/dave/ruby19
$ make
$ make install





Then, I just add /Users/dave/ruby19/bin to my path, and I'm using my nicely sandboxed version of Ruby 1.9.






$ PATH=/Users/dave/ruby19/bin:$PATH
$ ruby -v 
ruby 1.9.0 (2007-12-26 revision 0) [i686-darwin8.11.1]





If I install gems with that version in my path, they get installed into the sandbox, not globally. If I use the sandboxed version of Ruby when building extension libraries with extconf.rb, those extensions install into the sandbox. But, if I suddenly have to look at a problem in production code that means I have to use Ruby 1.8, I simply fire up another shell with my original PATH, and it's as if Ruby 1.9 doesn't exist.


1.9 is the future of Ruby, and it's a future that will be mainstream very soon. Start playing with it now, so you'll be up to speed when Matz creates his first production release.


