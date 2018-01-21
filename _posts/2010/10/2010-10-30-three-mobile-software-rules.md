---
title: "Three Mobile-Software Rules"
slug: three-mobile-software-rules
date: 2010-10-30 14:00:00 -0500
category: 
external-url: http://www.tbray.org/ongoing/When/201x/2010/10/30/Three-Android-Software-Rules
hash: e00a9eba94c45cbe488909a6b77fcd7c
year: 2010
month: 10
scheme: http
host: www.tbray.org
path: /ongoing/When/201x/2010/10/30/Three-Android-Software-Rules

---


These days, I spend quite a bit of time talking about how to write software
for Android. I think three of the general rules are worth expanding on here
because I’m increasingly convinced they apply to software in general, not just
for mobile devices.

Crash-Only
An Android app doesn’t need exit code.  You have callbacks for when you
start up, when you become active, and for when some other app takes your place and
pushes you aside; the latter two will typically be called repeatedly as the
phone’s owner switches back and forth between apps.

But there’s no need for exit code because the system can, and does, nuke
your process any time you’re not active and it needs the memory.  What that
means is that it’s your responsibility to save any state you might need in the
future, and without asking anyone to select “File/Save”, either.

At some point, after I’d explained a few times why you have to write
software this way on Android, I started wondering why all software, without
exception, isn’t written this way by default.

Loose Address/Type-Driven Coupling
The way you hand off from one screen to another in Android is with an
Intent.
An Intent has a Target, an Action, a URI, and a data type (as in Internet media-type, MIME
type), along with some ancillary stuff.  You can specify a target, essentially
a class name, and control passes to that class.  Or you can specify an action
(make a phone call, view something, delete something) and its URI and or
media-type, and let the system pick the right software to deal with it.

So, in your app, when
whenever your user taps on a URI, you fire off an Intent with the URI and the
“view” action, and control passes to his or her favorite browser.

This has the nice side-effect of pushing you on the stack, so when the
user gets tired of browsing and hits the Back button enough times, eventually
she gets back to your app.  By fiddling media-types and actions, it’s dead easy for the
user to traipse naturally between Twitter, the browser, maps, contacts,
photo-browsing, music-listening, and so on, never losing the use of the
all-important Back button.

Gosh, this notion of tying everything together loosely with addresses, data
types, and a few simple verbs
seems to have legs.  But since it
wasn’t obvious to me from first principles that it would be a good way to
construct mobile-device software, I’m wondering if maybe in general it’s a
good way to do almost everything.

Remove Decoration
We advise people that, since mobile-device screens are small, that they
have to focus on data not decoration; get rid of all the headers and trailers
and sidebars and toolbars that you can, so that the user gets the
maximum-possible amount of payload.

Computer screens, whether desktop or laptop, are by comparison huge, and
this has led to a temptation to festoon interfaces with all sorts of
decoration and apparatus and gadgets and widgets and whatever.

The fact that on the mobile screen there’s just not room for that stuff
makes me increasingly wonder how much we really need it.  With every hour I
spend traversing here and there on the Web, wincing away from sites that are
decoration-heavy and smiling at the ones that are all-message, the feeling grows.


