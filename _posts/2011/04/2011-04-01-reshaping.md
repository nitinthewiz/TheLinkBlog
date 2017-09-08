---
title: "Reshaping"
date: 2011-04-01 19:00:00 +0000
external-url: http://www.tbray.org/ongoing/When/201x/2011/04/01/Straight-Right
hash: 91a534a7239478d0d593417697af2d30
annum:
    year: 2011
    month: 04
hostname: www.tbray.org
---


For the first time in years, I’m working on changing the look of this here
blog. I’ve been bored with it in recent
years, then Blaine Cook’s
Beautiful
Lines pushed me over the edge.  As of today, if you’re reading this at
tbray.org rather than in one feed
reader or another, the text is justified on both sides and hyphenated as
necessary.  There are side-effects, and I’m
not sure I’m 100% happy with the results. I am sure there’s lots more work to
do.

What Blaine Said
His piece makes three arguments:


Now we have wide variety in the pixel density on the screens we use,
extra work is required to come up with density-independent designs.

Right-justified text should be used because “Ragged right is an
abomination”.

Hyphenation, which has long been used in conjunction with right
justification, is now easily achievable with good-quality results.


Let’s take up Blaine’s points in reverse order.

Hyphenation
In this case I agree 100%.
Hyphenator.js is trivial to
install and seems to Just Work; as I consider its results, I have seen very
little so far that offends my eye.  Also, the architecture is pleasing;
it makes perfect sense to run this sort of publishing busywork on the
Web’s billions of underworked client systems, rather than on its millions of
often-overworked servers.

But there are a few little issues. 
The software works by peppering the text with soft-hyphen characters in all
the places where you might want to break words, and then leaves the work
of doing the hyphenation to the browser.

This character is Unicode U+00AD SOFT HYPHEN. Hyphenator.js wants to use the
HTML escape &shy;, which caused problems with my XML-based
publishing system that doesn’t know HTML escapes.  I was going to use
&#xad; but then realized that JavaScript literals are
supposed to be UTF-8, so I put the literal character right there in the
JavaScript source and that works fine.

Next, you have to consider the effect of having all those invisible
soft-hyphens littering your deathless prose.  Hyphenate.js does some magic
that means when you copy text out of the browser, the soft-hyphens don’t come
with it.

Also, consider the effect on in-browser search.  Type Command-F or
Control-F and search for “architecture”.  Firefox or Chrome can find it, but
Safari can’t.  I suspect that this one should be easy to crush once it comes
to Apple’s attention.

Of course, the only reason to hyphenate is to make justification work
better.  In the publishing-tech community where I spent years of my
professional life, we used to just say “H&J”.

Justification
Nothing to it; insert
text-align: justify; appropriately in your CSS and there you go.  I
do notice some subtle but obvious-to-the-eye differences in the justification
algorithm from one browser to another.  The ragged-right “abomination” is
history.
 
But I’m wondering whether it really was that bad.  I’m aware that there’s
research out there studying the effect of various techniques including
kerning and leading and H&J.  But I couldn’t find it just now.

Personally, I like justification more and more as the columns get narrower
and narrower; in book-length lines, I find ragged right to be sort of
appealing.  On the other hand, in actual real books designed by actual real
professional book designers, justification is pretty universal.

I seem also to remember that narrow columns, in the style of
newspapers, were found more readable.  But then why are book-length texts not
formatted that way?  I’m sure that somewhere on the Web there’s a high-quality
professional introduction to these issues.  On balance, I like the way that 
ongoing looks all squared-up.  But that may not last.

On Lines
Which leads to Blaine’s first point, about density-independence and line
lengths. He posted nice clever code that does 
calculations with the goal of arranging that each line has more or less the
same number of characters; then you get to have an amusing argument what the
right number is.

This code doesn’t just drop in; it needs to hook into
your page layout at just the right places. So it took a
bit of quality Firebug time to get it running.

Then I took it out again.  The layout here at ongoing is “liquid”, meaning it grows or
shrinks, within reason, should the browser be resized.  I found the effect
overly twitchy and, the more I thought about it, the more I didn’t believe
that number-of-characters-per-line is the right invariant.

When we routinely use displays whose dots-per-inch vary from 
under 100 to over 300, it
seems reasonable to worry about resolution-independence in your type
design.

But maybe not.  I think I smell an abstraction leaking.
When I say font-size: 0.95em;, I’m thinking that it’d be better
if I left it to the browser to figure out how many pixels make up the best 
“em”, bearing in mind the physics of the display.

Having said all that, I widened the center-content area on the blog here,
and increased the size to that 0.95em quoted above.  The effect, I think, is
more book than newspaper, which feels right to me.

Still To Do
I set up the basic CSS layout of this page between 2003 and 2006, stealing
mostly from
Eric Meyer.  It was bleeding-edge then but is kinda mouldy and
old-fashioned now, and doesn’t handle really wide browser windows nearly as well
as I’d like.  So I’ll have to fix that.

And then there’s fun part: fonts!  I’ve been offering readers the
choice of
Georgia and
Verdana for a long time.
Those were probably sensible options back in 2003. But
that was then, this is now. I’ve been following
the Typekit blog and glancing at
Google Web Fonts and licking my
lips a bit.

Also, I’m increasingly loathing Georgia’s italics.

It looks like it’ll be straightforward to shift the fonts in
this space.
That’s after I’ve picked new typefaces; a prospect that, frankly,
intimidates me.  I’m not even sure how to start thinking about it, but I’m
pretty sure that I’ll have fun once I do.

By the way, I shifted this in over a day ago and mostly nobody noticed.
Which is a good thing.  Oh, and thanks to Blaine!


